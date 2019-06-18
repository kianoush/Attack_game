import pygame
import os
from .enemy import Enemy


class Scorpion(Enemy):

    def __init__(self):
        super(Scorpion, self).__init__()

        self.imgs = []

        for x in range(9):
            add_str = str(x)
            if x < 10:
                add_str = "0" + add_str
            self.imgs.append(pygame.transform.scale(
                pygame.image.load(os.path.join("game_assets/enemies/1/", "1_enemies_1_RUN_0" + add_str + ".png")),
                (64, 64)))

