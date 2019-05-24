
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = 50
y = 50

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Rpg prototype")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            y += 20

    
    screen.fill((0, 0, 0))
    # Beginning of Drawing

    pygame.draw.rect(screen, WHITE, [x, y, 50, 50])

    # End of Drawing
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
