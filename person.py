import pygame
import random

global SCREEN_WIDTH
global SCREEN_HEIGHT

# 캐릭터
character = pygame.image.load("character.png")
characterSize = character.get_rect().size  # img크기 불러옴
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXpos = (SCREEN_WIDTH / 2) - (characterWidth / 2)
characterYpos = SCREEN_HEIGHT - characterHeight

# 이동할 좌표
toX = 0
toY = 0

# 이동속도
characterSpeed = 1

# 난수 생성 - 똥 생성용
randomNumber = 30
poSpeed = 10

# Title

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트, 크기

# 게임 플레이 총 시간
totalTime = 10
startTicks = pygame.time.get_ticks()


def key():
    global toX, toY
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            toX -= characterSpeed
        if event.key == pygame.K_RIGHT:
            toX += characterSpeed
        if event.key == pygame.K_UP:
            toY -= characterSpeed
        if event.key == pygame.K_DOWN:
            toY += characterSpeed
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            toX = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            toY = 0

            # 캐릭터 이동 & 프레임맞추기


characterXpos += toX * dt
characterYpos += toY * dt

# 경계 설정-가로
if characterXpos < 0:
    characterXpos = 0
elif characterXpos > SCREEN_WIDTH - characterWidth:
    characterXpos = SCREEN_WIDTH - characterWidth

# 경계 설정-세로
if characterYpos < 0:
    characterYpos = 0
elif characterYpos > SCREEN_HEIGHT - characterHeight:
    characterYpos = SCREEN_HEIGHT - characterHeight

screen.blit(background, (0, 0))
screen.blit(character, (characterXpos, characterYpos))
pygame.display.update()  # 화면 새로고침

pygame.quit()  # pygame 종료
