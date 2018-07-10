import pygame
from pygame.locals import *
from TextObjects import *
import os
def ranking(file):
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
    clock=pygame.time.Clock()
    with open(os.getcwd()+"\Maps\%s.txt"%file,"r") as f:
        w=f.readlines()[0].split(";")[-2:]
        names=w[0].replace(" ","").replace("'","")[1:-1].split(",")
        scores=w[1].replace(" ","").replace("'","")[1:-1].split(",")
    while ACTIVE:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==QUIT:
                ACTIVE=False
        largeText = pygame.font.Font('freesansbold.ttf',90)
        smallText = pygame.font.Font("freesansbold.ttf",20)
        TextSurf, TextRect = text_objects("%s"%(file), largeText, WHITE)
        TextRect.center = (SIZE[0]/2,SIZE[1]/8)
        screen.blit(TextSurf, TextRect)
        pygame.draw.rect(screen,RED,(SIZE[1]/2-B_WH/2,500 + B_HT/2,B_WH,B_HT))
        textSurf, textRect = text_objects('BACK', smallText, WHITE)
        textRect.center = ( SIZE[1]/2,500 + B_HT)
        screen.blit(textSurf, textRect)
        TextSurf=[0]*len(names)
        TextRect=[0]*len(names)
        for i in range(len(names)):
            TextSurf[i], TextRect[i] = text_objects("%s"%(names[i]), smallText, WHITE)
            TextRect[i].center = (SIZE[0]/4,SIZE[1]/8+30+(2*i+1)*20)
            screen.blit(TextSurf[i], TextRect[i])
        for i in range(len(scores)):
            TextSurf[i], TextRect[i] = text_objects("%s"%(scores[i]), smallText, WHITE)
            TextRect[i].center = (SIZE[0]/4*3,SIZE[1]/8+30+(2*i+1)*20)
            screen.blit(TextSurf[i], TextRect[i])
        pygame.display.update()
        if pygame.mouse.get_pressed()[2]:
            mouse = pygame.mouse.get_pos()
            if (SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and 500+3*B_HT/2 > mouse[1] > 500-B_HT/2):
                ACTIVE=False
    pygame.quit()
    return 3