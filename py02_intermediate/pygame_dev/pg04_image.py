import pygame
import os

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 320

# 색 정의
LAND = (160, 120, 40)

pygame.init()
pygame.display.set_caption('Image')
iconImg = pygame.image.load('./images/game-controller.png')
pygame.display.set_icon(iconImg)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, '../../assets')

# 배경 이미지 로드
background_image = pygame.image.load(os.path.join(assets_path, 'terrain.png'))

# 이미지 로드
mushroom_image_1 = pygame.image.load(os.path.join(assets_path, 'mushroom1.png'))
mushroom_image_2 = pygame.image.load(os.path.join(assets_path, 'mushroom2.png'))
mushroom_image_3 = pygame.image.load(os.path.join(assets_path, 'mushroom3.png'))

done = False

while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(LAND)

    # 화면 그리기 구간
    # 베경 이미지 그리기
    screen.blit(background_image, background_image.get_rect())

    # 버섯 이미지 그리기
    screen.blit(mushroom_image_1, [100, 80])
    screen.blit(mushroom_image_2, [300, 100])
    screen.blit(mushroom_image_3, [450, 140])

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()