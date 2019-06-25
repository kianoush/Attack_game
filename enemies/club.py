import pygame
import os
from .enemy import Enemy


class Club(Enemy):

    def __init__(self):
        super(Club, self).__init__()
        self.imgs = []
        self.max_health = 5
        self.health = self.max_health

        for x in range(9):
            add_str = str(x)
            if x < 10:
                add_str = "0" + add_str
            self.imgs.append(pygame.transform.scale(
                pygame.image.load(os.path.join("game_assets/enemies/2/", "2_enemies_1_RUN_0" + add_str + ".png")),
                (70, 70)))





