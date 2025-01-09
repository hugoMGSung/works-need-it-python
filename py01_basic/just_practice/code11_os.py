import os  # os패키지를 이제부터 가져다 쓸거야!

print(f'OS 환경 : {os.environ}')

print(f'현재 경로 : {os.getcwd()}')

print(os.system('dir'))

# 파일 경로내 모든 폴더, 파일 리스트
import glob

print(glob.glob('D:/01_Programming/100_HugoBank/Mine/kamp-cloning/*'))