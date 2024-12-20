import requests


class Request:
    """请求对象"""

    def __init__(self, url: str, method="GET", headers: dict = None, params: dict | str = None, data: dict = None, json: dict = None, proxies: dict = None, timeout: int | float = 5, **kwargs):
        self.url = url
        self.method = method
        self.headers = headers
        self.params = params
        self.data = data
        self.json = json
        self.proxies = proxies
        self.timeout = timeout
        self.kwargs = kwargs

    def do(self):
        if self.method == "GET":
            response = requests.get(
                self.url,
                headers=self.headers, params=self.params,
                data=self.data, json=self.json,
                proxies=self.proxies, timeout=self.timeout,
                **self.kwargs
            )
            return response


if __name__ == '__main__':
    req = Request("https://www.baidu.com")
    r = req.do()
    print(r, len(r.text))
