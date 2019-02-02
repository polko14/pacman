import pygame
from pygame.locals import *
import os
import tkinter as tk
import random
from math import ceil, floor


def game(file):
    def save(*args):
        with open(os.getcwd()+"\Maps\%s.txt" % file, "r") as f:
            w = f.readlines()[0].split(";")
        names = w[-2].replace(" ", "").replace("'", "")[1:-1].split(",")
        scores = w[-1].replace(" ", "").replace("'", "")[1:-1].split(",")
        scores = [int(scores[i]) for i in range(len(scores))]
        for i in range(len(scores)):
            if SCORE > scores[i]:
                names.insert(i, nick.get())
                names = names[:-1]
                scores.insert(i, SCORE)
                scores = scores[:-1]
                break
        scores = [str(scores[i]) for i in range(len(scores))]
        with open(os.getcwd()+"\Maps\%s.txt" % file, "w") as f:
            f.write(w[0]+";"+w[1]+";"+w[2]+";"+str(names)+";"+str(scores))
        top.destroy()

    class Wall(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = s_wall
            self.rect = self.image.get_rect()
            self.rect.center = (x+RES/2, y+RES/2)

    class Ghost(pygame.sprite.Sprite):
        def __init__(self, x, y, s_image):
            pygame.sprite.Sprite.__init__(self)
            self.image = s_image
            self.rect = self.image.get_rect()
            self.rect.center = (x+RES/2, y+RES/2)
            self.xvel = 0
            self.yvel = 0

        def update(self):
            if self.rect.right % RES == 0 and self.rect.bottom % RES == 0:
                d = random.randint(0, 3)
                if d == 0:
                    self.xvel = 2
                    self.yvel = 0
                    if self.rect.right+self.xvel > SIZE[0]-RES:
                        self.xvel *= -1
                if d == 1:
                    self.xvel = -2
                    self.yvel = 0
                    if self.rect.left+self.xvel < RES:
                        self.xvel *= -1
                if d == 2:
                    self.xvel = 0
                    self.yvel = 2
                    if self.rect.bottom+self.yvel > SIZE[0]-3*RES:
                        self.yvel *= -1
                if d == 3:
                    self.xvel = 0
                    self.yvel = -2
                    if self.rect.top+self.yvel < RES:
                        self.yvel *= -1
            self.rect.centerx += self.xvel
            self.rect.centery += self.yvel
            self.rect.move_ip((self.xvel, self.yvel))

    class Pacman(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.sprites = s_pacman
            self.image = self.sprites[2]
            self.rect = self.image.get_rect()
            self.rect.center = (x+RES/2, y+RES/2)
            self.xvel = 0
            self.yvel = 0

        def update(self):
            self.rect.centerx += self.xvel
            self.rect.centery += self.yvel
            self.rect.move_ip((self.xvel, self.yvel))

    class Point(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = s_point
            self.rect = self.image.get_rect()
            self.rect.center = (x+RES/2, y+RES/2)

    class Special(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = s_special
            self.rect = self.image.get_rect()
            self.rect.center = (x+RES/2, y+RES/2)

    class Heart(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = s_heart
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    class ScoreBoard(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.score = 0
            self.text = "Score: %d" % self.score
            self.font = pygame.font.Font("freesansbold.ttf", 32)
            self.image = self.font.render(self.text, 1, WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (self.rect.size[0]/2, SIZE[1]-16)

        def update(self):
            self.text = "Score: %d" % self.score
            self.image = self.font.render(self.text, 1, WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (self.rect.size[0]/2, SIZE[1]-16)
    with open(os.getcwd()+"\Maps\%s.txt" % file, "r") as f:
        w = f.readlines()[0].split(";")[:3]
    ROWS = int(w[0])
    COLS = int(w[1])
    MAP = w[2][1:-1].replace(' ', '').split(',')
    RES = 16
    ACTIVE = True
    SIZE = (COLS*RES, (ROWS+2)*RES)
    EATING = 0
    EATING_TIME = 0
    LIVES = 3
    SCORE = 0
    WHITE = (255, 255, 255)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    bg = pygame.Surface(SIZE)
    bg.fill((0, 0, 0))
    pygame.display.set_caption("PacMan- Game")
    fullPath = os.getcwd()+r"Graphics"
    sd_point = pygame.mixer.Sound(os.getcwd()+r"\Sounds\point.wav")
    sd_ghost = pygame.mixer.Sound(os.getcwd()+r"\Sounds\ghost.wav")
    sd_move = pygame.mixer.Sound(os.getcwd()+r"\Sounds\move.wav")
    s_wall = pygame.image.load(os.getcwd()+r"\Graphics\wall.gif")
    s_point = pygame.image.load(os.getcwd()+r"\Graphics\point.gif")
    s_special = pygame.image.load(os.getcwd()+r"\Graphics\special.gif")
    s_blinky = pygame.image.load(os.getcwd()+r"\Graphics\blinky.gif")
    s_pinky = pygame.image.load(os.getcwd()+r"\Graphics\pinky.gif")
    s_inky = pygame.image.load(os.getcwd()+r"\Graphics\inky.gif")
    s_clyde = pygame.image.load(os.getcwd()+r"\Graphics\clyde.gif")
    s_pacman = ([pygame.image.load(os.getcwd()+f"\Graphics\{f}")
                 for f in os.listdir(os.getcwd()+r"\Graphics") if
                 f[0:3] == "pac"])
    s_sup_pacman = ([pygame.image.load(os.getcwd()+f"\Graphics\{f}")
                     for f in os.listdir(os.getcwd()+r"\Graphics") if
                     f[0:3] == "sup"])
    s_heart = pygame.image.load(os.getcwd()+r"\Graphics\heart.gif")
    walls = pygame.sprite.RenderClear()
    points = pygame.sprite.RenderClear()
    ghosts = pygame.sprite.RenderClear()
    player_sprite = pygame.sprite.RenderClear()
    specials = pygame.sprite.RenderClear()
    hearts = pygame.sprite.RenderClear()
    hearts.add(Heart(SIZE[0]-40, SIZE[1]-8))
    hearts.add(Heart(SIZE[0]-24, SIZE[1]-8))
    hearts.add(Heart(SIZE[0]-8, SIZE[1]-8))
    scoreboard = pygame.sprite.RenderClear()
    scoreboard.add(ScoreBoard())
    scoreboard.draw(screen)
    pygame.display.flip()
    for row in range(ROWS):
        for col in range(COLS):
            if MAP[col+COLS*row] == '1':
                walls.add(Wall(col*16, row*16))
            elif MAP[col+COLS*row] == '2':
                points.add(Point(col*16, row*16))
            elif MAP[col+COLS*row] == '3':
                specials.add(Special(col*16, row*16))
            elif MAP[col+COLS*row] == '4':
                blinky = Ghost(col*16, row*16, s_blinky)
                ghosts.add(blinky)
            elif MAP[col+COLS*row] == '5':
                pinky = Ghost(col*16, row*16, s_pinky)
                ghosts.add(pinky)
            elif MAP[col+COLS*row] == '6':
                inky = Ghost(col*16, row*16, s_inky)
                ghosts.add(inky)
            elif MAP[col+COLS*row] == '7':
                clyde = Ghost(col*16, row*16, s_clyde)
                ghosts.add(clyde)
            elif MAP[col+COLS*row] == '8':
                player = Pacman(col*16, row*16)
                player_sprite.add(player)
                p_pos = (col*16, row*16)
    while ACTIVE:
        clock.tick(16)
        if player.rect.right % RES == 0 and player.rect.top % RES == 0:
            for event in pygame.event.get():
                if event.type == QUIT:
                    ACTIVE = False
                    return 1
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        player.image = player.sprites[1]
                        player.xvel = -2
                        player.yvel = 0
                    elif event.key == K_RIGHT:
                        player.image = player.sprites[2]
                        player.xvel = 2
                        player.yvel = 0
                    elif event.key == K_UP:
                        player.image = player.sprites[3]
                        player.yvel = -2
                        player.xvel = 0
                    elif event.key == K_DOWN:
                        player.image = player.sprites[0]
                        player.yvel = 2
                        player.xvel = 0
                elif event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        player.xvel = 0
                    elif event.key == K_DOWN or event.key == K_UP:
                        player.yvel = 0
        if(player.xvel != 0 or player.yvel != 0):
            sd_move.play()
        blinky.update()
        pinky.update()
        inky.update()
        clyde.update()
        player.update()
        if EATING_TIME > 0 and EATING_TIME < 16:
            if EATING_TIME % 2 == 0:
                player.sprites = s_sup_pacman
                player.image = s_sup_pacman[s_pacman.index(player.image)]
            else:
                player.sprites = s_pacman
                player.image = s_pacman[s_sup_pacman.index(player.image)]
        pygame.display.update()
        for hit in pygame.sprite.groupcollide(player_sprite, points, 0, 1):
            sd_point.play()
            SCORE += 100
            scoreboard.sprites()[0].score += 100
            scoreboard.update()
            scoreboard.clear(screen, bg)
            scoreboard.draw(screen)
            if len(points) == 0:
                ACTIVE = False
            pygame.display.flip()
        for hit in pygame.sprite.groupcollide(player_sprite, specials, 0, 1):
            sd_point.play()
            pygame.display.flip()
            SCORE += 200
            scoreboard.sprites()[0].score += 200
            scoreboard.update()
            scoreboard.clear(screen, bg)
            scoreboard.draw(screen)
            EATING = 1
            player.sprites = s_sup_pacman
            if player.image in s_pacman:
                player.image = s_sup_pacman[s_pacman.index(player.image)]
            EATING_TIME += random.randint(80, 160)
        if not EATING:
            for hit in pygame.sprite.groupcollide(player_sprite, ghosts, 1, 0):
                LIVES -= 1
                hearts.remove(hearts.sprites()[LIVES])
                if LIVES <= 0:
                    ACTIVE = False
                else:
                    player = Pacman(p_pos[0], p_pos[1])
                    player_sprite.add(player)
                pygame.display.flip()
        else:
            EATING_TIME -= 1
            for hit in pygame.sprite.groupcollide(player_sprite, ghosts, 0, 1):
                sd_ghost.play()
                SCORE += 400
                scoreboard.sprites()[0].score += 400
                scoreboard.update()
                scoreboard.clear(screen, bg)
                scoreboard.draw(screen)
                pygame.display.flip()
            if EATING_TIME <= 0:
                player.sprites = s_pacman
                try:
                    player.image = s_pacman[s_sup_pacman.index(player.image)]
                except:
                    pass
                EATING = 0
                EATING_TIME = 0
        for hit in pygame.sprite.groupcollide(player_sprite, walls, 0, 0):
            player.xvel = 0
            player.yvel = 0
            if player.rect.right % RES > RES/2:
                player.rect.right += (RES-player.rect.right % RES)
            elif (player.rect.right % RES <= RES/2 and
                  player.rect.right % RES > 0):
                player.rect.right -= player.rect.right % RES
            if player.rect.top % RES > RES/2:
                player.rect.top += (RES-player.rect.top % RES)
            elif player.rect.top % RES <= RES/2 and player.rect.top % RES > 0:
                player.rect.top -= player.rect.top % RES
        walls.clear(screen, bg)
        points.clear(screen, bg)
        specials.clear(screen, bg)
        ghosts.clear(screen, bg)
        player_sprite.clear(screen, bg)
        hearts.clear(screen, bg)
        walls.draw(screen)
        points.draw(screen)
        specials.draw(screen)
        ghosts.draw(screen)
        player_sprite.draw(screen)
        hearts.draw(screen)
    pygame.quit()
    top = tk.Tk()
    top.title("Save results")
    frame = tk.Frame(top)
    frame.grid(column=0, row=0)
    nick = tk.StringVar(frame)
    nick.set("Player")
    l_score = tk.Label(frame, text="Your score %s" % (SCORE))
    l_score.grid(column=1, row=1)
    l_nick = tk.Label(frame, text="Player name: ")
    l_nick.grid(column=1, row=2)
    e_nick = tk.Entry(frame, textvariable=nick)
    e_nick.grid(column=2, row=2)
    b_save = tk.Button(frame, text="Save", command=save)
    b_save.grid(column=2, row=3)
    top.mainloop()
    return 1


if __name__ == "__main__":
    game("level1")
