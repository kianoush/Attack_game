
import pygame
import os
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard
from towers.archerTower import ArcherTowerLong, ArcherTowerShort
from towers.supportTower import DamageTower, RangeTower
from menu.menu import VerticalMenu
import time
import random
pygame.font.init()


lives_img = pygame.image.load(os.path.join("game_assets/", "heart.png"))
star_img = pygame.image.load(os.path.join("game_assets/", "star.png"))
side_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "side.png")),(60,280))

buy_archer = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "buy_archer.png")),(50,50))
buy_archer1 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "buy_archer1.png")),(50,50))
buy_damage = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "buy_damage.png")),(50,50))
buy_range = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "buy_range.png")),(50,50))


class Game:
    def __init__(self):
        self.width = 1350
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.attack_towers = [ArcherTowerLong(200, 470), ArcherTowerLong(740, 300), ArcherTowerShort(927, 620)]
        self.support_towers = [DamageTower(280, 470)]

        self.lives = 10
        self.money = 2000
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.clicks = [] #remove
        self.life_font = pygame.font.SysFont("comicsans", 45)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width - side_img.get_width() + 30, 380, side_img)
        self.menu.add_btn(buy_archer, "buy_archer", 500)
        self.menu.add_btn(buy_archer1, "buy_archer_1", 750)
        self.menu.add_btn(buy_damage, "buy_damage", 1000)
        self.menu.add_btn(buy_range, "buy_range", 1000)



    def run(self):

        run = True
        clock = pygame.time.Clock()
        while run:
            if time.time() - self.timer >= random.randrange(1,5)/2:
                self.timer = time.time()
                self.enemys.append(random.choice([Club(), Scorpion(), Wizard()]))

            #pygame.time.delay(500)
            clock.tick(20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # look if you click on attack tower
                    btn_clicked = None
                    if self.selected_tower:
                        btn_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                        if btn_clicked:
                            if btn_clicked == "Upgrade":
                                cost = self.selected_tower.get_upgrade_cost()
                                if self.money >= cost:
                                    self.money -= cost
                                    self.selected_tower.upgrade()

                    if not(btn_clicked):
                        for tw in self.attack_towers:
                            if tw.click(pos[0], pos[1]):
                                tw.selected = True
                                self.selected_tower = tw
                            else:
                                tw.selected = False

                        # look if you clicked on support towers
                        for tw in self.support_towers:
                            if tw.click(pos[0], pos[1]):
                                tw.selected = True
                                self.selected_tower = tw
                            else:
                                tw.selected = False

            # loop throuth enemies
            to_del = []
            for en in self.enemys:
                if en.x > 1260:
                    to_del.append(en)

            # delete all enemies off screen
            for d in to_del:
                self.lives -= 1
                self.enemys.remove(d)

            # loop through attack towers
            for tw in self.attack_towers:
                self.money += tw.attack(self.enemys)

            # loop through support towers
            for tw in self.support_towers:
                tw.support(self.attack_towers)

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

        # draw attack_towers
        for tw in self.attack_towers:
            tw.draw(self.win)

        # draw support_towers
        for tw in self.support_towers:
            tw.draw(self.win)

        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        # draw side menu
        self.menu.draw(self.win)


        #draw lives
        text = self.life_font.render(str(self.lives), 1, (255,255,255))
        life = pygame.transform.scale(lives_img,(35,35))
        start_x = self.width - life.get_width() - 10
        self.win.blit(text, (start_x - text.get_width() - 1, 13))
        self.win.blit(life, (start_x, 10))

        # draw money
        text = self.life_font.render(str(self.money), 1, (255,255,255))
        money = pygame.transform.scale(star_img,(35,35))
        start_x = self.width - life.get_width() - 10
        self.win.blit(text, (start_x - text.get_width() - 1, 70))
        self.win.blit(money, (start_x, 63))



        pygame.display.update()

    def draw_menu(self):
        pass

g = Game()
g.run()