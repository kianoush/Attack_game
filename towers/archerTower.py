import pygame
from .tower import Tower
import os


class ArcherTowerLong(Tower):
    def __init__(self, x, y):
        super(ArcherTowerLong, self).__init__(x, y)
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0
        self.range = 50
        self.inRange = False

        # load archer tower images
        for x in range(7, 10):
            self.tower_imgs.append(pygame.transform.scale(
                pygame.image.load(os.path.join("game_assets/archer_towers/archer_1", str(x) + ".png")),
                (90, 90)))

        # load archer images
        for x in range(37, 43):
            self.archer_imgs.append(
                pygame.image.load(os.path.join("game_assets/archer_towers/archer_top", str(x) + ".png")),)


    def draw(self, win):
        super(ArcherTowerLong, self).draw(win)
        if self.archer_count >= len(self.archer_imgs)*10:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count//10]
        win.blit(archer, ((self.x + self.width/2 - 25), (self.y - archer.get_height() - 25)))
        self.archer_count += 1

    def change_range(self, r):
        """
        change range of archer tower
        :param r: int
        :return: None
        """
        self.range = r

    def attack(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """
        pass
