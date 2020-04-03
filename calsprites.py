import pygame as pg
from settings import *
import random
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        cal = 0
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
            cal = hits[0].cal
            print("In jump", cal)
        return cal
            

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        col = random.randint(1,8)
        self.cal = 0
        if col == 1:
            self.image.fill(GREEN)
            self.cal = 150

        if col == 2:
            self.image.fill(YELLOW)
            self.cal = 300
            
        if col == 3:
            self.image.fill(RED)
            self.cal = 75
            
        if col ==4:
            self.image.fill(PURPLE)
            self.cal = -600
            
        if col == 5:
            self.image.fill(PINK)
            self.cal = -300
            
        if col == 6:
            self.image.fill(LIGHTBLUE)
            self.cal = 250

        if col == 7:
            self.image.fill(ORANGE)
            self.cal = 600

        if col == 8:
            self.image.fill(DARKBLUE)
            self.cal = 130
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def counter(self,countg,county,countr,countpu,countpi,countlb):
            self.countg = 0
            self.county = 0
            self.countr = 0
            self.countpu = 0
            self.countpi = 0
            self.countlb = 0
