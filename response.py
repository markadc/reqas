from parsel import Selector
from requests import Response as BaseResponse


class Response(BaseResponse):
    """响应对象"""

    def __init__(self, response: BaseResponse):
        super().__init__()
        self.__dict__.update(response.__dict__)
        self.selector = Selector(text=response.text)

    def __str__(self):
        return "<Response {}>".format(self.status_code)

    def xpath(self, query: str):
        sel = self.selector.xpath(query)
        return sel

    def css(self, query: str):
        sel = self.selector.css(query)
        return sel

    def get_one(self, query: str, default=""):
        value = self.selector.xpath(query).get(default).strip()
        return value

    def get_all(self, query: str):
        value = [v.strip() for v in self.selector.xpath(query).getall()]
        return value
