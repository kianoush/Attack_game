
import pygame
import os
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard



class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Scorpion(), Club(), Wizard()]
        self.towers = []
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = [] #remove



    def run(self):

        run = True
        clock = pygame.time.Clock()
        while run:
            #pygame.time.delay(500)
            clock.tick(60)
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
                if en.x < -5:
                    to_del.append(en)

            # delete all enemies off screen
            for d in to_del:
                self.enemys.remove(d)

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        for p in self.clicks:# remove
            pygame.draw.circle(self.win, (255,0,0),(p[0], p[1]), 5,0 )# remove


        # draw enemies
        for en in self.enemys:
            en.draw(self.win)
        pygame.display.update()


g = Game()
g.run()