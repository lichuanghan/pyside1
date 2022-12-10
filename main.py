import urllib
import urllib.request
import ssl  # 导入Python SSL处理模块

# 如果网站的SSL证书是经过CA认证，就需要单独处理SSL证书，让程序忽略SSL证书验证错误，即可正常访问
context = ssl._create_unverified_context()  # 忽略安全
url = "https://www.baidu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}

# url 作为Request()方法的参数，构造并返回一个Request对象
request = urllib.request.Request(url, headers=headers)

# Request对象作为urlopen()方法的参数，发送给服务器并接收响应
# 在urlopen()方法里 指明添加 context 参数
response = urllib.request.urlopen(request, context=context).read()
print(response.decode("utf-8"))
