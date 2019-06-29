import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(9):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/1/", "1_enemies_1_RUN_0" + add_str + ".png")),
        (70, 70)))


class Scorpion(Enemy):

    def __init__(self):
        super(Scorpion, self).__init__()
        self.name = "scorpion"
        self.money = 1
        self.imgs = imgs[:]
        self.max_health = 1
        self.health = self.max_health
