# henripaul
import pygame
import random
import sys

# vajalikud read, et ekraan ning moned pisidetailid tootaksid
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("rallimang - irneh")
clock = pygame.time.Clock()
score = 0

# taustapilt
taust = pygame.image.load("bg_rally.jpg")
taust2 = pygame.image.load("bg_rally.jpg")  # lisame ka teise taustapildi mida on vaja animeerimiseks
taustposX = 0  # taustapilt uhes kohas
taust2posX = 480  # samasugune taustapilt teises kohas
taustspeedX = -3  # siin sunnib maagia, kus pilt justkui "animeeritakse"
screen.blit(taust, (0, taustposX))
screen.blit(taust2, (0, taust2posX))

# laeme sisse punase auto
punaneauto = pygame.image.load("f1_red.png")
punaneautoPosX, punaneautoPosY = 300, 385
punaneautokiirus = 0

# laeme sisse sinise auto ning tema kaksiku, sinise auto 2
sinineauto = pygame.image.load("f1_blue.png")
sinineauto = pygame.transform.rotate(sinineauto, 180)
sinineauto2 = pygame.image.load("f1_blue.png")
sinineauto2 = pygame.transform.rotate(sinineauto2, 180)
sinineautoPosY = random.randint(0, 100)
sinineauto2PosY = random.randint(0, 100)
sinineautoX = random.randint(300, 460)
sinineauto2PosX = random.randint(130, 280)
sinineautokiirus = 0

pygame.display.flip()

# kerge tsukkel, et asjad toimiksid korraparaselt
gameover = False
while not gameover:
    clock.tick(60)

# tausta animatsioon, ehk meie "liikuv autotee"
    screen.blit(taust, (0, taustposX))
    screen.blit(taust2, (0, taust2posX))
    taustposX -= taustspeedX
    taust2posX -= taustspeedX

    if taustposX >= 480:
        taustposX = -480
    if taust2posX >= 480:
        taust2posX = -480

# peab ulal nurgas skoori, loendab meie nn "punkte"
    screen.blit(pygame.font.Font(None, 32).render(f"skoor: {score}", True, [255, 255, 255]), [15, 12])

# maagia abil volume punase auto ekraanile
    screen.blit(punaneauto, (punaneautoPosX, punaneautoPosY))

# punase auto juhitavus nn "virtuaalne rool"
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:  # sellega saame tiirutada vasakule
        punaneautoPosX -= 8
    if key[pygame.K_RIGHT]:  # ning sellega paremale poole
        punaneautoPosX += 8

# maagia abil volume valja ka paar sinist autot
    screen.blit(sinineauto, (sinineautoX, sinineautoPosY))
    screen.blit(sinineauto2, (sinineauto2PosX, sinineauto2PosY))

# siniste autode kiirused
    sinineautoPosY += sinineautokiirus + 4
    sinineauto2PosY += sinineautokiirus + 4

# siniste autode genereerimine ning skoori loendamine
    if sinineautoPosY >= 480:
        sinineautoPosY = -120
        score += 1
        sinineautoX = random.randint(125, 260)

    if sinineauto2PosY >= 480:
        sinineauto2PosY = -120
        score += 1
        sinineauto2PosX = random.randint(295, 470)

# kui punane auto soidab sinisele autole sisse, lopetatakse mang
    if punaneautoPosY + 30 >= sinineautoPosY >= punaneautoPosY - 70:
        if punaneautoPosX + 30 >= sinineautoX >= punaneautoPosX - 30:
            gameover = True

    if punaneautoPosY + 30 >= sinineauto2PosY >= punaneautoPosY - 70:
        if punaneautoPosX + 30 >= sinineauto2PosX >= punaneautoPosX - 30:
            gameover = True

    pygame.display.flip()

# tsukkel, et ekraan pusima jaaks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

pygame.quit()  # et ta kinni ka laheks ikka
