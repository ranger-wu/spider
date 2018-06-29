from urllib.request import urlopen
from urllib.request import Request
import random

url = 'http://www.shsxt.com'
user_Agent = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'

]
headers = {
    'User_Agent':random.choice(user_Agent)
}
request = Request(url, headers=headers)
response = urlopen(request)
html = response.read().decode()
print(html)