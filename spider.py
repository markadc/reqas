from reqas import Request
from reqas.plugins import SpiderPlugin, UserAgentPlugin, ResponsePlugin


class BaseSpider:
    plugins: list[SpiderPlugin] = []

    def on_request(self, request: Request):
        for plugin in self.plugins:
            plugin.deal_request(request)

    def on_response(self, response):
        new_response = response
        for plugin in self.plugins:
            new_response = plugin.deal_response(new_response)
        return new_response

    def add_plugin(self, plugin: SpiderPlugin):
        self.plugins.append(plugin)

    def add_plugins(self, plugins: list[SpiderPlugin]):
        for plugin in plugins:
            self.add_plugin(plugin)

    def goto(self, url: str, headers: dict = None, params: dict | str = None, data: dict = None, json: dict = None, proxies: dict = None, timeout: int | float = 5, **kwargs):
        request = Request(url, headers=headers, params=params, data=data, json=json, proxies=proxies, timeout=timeout, **kwargs)
        self.on_request(request)
        response = request.do()
        new_response = self.on_response(response)
        new_response.request = request
        return new_response


class Spider(BaseSpider):
    plugins: list[SpiderPlugin] = [UserAgentPlugin(), ResponsePlugin()]
