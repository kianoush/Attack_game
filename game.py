
import pygame
import os
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard
from towers.archerTower import ArcherTowerLong, ArcherTowerShort
from towers.supportTower import DamageTower, RangeTower
from menu.menu import VerticalMenu, PlayPauseButton
import time
import random
import math
import numpy as np
import matplotlib.pyplot as plt
pygame.font.init()

path = [(12, 551), (159, 549), (334, 548), (405, 539), (454, 475), (455, 401), (521, 332), (620, 329), (668, 370), (690, 439), (715, 510), (771, 544), (843, 548), (1065, 542), (1269, 542), (1338, 544), (1191, 550)] #  change area (614, 429) ---> [(648, 397), (690, 381), (725, 353), (749, 318), (760, 275), (776, 229), (804, 194), (853, 172), (900, 167), (953, 164), (1007, 162), (1056, 172), (1084, 179), (1109, 194), (1129, 211), (1154, 218), (1185, 218), (1196, 217)]



lives_img = pygame.image.load(os.path.join("game_assets/", "heart.png"))
star_img = pygame.image.load(os.path.join("game_assets/", "star.png"))
side_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "side.png")),(60,280))

buy_archer = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "buy_archer.png")),(50,50))
buy_archer1 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "buy_archer1.png")),(50,50))
buy_damage = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "buy_damage.png")),(50,50))
buy_range = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "buy_range.png")),(50,50))

play_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "button_start.png")),(50,50))
pause_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "button_pause.png")),(50,50))

wave_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/", "wave.png")),(210,65))


attack_tower_names = ["archer", "archer2"]
support_tower_names = ["range", "damage"]

# waves are in form
# frequncy of enemies
# ( #scorpian, #wizards, #clubs)

waves = [
    [20, 0, 0],
    [50, 0, 0],
    [100, 0, 0],
    [0, 20, 0],
    [0, 50, 0],
    [0, 100, 0],
    [20, 100, 0],
    [50, 100, 0],
    [100, 100, 0],
    [20, 0, 100],
    [200, 0, 150],
    [200, 100, 200]
]

class Game:
    def __init__(self):
        self.width = 1350
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.attack_towers = []
        self.support_towers = []
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
        self.moving_object = None
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.pause = True
        self.playPauseButton = PlayPauseButton(play_btn, pause_btn, 10, self.height - 85)
        #self.path = [] red point

    def gen_enemies(self):
        """
        generate the next enemy or enemiest to show
        :return: enemy
        """
        if sum(self.current_wave) == 0:
            if len(self.enemys) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
                self.pause = True
                self.playPauseButton.paused = self.pause
        else:
            wave_enemies = [Scorpion(), Wizard(), Club()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemys.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break


    def run(self):

        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(200)

            if self.pause == False:
                # gen monsters
                if time.time() - self.timer >= random.randrange(1,5)/2:
                    self.timer = time.time()
                    self.gen_enemies()


            pos = pygame.mouse.get_pos()

            # check for moving object
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])

            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if you are moving an object and click
                    # self.path.append(pos)        red point
                    # print(self.path)

                    if self.moving_object:
                        not_allowed = False
                        tower_list = self.attack_towers[:] + self.support_towers[:]
                        for tower in tower_list:
                            if tower.collide(self.moving_object):
                                not_allowed = True

                        if not not_allowed and self.point_to_line(self.moving_object):
                            if self.moving_object.name in attack_tower_names:
                                self.attack_towers.append(self.moving_object)
                            elif self.moving_object.name in support_tower_names:
                                self.support_towers.append(self.moving_object)
                            self.moving_object.moving = False
                            self.moving_object = None


                    else:
                        # check for play or pause
                        if self.playPauseButton.click(pos[0], pos[1]):
                            self.pause = not(self.pause)
                            self.playPauseButton.paused = self.pause

                        # look if you click on side menu
                        side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if side_menu_button:
                            cost = self.menu.get_item_cost(side_menu_button)
                            if self.money >= cost:
                                self.money -= cost
                                self.add_tower(side_menu_button)

                        # look if you click on attack tower or support tower
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

            if not self.pause:
                # loop throuth enemies
                to_del = []
                for en in self.enemys:
                    en.move()
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

    def point_to_line(self,tower):
        """
        returns if you can place tower based on distance from path
        :param tower: Tower
        :return: bool
        """
        # find to closest points
        closest = []
        for point in path:
            dis = math.sqrt((tower.x - point[0])**2 + (tower.y - point[1])**2)
            closest.append([dis, point])

        closest.sort(key=lambda x: x[0])

        x = closest[0][1]
        y = closest[1][1]

        coefficients = np.polyfit(x, y, 1)


        #dis = abs(line_vectore[0] * tower.x + line_vectore[1]*tower.y + c)/math.sqrt(line_vectore[0]**2 + line_vectore[1]**2)

        return True

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        # for pos in self.path: # remove    red point
        #     pygame.draw.circle(self.win, (255,0,0), pos, 5, 0) # remove


        # draw placement rings
        if self.moving_object:
            for tower in self.attack_towers:
                tower.draw_placement(self.win)

            for tower in self.support_towers:
                tower.draw_placement(self.win)

            self.moving_object.draw_placement(self.win)

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

        # draw moving object
        if self.moving_object:
            self.moving_object.draw(self.win)

        # draw play pause button
        self.playPauseButton.draw(self.win)

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

        # draw wave
        self.win.blit(wave_bg, (10,10))
        text = self.life_font.render("Wave #" + str(self.wave), 1, (255,255,255))
        self.win.blit(text,(10 + wave_bg.get_width()/2 - text.get_width()/2, 30))


        pygame.display.update()

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_archer","buy_archer_1", "buy_damage", "buy_range"]
        object_list = [ArcherTowerLong(x, y), ArcherTowerShort(x, y), DamageTower(x, y), RangeTower(x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")




g = Game()
g.run()