# henripaul
import pygame
pygame.init()

# vajalikud read, et ekraan tootaks
ekraanx, ekraany = 640, 480
screen = pygame.display.set_mode((ekraanx, ekraany))
pygame.display.set_caption("pingpong - irneh")
background_color = (135, 206, 250)

# toob palli mangu
pallisuurus = 20
pallipilt = pygame.image.load("ball.png")
pallipilt = pygame.transform.scale(pallipilt, (pallisuurus, pallisuurus))
pallx = ekraanx // 2 - pallisuurus // 2
pally = ekraany // 2 - pallisuurus // 2
pallikiirus_x = 3
pallikiirus_y = 3

# toob aluse mangu
alus_width, alus_height = 120, 20
alus_image = pygame.image.load("pad.png")
alus_image = pygame.transform.scale(alus_image, (alus_width, alus_height))
alus_x = ekraanx // 2 - alus_width // 2
alus_y = int(ekraany / 1.5)
alus_speed = 5

# skoorisusteem
score = 0
score_font = pygame.font.SysFont("Arial", 36)

# mang ise, "manguloop"
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # aluse kontrollimine
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and alus_x > 0:
        alus_x -= alus_speed
    if keys[pygame.K_RIGHT] and alus_x < ekraanx - alus_width:
        alus_x += alus_speed

    pallx += pallikiirus_x
    pally += pallikiirus_y

    # kokkuporge seintega
    if pallx <= 0 or pallx >= ekraanx - pallisuurus:
        pallikiirus_x *= -1
    if pally <= 0:
        pallikiirus_y *= -1

    # kokkuporge alusega
    if (
        pally + pallisuurus >= alus_y
        and pallx + pallisuurus >= alus_x
        and pallx <= alus_x + alus_width
    ):
        pallikiirus_y *= -1
        score += 1

    # kokkuporge alumise ekraani aarega
    if pally + pallisuurus >= ekraany:
        pally = ekraany - pallisuurus
        pallikiirus_y *= -1
        score -= 1

    # vajalikud read, et mang tootaks
    screen.fill(background_color)
    screen.blit(pallipilt, (pallx, pally))
    screen.blit(alus_image, (alus_x, alus_y))

    # kuvab skoori
    score_text = score_font.render("skoor: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
