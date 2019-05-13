import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WARM_RED = (229, 2, 78)
DARK_RED = (145, 1, 49)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (34, 31, 147)
PURPLE = (255, 0, 255)
PINK = (255, 122, 210)
YELLOW = (255, 239, 22)

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

    # box
    pygame.draw.rect(screen, DARK_BLUE, [100, 420, 500, 80], 0)
    pygame.draw.rect(screen, BLUE, [100, 200, 500, 220], 0)

    # makes the stitch pattern
    for y_offset in range(-100, 700, 20):
        pygame.draw.line(screen, BLUE, [0 + y_offset, 0], [100 + y_offset, 110], 5)
        pygame.draw.line(screen, PURPLE, [0 + y_offset + 10, 0], [100 + y_offset + 10, 110], 5)

    for y_offset in range(-100, 700, 20):
        pygame.draw.line(screen, BLUE, [100 + y_offset, 0], [0 + y_offset, 110], 5)
        pygame.draw.line(screen, PURPLE, [100 + y_offset + 10, 0], [0 + y_offset + 10, 110], 5)

    # for y_offset in range(-100, 700, 20):
        # pygame.draw.line(screen, BLUE, [100 + y_offset, 110], [0 + y_offset, 220], 5)
        # pygame.draw.line(screen, PURPLE, [100 + y_offset + 10, 110], [0 + y_offset + 10, 220], 5)

    # Kirby's left foot
    pygame.draw.ellipse(screen, RED, [220, 330, 130, 70], 0)
    # Kirby's right foot
    pygame.draw.ellipse(screen, RED, [350, 330, 130, 70], 0)

    # Kirby's body
    pygame.draw.ellipse(screen, PINK, [250, 190, 200, 200], 0)

    # Kirby's left nub
    pygame.draw.ellipse(screen, PINK, [245, 185, 60, 60], 0)
    # Kirby's right nub
    pygame.draw.ellipse(screen, PINK, [420, 270, 60, 60], 0)

    # Kirby's left eye
    pygame.draw.ellipse(screen, BLACK, [300, 230, 30, 60], 0)
    # Kirby's right eye
    pygame.draw.ellipse(screen, BLACK, [360, 230, 30, 60], 0)
    # Kirby's left pupil
    pygame.draw.ellipse(screen, WHITE, [303, 232, 25, 40], 0)
    # Kirby's right pupil
    pygame.draw.ellipse(screen, WHITE, [363, 232, 25, 40], 0)

    # Kirby's left blush
    pygame.draw.ellipse(screen, RED, [390, 280, 35, 20], 0)
    # Kirby's right blush
    pygame.draw.ellipse(screen, RED, [265, 280, 35, 20], 0)

    # Kirby's mouth
    pygame.draw.polygon(screen, DARK_RED, [[325, 300], [350, 330], [365, 300]], 0)
    pygame.draw.polygon(screen, WARM_RED, [[333, 310], [350, 330], [360, 310]], 0)

    # pygame.draw.arc(screen, GREEN, [100,100,250,200],  PI/2,     PI, 2)
    # pygame.draw.arc(screen, BLACK, [100,100,250,200],     0,   PI/2, 2)
    # pygame.draw.arc(screen, RED,   [100,100,250,200],3*PI/2,   2*PI, 2)
    # pygame.draw.arc(screen, BLUE,  [100,100,250,200],    PI, 3*PI/2, 2)
    
    #pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200], [300, 100]], 5)

    # star
    pygame.draw.polygon(screen, YELLOW, [[100, 100], [140, 200], [220, 200], [150, 250], [180, 330], [100, 280], [20, 330], [50, 250], [-20, 200], [60, 200]], 0)

    # poyo.
    font = pygame.font.SysFont('Comic Sans MS', 25, True, False)
    text = font.render("poyo.", True, BLACK)
    screen.blit(text, [500, 250])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
