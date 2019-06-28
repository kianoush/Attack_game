import pygame
from .tower import Tower
import os
import math
import time


range_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "4.png")),(90,90)),
              pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "5.png")),(90,90))]


class RangeTower(Tower):
    """
    Add extra range to each surrounding tower
    """
    def __init__(self, x, y):
        super(RangeTower,self).__init__(x,y)
        self.range = 150
        self.effect = [0.2, 0.4]
        self.tower_imgs = range_imgs[:]


    def draw(self, win):
        super(RangeTower, self).draw_radius(win)
        super(RangeTower, self).draw(win)

    def support(self, towers):
        """
        will modify towers according to ability
        :param towers: list
        :return: None
        """
        pass


damage_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "8.png")),(90,90)),
              pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "9.png")),(90,90))]


class DamageTower(RangeTower):
    """
    add damage to surrounding towers
    """
    def __init__(self,x,y):
        super(DamageTower,self).__init__(x,y)
        self.range = 150
        self.tower_imgs = damage_imgs[:]
        self.effect = [1, 2]

    def support(self, towers):
        """
        will modify towers according to ability
        :param towers: list
        :return: None
        """
        pass