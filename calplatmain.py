import pygame as pg
import random
import sys
from calsettings import *
from calsprites import *



class Game:


    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
    

    

    def new(self):
        # start a new game
        self.score = 2000
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.pplatform = pg.sprite.Group() 
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
            self.pplatform.add(p)
        self.run()


    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
  


    def check_score(self):
        if self.score <= 0:
            self.screen.fill(BLACK)
            self.draw_text("Good Job!", 44, WHITE, WIDTH / 2, HEIGHT / 4)
            self.draw_text("You have eaten the perfect amount of calories for a healthy day.", 22, BLUE, WIDTH / 2, HEIGHT / 2)
            self.score = 2000
            pg.display.flip()
            waiting = True
            while waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        waiting = False
                        self.running = False
                    if event.type == pg.KEYUP:
                        waiting = False
            pg.time.wait(100000000)              
            
    def update(self):
        # Game Loop - Update
       # print("In update", self.score)
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                

        # if player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()


        # Die!
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
            if len(self.platforms) == 0:
                self.playing = False
            
                   
        #print("In update", self.score)

        
            
        # spawn new platforms to keep same average number
        while len(self.platforms) < 8:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30),
                         width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)
            
    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    cal = self.player.jump()
                    print ("subtracting", self.score, cal)
                    self.score = self.score - cal;
                    self.check_score() 
                if event.key == pg.K_w:
                    cal = self.player.jump()
                    print ("subtracting", self.score, cal)
                    self.score = self.score - cal;
                    self.check_score() 
                if event.key == pg.K_SPACE:
                    cal = self.player.jump()
                    print ("subtracting", self.score, cal)
                    self.score = self.score - cal;
                    self.check_score() 
                if event.key == pg.K_ESCAPE:
                    self.show_escape_screen()
                    pg.time.wait(100000000)
        if self.score > 2000:
            self.score = 2000

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK) 
        self.all_sprites.draw(self.screen)
        y = str(self.score) + str(" Calories Remaining")
        self.draw_text(y, 22, WHITE, WIDTH / 2, 15)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BLACK)
        self.draw_text(TITLE, 62, WHITE, WIDTH / 2, 15)
        self.draw_text("Red stands for fruits. You ate 75 nutritional calories.", 20, RED, WIDTH / 2, HEIGHT *2/11)
        self.draw_text("Orange stands for protien. You ate 600 nutritional calories", 20, ORANGE, WIDTH / 2, HEIGHT *3/11)
        self.draw_text("Yellow stands for healthy entrees. You ate 300 nutritional calories.", 20, YELLOW, WIDTH / 2, HEIGHT *4/11)
        self.draw_text("Green stands for vegetables. You ate 150 nutritional calories.", 20, GREEN, WIDTH / 2, HEIGHT *5/11)
        self.draw_text("Lightblue stands for dairy. You ate 250 nutritional calories.", 20, LIGHTBLUE, WIDTH / 2, HEIGHT *6/11)
        self.draw_text("Darkblue stands for whole grains. You ate 130 nutritional calories.", 20, DARKBLUE, WIDTH / 2, HEIGHT *7/11)
        self.draw_text("Purple stands for unhealthy entrees. You ate 600 unhealthy calories.", 20, PURPLE, WIDTH / 2, HEIGHT *8/11)
        self.draw_text("Pink stands for candy and deserts. You ate 300 unhealthy calories.", 20, PINK, WIDTH / 2, HEIGHT *9/11)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER!", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Oh no! You don't have enough calories to live a healthy day.", 22, YELLOW, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to play again.", 22, LIGHTBLUE, WIDTH / 2, HEIGHT * 3/4)
        pg.display.flip()
        self.wait_for_key()

    def show_escape_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER!", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Oh no! You don't have enough calories to live a healthy day.", 22, YELLOW, WIDTH / 2, HEIGHT / 2)
        self.draw_text("To play again, exit this screen and reopen the game to play", 22, LIGHTBLUE, WIDTH / 2, HEIGHT * 3/4)
        pg.display.flip()
        self.wait_for_key()


    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()