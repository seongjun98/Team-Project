# 메소드(9팀) - 팀 프로젝트

from turtle import done
import pygame
import random
import bomb
import person

# 게임판 구성
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

bomb.init(SCREEN_WIDTH, SCREEN_HEIGHT)
person.init(SCREEN_WIDTH, SCREEN_HEIGHT)

# 배경이미지
# background = pygame.image.load("background.png")

# 난수 생성 - 똥 생성용
randomNumber = 30
poSpeed = 10

# 게임 플레이 총 시간
totalTime = 10
startTicks = pygame.time.get_ticks()

heartfont = pygame.font.SysFont("arial", 30, True, True)
heart3 = heartfont.render("♥ ♥ ♥", True, (0, 0, 0))
heart2 = heartfont.render("  ♥ ♥", True, (0, 0, 0))
heart1 = heartfont.render("    ♥", True, (0, 0, 0))


def runGame():
    run = True

    Gaming = True  # 시작 버튼을 눌렀을 경우
    heart = 3  # 시작 버튼을 눌렀을 경우

    while run:
        screen.fill((255, 255, 255))
        dt = clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if Gaming:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        person.moveX(-1)
                    if event.key == pygame.K_RIGHT:
                        person.moveX(1)
                    if event.key == pygame.K_UP:
                        person.moveY(-1)
                    if event.key == pygame.K_DOWN:
                        person.moveY(1)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        person.toX = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        person.toY = 0
        if Gaming:
            person.run(screen)
            bomb.run(screen)
            pp = person.getPos()
            for b in bomb.explosion:
                if b['hit']:
                    continue
                if (b['rect'].left <= pp['x'] <= b['rect'].left + b['scale']) and (
                        b['rect'].top <= pp['y'] <= b['rect'].top + b['scale']):
                    heart -= 1
                    b['hit'] = True
                    if heart <= 0:
                        Gaming = False
                    break
            if heart == 3:
                screen.blit(heart3, (500, 0))
            elif heart == 2:
                screen.blit(heart2, (500, 0))
            elif heart == 1:
                screen.blit(heart1, (500, 0))

        pygame.display.update()

    pygame.quit()


runGame()
