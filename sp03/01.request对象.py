'''
#这是简单的爬取页面:  方法一:
from urllib.request import urlopen
from urllib.request import Request

url = 'http://www.shsxt.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
request = Request(url, headers=headers)
print(request.get_header('User-Agent'))
resp = urlopen(request)
print(resp.read().decode())
'''



# 方法二:
import requests

url = 'http://www.shsxt.com'
response = requests.get(url)
#response.encoding='utf-8'
html = response.content.decode()

#html = response.text
print(html)

'''
总结:①虽然方法二比方法一要简便,但它适应于没有反爬设置的网页,用来获取简单的网页源代码!

②:http 与https 区别   后者带有安全证书认证,爬的时候需要有个忽略证书项的操作!
③:获取页面 html = response.text  与  html = response.content.decode()区别: 
 前者需要对响应的内容做个编码:response.encoding='utf-8';后者直接对内容解码:response.content.decode()
 

'''

'''
问题:
url = 'http://www.shsxt.com'
response = requests.get(url)
#response.encoding='utf-8'
html = response.read().decode()
print(html)
'''