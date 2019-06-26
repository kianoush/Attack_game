
import pygame
import os
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard
from towers.archerTower import ArcherTowerLong, ArcherTowerShort
import time
import random
pygame.font.init()


lives_img = pygame.image.load(os.path.join("game_assets/", "heart.png"))
star_img = pygame.image.load(os.path.join("game_assets/", "star.png"))


class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Club()]
        self.towers = [ArcherTowerLong(200,400),ArcherTowerLong(700,300),ArcherTowerShort(900,600)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.clicks = [] #remove
        self.life_font = pygame.font.SysFont("comicsans", 70)



    def run(self):

        run = True
        clock = pygame.time.Clock()
        while run:
            if time.time() - self.timer >= random.randrange(1,5)/2:
                self.timer = time.time()
                self.enemys.append(random.choice([Club(), Scorpion(), Wizard()]))

            #pygame.time.delay(500)
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)# remove
                    print(self.clicks)# remove

            # loop throuth enemies
            to_del = []
            for en in self.enemys:
                if en.x < -15:
                    to_del.append(en)

            # delete all enemies off screen
            for d in to_del:
                self.enemys.remove(d)


            # loop throuth towers
            for tw in self.towers:
                tw.attack(self.enemys)

            # if you lose
            if self.lives <= 0:
                print("You Lose")
                run = False

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        for p in self.clicks: # remove
            pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0) # remove



        # draw towers
        for tw in self.towers:
            tw.draw(self.win)

        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        #draw lives
        text = self.life_font.render(str(self.lives), 1, (0,0,0))

        life = pygame.transform.scale(lives_img,(20,20))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 10))
        self.win.blit(life, (start_x, 10))

        pygame.display.update()


g = Game()
g.run()