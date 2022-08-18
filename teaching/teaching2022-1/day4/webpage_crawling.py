# 웹페이지 긁어오기
# from urllib.request import Request, urlopen

# req = Request('https://www.naver.com') # 네이버 웹페이지 요청
# res = urlopen(req)

# print(res.status)

# 외부 request 패키지 추가 설치
# pip install requests
# import requests
# url = 'https://www.naver.com'
# res = requests.get(url)

# # print(res.status_code)
# print(res._content)

from urllib.request import Request, urlopen
url = 'https://www.yahoo.com'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urlopen(req).read()

print(res)
