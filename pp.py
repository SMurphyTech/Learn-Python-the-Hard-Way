import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PI = 3.141592653

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("cool game by me haha")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # if event.type == pygame.KEYUP:
            


    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, [100, 400, 500, 100], 3)

    #for y_offset in range(0, 380, 10):
        #pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)
        #pygame.draw.polygon(screen, BLACK, [[100, 100 + y_offset], [0, 200 + y_offset], [200+ y_offset, 200+ y_offset], [300+ y_offset, 100+ y_offset]], 5)

    pygame.draw.ellipse(screen, GREEN, [250, 190, 200, 200], 2)
    pygame.draw.ellipse(screen, RED, [220, 330, 130, 70], 2)
    pygame.draw.ellipse(screen, RED, [350, 330, 130, 70], 2)
    pygame.draw.ellipse(screen, GREEN, [250, 190, 60, 60], 2)
    pygame.draw.ellipse(screen, GREEN, [420, 270, 60, 60], 2)

    # pygame.draw.arc(screen, GREEN, [100,100,250,200],  PI/2,     PI, 2)
    # pygame.draw.arc(screen, BLACK, [100,100,250,200],     0,   PI/2, 2)
    # pygame.draw.arc(screen, RED,   [100,100,250,200],3*PI/2,   2*PI, 2)
    # pygame.draw.arc(screen, BLUE,  [100,100,250,200],    PI, 3*PI/2, 2)
    
    #pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200], [300, 100]], 5)

    pygame.draw.polygon(screen, BLACK, [[100, 100], [140, 200], [220, 200], [150, 250], [180, 330], [100, 280], [20, 330], [50, 250], [-20, 200], [60, 200]], 5)

    # font = pygame.font.SysFont('Calibri', 25, True, False)
    # text = font.render("My stupid", True, BLACK)
    # screen.blit(text, [250, 250])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
