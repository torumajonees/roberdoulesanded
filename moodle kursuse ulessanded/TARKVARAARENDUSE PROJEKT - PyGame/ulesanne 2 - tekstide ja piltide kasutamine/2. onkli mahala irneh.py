#henri paul

import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#Lisame tausta
bg = pygame.image.load("bg_shop.png")
screen.blit(bg,[0,0])

#lisame poeonkli
seller = pygame.image.load("seller.png")
seller = pygame.transform.scale(seller, [265,308])
screen.blit(seller,[100,155])

#lisame jutumulli
chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [250,200])
screen.blit(chat,[250,70])

#jutumulli tekst
font = pygame.font.Font(pygame.font.match_font('Times New Roman'), 20)
text = font.render("Tere, olen henri paul", True, [255, 255, 255])
text_width = text.get_rect().width
text_height = text.get_rect().height
screen.blit(text, [300-text_width/10, 150-text_height/5])
pygame.display.flip()

#terve see oogabooga tsukkel on koigest selle jaoks, et ekraan kuvama jaaks
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#selle oogabooga lopp