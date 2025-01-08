# 네이버 웹페이지 긁어오기1
from urllib.request import Request, urlopen

req = Request('https://www.naver.com/')
res = urlopen(req)
print(res.status)