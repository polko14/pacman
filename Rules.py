import pygame
from pygame.locals import *

def rules():
    def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
    pygame.init()
    largeText = pygame.font.Font('freesansbold.ttf',80)
    smallText = pygame.font.Font("freesansbold.ttf",20)
    smallTexts=["Player's task is to collect points-",
                "small dots on the map- and to avoid",
                "dangerous ghosts. Picking up the special",
                "point(big dots) changes your appearance",
                "and allows you to 'eat' enemies for additonal",
                "score. The effect duration is random",
                "between 10-15 seconds.",
                "Use arrow keys to move."]
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
        textSurf2, textRect2 = text_objects('GAME RULES', largeText, YELLOW)
        textRect2.center = ( SIZE[0]/2,SIZE[1]/6 )
        screen.blit(textSurf2, textRect2)
        for i in range(len(smallTexts)):
            textSurf, textRect = text_objects(smallTexts[i], smallText, WHITE)
            textRect.center = ( SIZE[1]/2,SIZE[1]/6 + 80+ i*30 )
            screen.blit(textSurf, textRect)
        pygame.draw.rect(screen,RED,(SIZE[1]/2-B_WH/2,450 + B_HT/2,B_WH,B_HT))
        textSurf, textRect = text_objects('BACK', smallText, WHITE)
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
if __name__=="__main__":
    rules()

