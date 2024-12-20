from reqas import BaseSpider, Spider
from reqas.plugins import UserAgentPlugin, ResponsePlugin

url = 'https://blog.csdn.net/MarkAdc'

# 1. 基础爬虫
s = BaseSpider()
r = s.goto(url)
print(r)
print(r.headers)
print(r.request.headers)
print(dir(r))
print()

# 2. 基础爬虫 + ua插件 + 响应插件（可以使用Xpath、CSS）
s = BaseSpider()
s.add_plugins([UserAgentPlugin(), ResponsePlugin()])
r = s.goto(url)
print(r)
print(r.headers)
print(r.request.headers)
print(dir(r))
print()

# 3. 标准爬虫，等价于 基础爬虫 + ua插件 + 响应插件
s = Spider()
r = s.goto(url)
print(r)
print(r.headers)
print(r.request.headers)
print(dir(r))
