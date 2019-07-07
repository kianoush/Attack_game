import pygame
from .tower import Tower
import os
import math


range_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "4.png")),(90,90)),
              pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "5.png")),(90,90))]


class RangeTower(Tower):
    """
    Add extra range to each surrounding tower
    """
    def __init__(self, x, y):
        super(RangeTower,self).__init__(x,y)
        self.range = 75
        self.effect = [0.2, 0.4]
        self.tower_imgs = range_imgs[:]
        self.width = self.height = 90
        self.name = "range"


    def draw(self, win):
        super(RangeTower, self).draw_radius(win)
        super(RangeTower, self).draw(win)

    def support(self, towers):
        """
        will modify towers according to ability
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)

            if dis <= self.range + tower.width/2:
                effected.append(tower)

        for tower in effected:
            tower.range = tower.original_range + round(tower.range * self.effect[self.level - 1])

damage_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "8.png")),(90,90)),
              pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "9.png")),(90,90))]


class DamageTower(RangeTower):
    """
    add damage to surrounding towers
    """
    def __init__(self,x,y):
        super(DamageTower,self).__init__(x,y)
        self.range = 75
        self.tower_imgs = damage_imgs[:]
        self.effect = [.2, .4]
        self.width = self.height = 90
        self.name = "damage"

    def support(self, towers):
        """
        will modify towers according to ability
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)

            if dis <= self.range + tower.width/2:
                effected.append(tower)

        for tower in effected:
            tower.damage = tower.original_damage + round(tower.damage * self.effect[self.level - 1])