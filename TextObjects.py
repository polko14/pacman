import pygame
def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

def draw_texts(screen, texts, position, fontsize, color, spacing=None, font='freesansbold.ttf'):
    if spacing==None:
        spacing=fontsize
    font = pygame.font.Font(font,fontsize)
    if type(texts)==str:
        texts=[texts]
    for i in range(len(texts)):
        textSurf, textRect = text_objects(texts[i], font, color)
        textRect.center = (position[0],position[1]+i*spacing)
        screen.blit(textSurf, textRect)
