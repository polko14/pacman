import pygame
from pygame.locals import *
from Ranking import *
from Game import *
from TextObjects import *
import os


def level_select(n):
    SIZE = (600, 600)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 225, 0)
    RED = (255, 0, 0)
    B_WH = 250
    B_HT = 50
    L_WH = 100
    ACTIVE = True
    fullPath = os.getcwd()+"\Maps"
    files = [f[0:-4] for f in os.listdir(fullPath) if (
        os.path.isfile(os.path.join(fullPath, f)) and f[-4:] == ".txt")]
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("PacMan- Level Select")
    clock = pygame.time.Clock()
    pygame.draw.rect(screen, RED, (SIZE[1]/2-B_WH/2, 500 + B_HT/2, B_WH, B_HT))
    draw_texts(screen, "SELECT LEVEL", (SIZE[0]/2, SIZE[1]/8), 60, WHITE)
    draw_texts(screen, "BACK", (SIZE[1]/2, 500 + B_HT), 20, WHITE)
    if len(files) == 0:
        draw_texts(screen, "Maps not found create some using map creator",
                   (SIZE[0]/2, SIZE[1]/5), 20, WHITE)
    elif len(files) > 20:
        draw_texts(screen, ["To many levels in /Map directory",
                            "Maximum amount is 20"],
                   (SIZE[0]/2, SIZE[1]/5), 20, WHITE, spacing=30)
    else:
        draw_texts(screen, files[:int((len(files)+1)/2)],
                   (SIZE[0]/4, SIZE[1]/8+50), 20, WHITE, spacing=40)
        draw_texts(screen, files[int((len(files)+1)/2):],
                   (3*SIZE[0]/4, SIZE[1]/8+50), 20, WHITE, spacing=40)
    pygame.display.update()
    while(ACTIVE):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                ACTIVE = False
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()
            if (SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and
                    500+3*B_HT/2 > mouse[1] > 500-B_HT/2):
                ACTIVE = False
            if len(files) <= 20:
                for i in range(int((len(files)+1)/2)):
                    if (SIZE[0]/4+L_WH > mouse[0] > SIZE[0]/4-L_WH and
                            SIZE[1]/8+60+i*40 > mouse[1] > SIZE[1]/8+40+i*40):
                        ACTIVE = False
                        pygame.quit()
                        if n == 1:
                            return 2, files[i]
                        else:
                            return 4, files[i]
                for i in range(int((len(files)+1)/2)):
                    if (3*SIZE[0]/4+L_WH > mouse[0] > 3*SIZE[0]/4-L_WH and
                            SIZE[1]/8+60+i*40 > mouse[1] > SIZE[1]/8+40+i*40):
                        ACTIVE = False
                        pygame.quit()
                        if n == 1:
                            return 2, files[i+int((len(files)+1)/2)]
                        else:
                            return 4, files[i+int((len(files)+1)/2)]
    pygame.quit()
    return 0, ""


if __name__ == "__main__":
    level_select(1)
