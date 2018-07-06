import pygame
from pygame.locals import *

def credits():
    #Funkcja wyświetlająca informacje o autorze
    def text_objects(text, font, color):
        #Funkcja tworząca obiekt tekstu
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
    pygame.init()
    #######Deklaracja stałych
    largeText = pygame.font.Font('freesansbold.ttf',80)
    smallText = pygame.font.Font("freesansbold.ttf",30)
    largeTexts=['KOD', 'GRAFIKA', 'MUZYKA']
    smallTexts=['PAWEŁ BOGDAN','PAWEŁ BOGDAN','github.com/greyblue9/']
    SIZE=(600,600)
    BLACK=(0,0,0)
    WHITE=(255,255,255)
    YELLOW=(255,225,0)
    RED=(255,0,0)
    B_WH=250
    B_HT=50
    screen=pygame.display.set_mode(SIZE)
    pygame.display.set_caption("PacMan")
    clock=pygame.time.Clock()
    ACTIVE=True
    while ACTIVE:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==QUIT:
                ACTIVE=False
        screen.fill(BLACK)
        for i in range(3):
            #Pętla drukująca napisy
            textSurf, textRect = text_objects(smallTexts[i], smallText, WHITE)
            textSurf2, textRect2 = text_objects(largeTexts[i], largeText, YELLOW)
            textRect.center = ( SIZE[1]/2,(2*i+0.5)*80 + 2*30 )
            textRect2.center = ( SIZE[1]/2,(2*i+0.5)*80 )
            screen.blit(textSurf, textRect)
            screen.blit(textSurf2, textRect2)
        pygame.draw.rect(screen,RED,(SIZE[1]/2-B_WH/2,450 + B_HT/2,B_WH,B_HT))
        textSurf, textRect = text_objects('COFNIJ', smallText, WHITE)
        textRect.center = ( SIZE[1]/2,450 + B_HT)
        screen.blit(textSurf, textRect)
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        pygame.display.update()
        if clicked[2]:
            if SIZE[1]/2+B_WH/2 > mouse[0] > SIZE[1]/2-B_WH/2 and 450+3*B_HT/2 > mouse[1] > 450-B_HT/2:
                ACTIVE=False

    pygame.quit()
    return 0

