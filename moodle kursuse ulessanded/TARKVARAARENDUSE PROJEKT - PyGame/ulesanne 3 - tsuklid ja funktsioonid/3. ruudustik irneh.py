#henripaul
import pygame

#vajalikud read, et ekraan luua
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("ruudustik - irneh")

#varvid, mida mu programm kasutada saaks
bluu = [65, 51, 122]
federal = [14, 14, 82]
screen.fill(federal)

class ruut:
    def __init__(self, color, ooga, booga):
        self.color = color
        self.ooga = ooga
        self.booga = booga

    def make_square(self):
        y = 1
        for i in range(35):
            x = 1
            for j in range(38):
                pygame.draw.rect(screen, self.color, [x, y, self.ooga, self.booga])
                x += 18
            y += 18

ruut.make_square(ruut(bluu, 16, 16))

pygame.display.flip()

#terve see oogabooga tsukkel on koigest selle jaoks, et ekraan kuvama jaaks
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit() #et ta kinni ka laheks ikka