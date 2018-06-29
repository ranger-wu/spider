
from urllib.parse import urlencode
from urllib.request import Request, urlopen

args = {
    'wd': '尚学堂',
    'ie': 'utf-8'
}
url = 'http://www.baidu.com/s?'+ urlencode(args)
headers = {
    'User_Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
}

request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())



