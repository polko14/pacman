import pygame
from pygame.locals import *
def menu():
    #Funkcja odpowiadająca za działanie meny gry
    def text_objects(text, font, color):
        #Funkcja tworząca obiekt tekstu
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
    pygame.init()
    #Stałe
    SIZE=(600,600)
    BLACK=(0,0,0)
    WHITE=(255,255,255)
    YELLOW=(255,225,0)
    RED=(255,0,0)
    B_WH=250
    B_HT=50
    ACTIVE=True
    screen=pygame.display.set_mode(SIZE)
    pygame.display.set_caption("PacMan")
    clock=pygame.time.Clock()
    
    while ACTIVE:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==QUIT:
                ACTIVE=False
                pygame.quit()
                return 7
        screen.fill(BLACK)
        #TYTUŁ
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf2, TextRect2 = text_objects("PacMan", largeText, YELLOW)
        TextRect2.center = (SIZE[0]/2-5,SIZE[1]/6-5)
        TextSurf, TextRect = text_objects("PacMan", largeText, WHITE)
        TextRect.center = (SIZE[0]/2,SIZE[1]/6)
        screen.blit(TextSurf2, TextRect2)
        screen.blit(TextSurf, TextRect)
        #PRZYCISKI
        smallText = pygame.font.Font("freesansbold.ttf",20)
        texts=['GRAJ', 'WYNIKI', 'KREATOR MAP','ZASADY GRY', 'O AUTORZE', 'ZAMKNIJ']
        for i in range(0,6):
            pygame.draw.rect(screen,RED,(SIZE[1]/2-B_WH/2,SIZE[0]/4+(3*i+1)*B_HT/2,B_WH,B_HT))
            textSurf, textRect = text_objects(texts[i], smallText, WHITE)
            textRect.center = ( SIZE[1]/2,SIZE[0]/4+(3*i+2)*B_HT/2 )
            screen.blit(textSurf, textRect)
        #OBSŁUGA PRZYCISKÓW
        clicked = pygame.mouse.get_pressed()
        pygame.display.update()
        if clicked[2]:
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
                return 5
            elif SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and SIZE[0]/4+18/2*B_HT > mouse[1] > SIZE[0]/4+16*B_HT/2:
                ACTIVE=False
                pygame.quit()
                return 7