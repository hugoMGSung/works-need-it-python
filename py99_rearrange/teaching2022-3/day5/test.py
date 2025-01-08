import os

PRJ_ROOT = os.path.dirname(os.path.abspath(__file__))
print(PRJ_ROOT) # py 파일이 위치한 경로

BASE_DIR = os.path.dirname(PRJ_ROOT)
print(BASE_DIR) # 프로젝트 기반 폴더 경로

f = open('./test_console.txt', mode='w', encoding='utf-8')
f.write('Hello World\n')
f.close()