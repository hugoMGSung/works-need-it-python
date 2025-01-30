import pygame

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption('BALL')
iconImg = pygame.image.load('./images/game-controller.png')
pygame.display.set_icon(iconImg)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ball_x = int(WINDOW_WIDTH / 2)
ball_y = int(WINDOW_HEIGHT / 2)
ball_dx = 10
ball_dy = 10
ball_size = 40

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    ball_x += ball_dx
    ball_y += ball_dy

    # 공이 윈도우를 벗어날 경우
    if (ball_x + ball_size) > WINDOW_WIDTH or (ball_x - ball_size) < 0:
        ball_dx = ball_dx * -1
    if (ball_y + ball_size) > WINDOW_HEIGHT or (ball_y - ball_size) < 0:
        ball_dy = ball_dy * -1

    screen.fill(BLACK)

    # 공 그리기
    pygame.draw.circle(screen, BLUE, [ball_x, ball_y], ball_size, 0)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()