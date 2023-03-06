#henripaul

import pygame #impordib vajalikud failid, et programm tootaks
pygame.init()

screen = pygame.display.set_mode([300,300]) #loob akna, kus programm kuvatakse
pygame.display.set_caption("valgusfoor - henri paul") #lisab aknale pealkirja

#foori varvid
pygame.draw.circle(screen, [255, 0, 0], [150, 65], 40)
pygame.draw.circle(screen, [255, 255, 0], [150, 150], 40)
pygame.draw.circle(screen, [64, 255, 0], [150, 235], 40)

#foori post
pygame.draw.rect(screen, [124, 124, 124], [100, 17, 100, 267], 2)

pygame.display.flip() #varskendab vajaliku osa ekraanist, et kuvaks valgusfoor

#terve see oogabooga tsukkel on koigest selle jaoks, et ekraan kuvama jaaks
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#võimaldab sulgeda akent
pygame.quit()
