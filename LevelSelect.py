import pygame
from pygame.locals import *
from Ranking import *
from Game import *
from TextObjects import *
import os

def level_select(n):
    SIZE=(600,600)
    BLACK=(0,0,0)
    WHITE=(255,255,255)
    YELLOW=(255,225,0)
    RED=(255,0,0)
    B_WH=250
    B_HT=50
    pygame.init()
    smallText = pygame.font.Font("freesansbold.ttf",20)
    screen=pygame.display.set_mode(SIZE)
    pygame.display.set_caption("PacMan")
    clock=pygame.time.Clock()
    ACTIVE=True
    fullPath=os.getcwd()+"\Maps"
    files = [f[0:-4] for f in os.listdir(fullPath) if (os.path.isfile(os.path.join(fullPath, f)) and f[-4:]==".txt")]
    while(ACTIVE):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==QUIT:
                ACTIVE=False
        
        screen.fill(BLACK)
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("SELECT LEVEL", largeText, WHITE)
        TextRect.center = (SIZE[0]/2,SIZE[1]/8)
        screen.blit(TextSurf, TextRect)
        pygame.draw.rect(screen,RED,(SIZE[1]/2-B_WH/2,500 + B_HT/2,B_WH,B_HT))
        textSurf, textRect = text_objects('BACK', smallText, WHITE)
        textRect.center = ( SIZE[1]/2,500 + B_HT)
        screen.blit(textSurf, textRect)
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        if clicked[2]:
            if SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and 500+3*B_HT/2 > mouse[1] > 500-B_HT/2:
                ACTIVE=False
        if len(files)<=10:
            TextSurf=[0]*len(files)
            TextRect=[0]*len(files)
            for i in range(len(files)):
                TextSurf[i], TextRect[i] = text_objects("%s"%(files[i]), smallText, WHITE)
                TextRect[i].center = (SIZE[0]/2,SIZE[1]/8+30+(2*i+1)*20)
                screen.blit(TextSurf[i], TextRect[i])
            if pygame.mouse.get_pressed()[2]:
                mouse=pygame.mouse.get_pos()
                for i in range(len(files)):
                    if (SIZE[0]/2+TextRect[i].size[0]>mouse[0]>SIZE[0]/2-TextRect[i].size[0] 
                        and SIZE[1]/8+30+(2*i+1)*20+10>mouse[1]>SIZE[1]/8+30+(2*i+1)*20-10):
                        ACTIVE=False
                        pygame.quit()
                        if n==1:
                            return (2,files[i])
                        elif n==2:
                            return 4,files[i]
        elif len(files)>10 and len(files)<=20:
            TextSurf=[0]*len(files)
            TextRect=[0]*len(files)
            for i in range(int((len(files)+1)/2)):
                TextSurf[i], TextRect[i] = text_objects("%s"%(files[i]), smallText, WHITE)
                TextRect[i].center = (SIZE[0]/4,SIZE[1]/8+30+(2*i+1)*20)
                screen.blit(TextSurf[i], TextRect[i])
            for i in range(int(len(files)/2+1),len(files)):
                TextSurf[i], TextRect[i] = text_objects("%s"%(files[i]), smallText, WHITE)
                TextRect[i].center = (SIZE[0]/4*3,SIZE[1]/8+30+(2*(i-(len(files)+1)/2)+1)*20)
                screen.blit(TextSurf[i], TextRect[i])
            if pygame.mouse.get_pressed()[2]:
                mouse=pygame.mouse.get_pos()
                for i in range(len(files)):
                    if (SIZE[0]/4+TextRect[i].size[0]>mouse[0]>SIZE[0]/4-TextRect[i].size[0] 
                        and SIZE[1]/8+30+(2*i+1)*20+10>mouse[1]>SIZE[1]/8+30+(2*i+1)*20-10):
                        ACTIVE=False
                        pygame.quit()
                        if n==1:
                            return 2,files[i]
                        else:
                            return 4,files[i]
                for i in range(int(len(files)/2+1),len(files)):
                    if (SIZE[0]/4*3+TextRect[i].size[0]>mouse[0]>SIZE[0]/4*3-TextRect[i].size[0] 
                        and SIZE[1]/8+30+(2*(i-(len(files)+1)/2)+1)*20+10>mouse[1]
                        and mouse[1]>SIZE[1]/8+30+(2*(i-(len(files)+1)/2)+1)*20-10):
                        ACTIVE=False
                        pygame.quit()
                        if n==1:
                            return 2,files[i]
                        else:
                            return 4,files[i]
        else:
            TextSurf, TextRect = text_objects("To many levels in /Maps folder.",
                                             smallText, WHITE)
            TextRect.center = (SIZE[0]/2,SIZE[1]/5)
            screen.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("Maximum amount is 20.",
                                             smallText, WHITE)
            TextRect.center = (SIZE[0]/2,SIZE[1]/5+30)
            screen.blit(TextSurf, TextRect)
        try:
            pygame.display.update()
        except:
            pass
    pygame.quit()
    return 0,""