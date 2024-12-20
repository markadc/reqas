from abc import abstractmethod, ABC

from reqas.response import Response as HaderResponse
from reqas.tools import make_ua


class SpiderPlugin(ABC):
    @abstractmethod
    def deal_response(self, response):
        pass

    @abstractmethod
    def deal_request(self, request):
        pass


class UserAgentPlugin(SpiderPlugin):
    def deal_request(self, request):
        request.headers = request.headers or {}
        request.headers.setdefault('User-Agent', make_ua())

    def deal_response(self, response):
        return response


class ResponsePlugin(SpiderPlugin):
    def deal_request(self, request):
        pass

    def deal_response(self, response):
        return HaderResponse(response)
