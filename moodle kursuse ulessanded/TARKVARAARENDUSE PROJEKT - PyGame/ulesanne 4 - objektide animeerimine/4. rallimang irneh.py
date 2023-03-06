# henripaul
import pygame
import random
import sys

# vajalikud read, et ekraan luua
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("rallimang - irneh")
clock = pygame.time.Clock()

# taustapilt
taust = pygame.image.load("bg_rally.jpg")
taust2 = pygame.image.load("bg_rally.jpg")  # lisame ka teise taustapildi mida on vaja animeerimiseks
taustposX = 0  # esimese tausapildi positsioon
taust2posX = 480  # teine taustapildi positsioon
taustspeedX = -3  # taustapildi kiirus
screen.blit(taust, (0, taustposX))
screen.blit(taust2, (0, taust2posX))

# laeme sisse punase auto
punaneauto = pygame.image.load("f1_red.png")
punaneautoPosX, punaneautoPosY = 298, 390  # punase auto asukoht
punaneautokiirus = 0

# laeme sisse sinise auto ning tema kaksiku, sinise auto 2
sinineauto = pygame.image.load("f1_blue.png")
sinineauto = pygame.transform.rotate(sinineauto, 180)
sinineauto2 = pygame.image.load("f1_blue.png")
sinineauto2 = pygame.transform.rotate(sinineauto2, 180)
sinineautoPosY = random.randint(0, 100)  # sinise auto positsioon Y
sinineauto2PosY = random.randint(0, 100)  # sinise auto 2 positsioon Y
sinineautoX = random.randint(300, 460)  # sinise auto positsioon X
sinineauto2PosX = random.randint(130, 280)  # sinise auto 2 positsioon X
sinineautokiirus = 0

pygame.display.flip()

#
gameover = False
while not gameover:
    clock.tick(60)

# tausta animatsioon "auto tee"
    screen.blit(taust, (0, taustposX))
    screen.blit(taust2, (0, taust2posX))
    taustposX -= taustspeedX
    taust2posX -= taustspeedX

    if taustposX >= 480:
        taustposX = -480
    if taust2posX >= 480:
        taust2posX = -480

# maagika abil volume punase auto ekraanile
    screen.blit(punaneauto, (punaneautoPosX, punaneautoPosY))

# punase auto juhtivus "virtuaalne rool"
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:  # sellega saame tiirutada vasakule
        punaneautoPosX -= 8
    if key[pygame.K_RIGHT]:  # ning sellega paremale poole
        punaneautoPosX += 8

# maagia abil volume valja ka sinised autod
    screen.blit(sinineauto, (sinineautoX, sinineautoPosY))
    screen.blit(sinineauto2, (sinineauto2PosX, sinineauto2PosY))

# siniste autode kiirused
    sinineautoPosY += sinineautokiirus + 4
    sinineauto2PosY += sinineautokiirus + 4

# siniste autode genereerimine
    if sinineautoPosY >= 480:
        sinineautoPosY = -120
        sinineautoX = random.randint(125, 260)

    if sinineauto2PosY >= 480:
        sinineauto2PosY = -120
        sinineauto2PosX = random.randint(295, 470)

    pygame.display.flip()

# tsukkel, et ekraan pusima jaaks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# kui punane auto soidab sinisele autole sisse, lopetatakse mang
    if punaneautoPosY + 30 >= sinineautoPosY >= punaneautoPosY - 30:
        if punaneautoPosX + 30 >= sinineautoX >= punaneautoPosX - 30:
            gameover = True

    if punaneautoPosY + 30 >= sinineauto2PosY >= punaneautoPosY - 30:
        if punaneautoPosX + 30 >= sinineauto2PosX >= punaneautoPosX - 30:
            gameover = True

pygame.quit()  # et ta kinni ka laheks ikka
