# file: prac03_function.py
# desc: 함수만들기
from urllib.request import Request, urlopen
import webbrowser 

def get_url(name):
	req = Request(f'https://www.{name}.com/')
	res = urlopen(req)
	print(res)

get_url('google')

