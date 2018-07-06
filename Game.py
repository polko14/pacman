import pygame
from pygame.locals import *
import os
import tkinter as tk
import random
from math import ceil,floor
def game(file):
    #Funkcja odpowiadająca za logikę gry
    def zapisz(*args):
        #Zapisywanie wyniku gracza do pliku z mapą
        f=open(os.getcwd()+"\Mapy\%s.txt"%file,"r")
        w=f.readlines()[0].split(";")
        names=w[-2].replace(" ","").replace("'","")[1:-1].split(",")
        scores=w[-1].replace(" ","").replace("'","")[1:-1].split(",")
        f.close()
        scores=[int(scores[i]) for i in range(len(scores))]
        for i in range(len(scores)):
            if SCORE>scores[i]:
                names.insert(i,nick.get())
                names=names[:-1]
                scores.insert(i,SCORE)
                scores=scores[:-1]
                break
        scores=[str(scores[i]) for i in range(len(scores))]
        f=open(os.getcwd()+"\Mapy\%s.txt"%file,"w")
        f.write(w[0]+";"+w[1]+";"+w[2]+";"+str(names)+";"+str(scores))
        f.close()
        top.destroy()
    ###Klasy obiektów występujących w grze
    class sciana(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image=s_sciana
            self.rect = self.image.get_rect()
            self.rect.center = (x+RES/2,y+RES/2)
            #self.d=-1
    class duch(pygame.sprite.Sprite):
        def __init__(self,x,y,s_image):
            pygame.sprite.Sprite.__init__(self)
            self.image= s_image
            self.rect = self.image.get_rect()
            self.rect.center = (x+RES/2,y+RES/2)
            self.xvel=0
            self.yvel=0
        def update(self):
            #Losowy ruch duchów
            if self.rect.right%RES==0 and self.rect.bottom%RES==0:
                d=random.randint(0,3)
                if d==0:
                    self.xvel=2
                    self.yvel=0
                    if self.rect.right+self.xvel>SIZE[0]-RES:
                        self.xvel*=-1
                if d==1:
                    self.xvel=-2
                    self.yvel=0
                    if self.rect.left+self.xvel<RES:
                        self.xvel*=-1
                if d==2:
                    self.xvel=0
                    self.yvel=2
                    if self.rect.bottom+self.yvel>SIZE[0]-RES:
                        self.yvel*=-1
                if d==3:
                    self.xvel=0
                    self.yvel=-2   
                    if self.rect.top+self.yvel<RES:
                        self.yvel*=-1
            self.rect.centerx+=self.xvel
            self.rect.centery+=self.yvel
            self.rect.move_ip((self.xvel,self.yvel))
    class pacman(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image=s_pacman
            self.rect = self.image.get_rect()
            self.rect.center = (x+RES/2,y+RES/2)
            self.xvel=0
            self.yvel=0
        def update(self):
            self.rect.centerx+=self.xvel
            self.rect.centery+=self.yvel
            self.rect.move_ip((self.xvel,self.yvel))


    class punkt(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image=s_punkt
            self.rect = self.image.get_rect()
            self.rect.center = (x+RES/2,y+RES/2)
    class specjal(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image=s_specjal
            self.rect = self.image.get_rect()
            self.rect.center = (x+RES/2,y+RES/2)
    class heart(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image=s_heart
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)
    class ScoreBoard(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.score = 0
            self.text = "Wynik: %d" % self.score
            self.font = pygame.font.Font("freesansbold.ttf",32)
            self.image = self.font.render(self.text,1,WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (self.rect.size[0]/2,SIZE[1]-16)
        def update(self):
            self.text = "Wynik: %d" % self.score
            self.image = self.font.render(self.text,1,WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (self.rect.size[0]/2,SIZE[1]-16)
    #Odczyt danych mapy z plku
    f=open(os.getcwd()+"\Mapy\%s.txt"%file,"r")
    w=f.readlines()[0].split(";")[:3]
    f.close()
    #Stałe
    ROWS=int(w[0])
    COLS=int(w[1])
    MAPA=w[2][1:-1].replace(' ','').split(',')
    RES=16
    ACTIVE=True
    SIZE=(ROWS*RES,(COLS+2)*RES)
    ZJADANIE=0
    CZASZJADANIA=0
    LIVES=3
    SCORE=0
    WHITE=(255,255,255)
    pygame.init()
    clock=pygame.time.Clock()
    screen=pygame.display.set_mode(SIZE)
    bg = pygame.Surface(SIZE)
    bg.fill((0,0,0))
    pygame.display.set_caption("PacMan")
    #Import danych dźwiękowych
    d_punkt = pygame.mixer.Sound(os.getcwd()+r"\Dzwieki\punkt.wav")
    d_duch = pygame.mixer.Sound(os.getcwd()+r"\Dzwieki\duch.wav")
    d_ruch = pygame.mixer.Sound(os.getcwd()+r"\Dzwieki\ruch.wav")
    #Import grafik
    s_sciana = pygame.image.load(os.getcwd()+r"\Grafiki\sciana.gif")
    s_punkt = pygame.image.load(os.getcwd()+r"\Grafiki\punkt.gif")
    s_specjal = pygame.image.load(os.getcwd()+r"\Grafiki\specjal.gif")
    s_blinky = pygame.image.load(os.getcwd()+r"\Grafiki\blinky.gif")
    s_pinky = pygame.image.load(os.getcwd()+r"\Grafiki\pinky.gif")
    s_inky = pygame.image.load(os.getcwd()+r"\Grafiki\inky.gif")
    s_clyde = pygame.image.load(os.getcwd()+r"\Grafiki\clyde.gif")
    s_pacman = pygame.image.load(os.getcwd()+r"\Grafiki\pacman.gif")
    s_heart = pygame.image.load(os.getcwd()+r"\Grafiki\heart.gif")
    #Tworzenie kontenerów na sprite'y
    sciany=pygame.sprite.RenderClear()
    punkty=pygame.sprite.RenderClear()
    duchy=pygame.sprite.RenderClear()
    graczspr=pygame.sprite.RenderClear()
    specjale=pygame.sprite.RenderClear()
    hearts=pygame.sprite.RenderClear()
    #Tworzenie obiektów punktów życia
    hearts.add(heart(SIZE[0]-40,SIZE[1]-8))
    hearts.add(heart(SIZE[0]-24,SIZE[1]-8))
    hearts.add(heart(SIZE[0]-8,SIZE[1]-8))
    #Tworzenie obiektu tablicy wyników
    scoreboard = pygame.sprite.RenderClear()
    scoreboard.add(ScoreBoard())
    scoreboard.draw(screen)
    pygame.display.flip()
    for i in range(ROWS):
        #Tworzenie obiektów gry z pliku txt mapy
        for j in range(COLS):
            if MAPA[i+j*ROWS]=='1':
                sciany.add(sciana(i*16,j*16))
            elif MAPA[i+j*ROWS]=='2':
                punkty.add(punkt(i*16,j*16))
            elif MAPA[i+j*ROWS]=='3':
                specjale.add(specjal(i*16,j*16))
            elif MAPA[i+j*ROWS]=='4':
                blinky=duch(i*16,j*16,s_blinky)
                duchy.add(blinky)
            elif MAPA[i+j*ROWS]=='5':
                pinky=duch(i*16,j*16,s_pinky)
                duchy.add(pinky)
            elif MAPA[i+j*ROWS]=='6':
                inky=duch(i*16,j*16,s_inky)
                duchy.add(inky)
            elif MAPA[i+j*ROWS]=='7':
                clyde=duch(i*16,j*16,s_clyde)
                duchy.add(clyde)
            elif MAPA[i+j*ROWS]=='8':
                gracz=pacman(i*16,j*16)
                graczspr.add(gracz)
                p_pos=(i*16,j*16)
    while ACTIVE:
        clock.tick(16)
        #Obsługa akcji użytkownika
        if gracz.rect.right%RES==0 and gracz.rect.top%RES==0:
            for event in pygame.event.get():
                if event.type==QUIT:
                    ACTIVE=False
                    return 1
                elif event.type==KEYDOWN:
                    if event.key == K_LEFT:
                        gracz.xvel = -2
                        gracz.yvel=0
                    elif event.key == K_RIGHT:
                        gracz.xvel = 2
                        gracz.yvel=0
                    elif event.key == K_UP:
                        gracz.yvel = -2
                        gracz.xvel=0
                    elif event.key == K_DOWN:
                        gracz.yvel = 2
                        gracz.xvel=0
                elif event.type==KEYUP:
                    if event.key==K_LEFT or event.key==K_RIGHT:
                        gracz.xvel=0
                    elif event.key==K_DOWN or event.key==K_UP:
                        gracz.yvel=0
        #Odtwarzanie dźwięków i aktualizacja pozycji ruchomych obiektów
        if(gracz.xvel!=0 or gracz.yvel!=0):
            d_ruch.play()
        blinky.update()
        pinky.update()
        inky.update()
        clyde.update()
        gracz.update()
        pygame.display.update()

        #Sprawdzanie kolizji
        for hit in pygame.sprite.groupcollide(graczspr,punkty,0,1):
            #Gracz z punktem
            d_punkt.play()
            SCORE+=100
            scoreboard.sprites()[0].score +=100
            scoreboard.update()
            scoreboard.clear(screen, bg)
            scoreboard.draw(screen)
            if len(punkty)==0:
                ACTIVE=False
            pygame.display.flip()
        for hit in pygame.sprite.groupcollide(graczspr,specjale,0,1):
            #Gracz z punktem specjalnym
            d_punkt.play()
            pygame.display.flip()
            SCORE+=200
            scoreboard.sprites()[0].score +=200
            scoreboard.update()
            scoreboard.clear(screen, bg)
            scoreboard.draw(screen)
            ZJADANIE=1
            CZASZJADANIA=random.randint(160,240)

        if not ZJADANIE:
            #Supermoc nieaktywna
            for hit in pygame.sprite.groupcollide(graczspr,duchy,1,0):
                #Zderzenie gracza z przeciwnikiem
                LIVES-=1
                hearts.remove(hearts.sprites()[LIVES])
                if LIVES<=0:
                    ACTIVE=False
                else:
                    gracz=pacman(p_pos[0],p_pos[1])
                    graczspr.add(gracz)
                pygame.display.flip()
        else:
            #Supermoc aktywna
            for hit in pygame.sprite.groupcollide(graczspr,duchy,0,1):
                #Zderzenie gracza z przeciwnikiem
                d_duch.play()
                SCORE+=400
                scoreboard.sprites()[0].score +=400
                scoreboard.update()
                scoreboard.clear(screen, bg)
                scoreboard.draw(screen)
                pygame.display.flip()
            CZASZJADANIA-=1#Zmniejszenie czasu supermocy
            if CZASZJADANIA<=0:
                ZJADANIE=0#Wyłącznie supermocy
        for hit in pygame.sprite.groupcollide(graczspr,sciany,0,0):
            #Gracz ze ścianą
            gracz.xvel=0
            gracz.yvel=0
            if gracz.rect.right%RES>RES/2:
                gracz.rect.right+=(RES-gracz.rect.right%RES)
            elif gracz.rect.right%RES<=RES/2 and gracz.rect.right%RES>0:
                gracz.rect.right-=gracz.rect.right%RES
            if gracz.rect.top%RES>RES/2:
                gracz.rect.top+=(RES-gracz.rect.top%RES)
            elif gracz.rect.top%RES<=RES/2 and gracz.rect.top%RES>0:
                gracz.rect.top-=gracz.rect.top%RES
        #Czyszczenie planszy
        sciany.clear(screen,bg)
        punkty.clear(screen,bg)
        specjale.clear(screen,bg)
        duchy.clear(screen,bg)
        graczspr.clear(screen,bg) 
        hearts.clear(screen,bg) 
        #Rysowanie sprite'ów
        sciany.draw(screen)
        punkty.draw(screen)
        specjale.draw(screen)
        duchy.draw(screen)
        graczspr.draw(screen) 
        hearts.draw(screen) 

    pygame.quit()
    #GUI zapisu wyniku
    top=tk.Tk() 
    top.title("Zapisz wynik")
    ramka=tk.Frame(top)
    ramka.grid(column=0,row=0)
    nick=tk.StringVar(ramka)
    nick.set("Gracz")
    l_score=tk.Label(ramka,text = "Twój wynik to %s"%(SCORE))
    l_score.grid(column=1,row = 1)
    l_nick=tk.Label(ramka,text = "Podaj nazwę gracza: ")
    l_nick.grid(column=1,row = 2)
    e_nick=tk.Entry(ramka,textvariable=nick)
    e_nick.grid(column=2, row = 2)
    b_zapisz=tk.Button(ramka,text="zapisz",command=zapisz)
    b_zapisz.grid(column=2, row =3)
    top.mainloop()
    
    return 1
