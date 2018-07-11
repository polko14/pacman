import pygame
from pygame.locals import *
from TextObjects import *
def menu():
    SIZE=(600,600)
    BLACK=(0,0,0)
    WHITE=(255,255,255)
    YELLOW=(255,225,0)
    RED=(255,0,0)
    B_WH=250
    B_HT=50
    ACTIVE=True
    pygame.init()
    screen=pygame.display.set_mode(SIZE)
    pygame.display.set_caption("PacMan")
    texts=['PLAY', 'SCOREBOARD', 'MAP CREATOR','RULES', 'CLOSE']
    clock=pygame.time.Clock()
    for i in range(0,len(texts)):
        pygame.draw.rect(screen,RED,(SIZE[1]/2-B_WH/2,SIZE[0]/4+(3*i+1)*B_HT/2,B_WH,B_HT))
    draw_texts(screen, "PacMan", (SIZE[0]/2-5,SIZE[1]/6-5), 115, YELLOW)
    draw_texts(screen, "PacMan", (SIZE[0]/2,SIZE[1]/6), 115, WHITE)
    draw_texts(screen, texts, (SIZE[1]/2,SIZE[0]/4+B_HT), 20, WHITE, spacing=3*B_HT/2)
    pygame.display.update()
    while ACTIVE:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==QUIT:
                ACTIVE=False
                pygame.quit()
                return 7
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()
            if SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and SIZE[0]/4+3/2*B_HT > mouse[1] > SIZE[0]/4+B_HT/2:
                ACTIVE=False
                pygame.quit()
                return 1
            elif SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and SIZE[0]/4+6/2*B_HT > mouse[1] > SIZE[0]/4+4*B_HT/2:
                ACTIVE=False
                pygame.quit()
                return 3
            elif SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and SIZE[0]/4+9/2*B_HT > mouse[1] > SIZE[0]/4+7*B_HT/2:
                ACTIVE=False
                pygame.quit()
                return 6
            elif SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and SIZE[0]/4+12/2*B_HT > mouse[1] > SIZE[0]/4+10*B_HT/2:
                ACTIVE=False
                pygame.quit()
                return 8
            elif SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and SIZE[0]/4+15/2*B_HT > mouse[1] > SIZE[0]/4+13*B_HT/2:
                ACTIVE=False
                pygame.quit()
                return 7