import pygame
from pygame.locals import *
from TextObjects import *


def rules():
    smallTexts = ["Player's task is to collect points-",
                  "small dots on the map- and to avoid",
                  "dangerous ghosts. Picking up the special",
                  "point(big dots) changes your appearance",
                  "and allows you to 'eat' enemies for additonal",
                  "score. The effect duration is random",
                  "between 10-15 seconds.",
                  "Use arrow keys to move."]
    SIZE = (600, 600)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 225, 0)
    RED = (255, 0, 0)
    B_WH = 250
    B_HT = 50
    ACTIVE = True
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("PacMan- Rules")
    clock = pygame.time.Clock()
    pygame.draw.rect(screen, RED, (SIZE[1]/2-B_WH/2, 450 + B_HT/2, B_WH, B_HT))
    draw_texts(screen, 'RULES', (SIZE[0]/2, SIZE[1]/6), 80, YELLOW)
    draw_texts(screen, smallTexts,
               (SIZE[1]/2, SIZE[1]/6+80), 20, WHITE, spacing=30)
    draw_texts(screen, 'BACK', (SIZE[1]/2, 450 + B_HT), 20, WHITE)
    pygame.display.update()
    while ACTIVE:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                ACTIVE = False
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()
            if (SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and
                    450+3*B_HT/2 > mouse[1] > 450-B_HT/2):
                ACTIVE = False
    return 0


if __name__ == "__main__":
    pygame.init()
    rules()
    pygame.quit()
