import pygame
from pygame.locals import *
from TextObjects import *
import os


def ranking(file):
    SIZE = (600, 600)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 225, 0)
    RED = (255, 0, 0)
    B_WH = 250
    B_HT = 50
    ACTIVE = True
    with open(os.getcwd()+"\Maps\%s.txt" % file, "r") as f:
        w = f.readlines()[0].split(";")[-2:]
        names = w[0].replace(" ", "").replace("'", "")[1:-1].split(",")
        scores = w[1].replace(" ", "").replace("'", "")[1:-1].split(",")
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("PacMan- Ranking")
    clock = pygame.time.Clock()
    pygame.draw.rect(screen, RED, (SIZE[1]/2-B_WH/2, 500 + B_HT/2, B_WH, B_HT))
    draw_texts(screen, "%s" % (file), (SIZE[0]/2, SIZE[1]/8), 90, WHITE)
    draw_texts(screen, "BACK", (SIZE[1]/2, 500 + B_HT), 20, WHITE)
    draw_texts(screen, names, (SIZE[0]/4, SIZE[1]/8+50), 20, WHITE, spacing=40)
    draw_texts(screen, scores, (SIZE[0]/4*3,
                                SIZE[1]/8+50), 20, WHITE, spacing=40)
    pygame.display.update()
    while ACTIVE:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                ACTIVE = False
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()
            if (SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and
                    500+3*B_HT/2 > mouse[1] > 500-B_HT/2):
                ACTIVE = False
    pygame.quit()
    return 3


if __name__ == "__main__":
    ranking("level1")
