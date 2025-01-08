'''
웹페이지 크롤링 파이선 소스
디버깅하면서 HTML 소스 읽어봐야 함
'''
import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.yahoo.com/").text
soup = BeautifulSoup(source, "html.parser")
hotWords = soup.select("trending-list")

index = 0
for item in hotWords:
    index += 1
    print(str(index) + ", " + item.text)

    if index >= 20:
        break