## file : at01_first.py
## desc : 자동화 테스트

## > pip install pyautogui

import pyautogui as auto

print(auto.size()) # 모니터 해상도
print(auto.position()) # 현재 마우스 커서 위치

# 마우스 정보
# auto.mouseInfo()

# 절대 좌표로 이동
auto.moveTo(100, 100)                 # 100, 100 위치로 즉시 이동
auto.moveTo(500, 500, duration=1.5)   # 500, 500 위치로 1.5초간 이동

# 마우스 클릭
auto.click(clicks=1, interval=0.2, button='right')

# ... 계속