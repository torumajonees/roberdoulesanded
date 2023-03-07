# henripaul
import pygame

# vajalikud read, et ekraan tootaks
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("pingpong - irneh")
ooga = pygame.time.Clock()
booga = 0  # see naitab meie skoori

# peab ulal nurgas skoori, loendab meie nn "punkte"
screen.blit(pygame.font.Font(None, 32).render(f"skoor: {booga}", True, [255, 255, 255]), [15, 12])

pygame.display.flip()  # varskendab ekraani

# terve see oogabooga tsukkel on koigest selle jaoks, et ekraan kuvama jaaks
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()  # et ta kinni ka laheks ikka
