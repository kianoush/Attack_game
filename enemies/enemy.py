import pygame
import math

class Enemy:
    imgs = []

    def __init__(self):

        self.width = 64
        self.health = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(25, 223), (106, 223), (175, 234), (233, 269), (310, 272), (384, 271), (450, 270), (518, 268), (566, 255), (607, 213), (621, 158), (646, 101), (711, 63), (770, 67), (807, 106), (824, 144), (839, 195), (860, 242), (916, 274), (969, 281), (1014, 318), (1039, 380), (1033, 441), (992, 484), (921, 494), (811, 494), (749, 500), (701, 535), (634, 556), (552, 554), (169, 554), (108, 510), (87, 449), (68, 393), (35, 355), (0, 339), (-20, 359)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0


    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win:
        :return:
        """

        self.img = self.imgs[self.animation_count//3]
        self.animation_count += 1
        if self.animation_count >= len(self.imgs)*3:
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))
        self.move()


    def collide (self, X, Y):
        """
        Returns if position has hit enemy
        :param x: int
        :param y: int
        :return: Bool
        """

        if X < self.x + self.width and X >= self.x:
            if Y <= self.y + self.health and Y >= self.y:
                return True

        return False


    def move(self):
        """
        Move enemy
        :return: None
        """
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 339)
        else:
            x2, y2 = self.path[self.path_pos+1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.move_count += 1
        dirn = (x2-x1, y2-y1)

        move_x, move_y = (self.x + dirn[0] + self.move_count, self.y + dirn[1] + self.move_count)
        self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)

        # Go to next point
        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1
            if self.path_pos >= len(self.path):
                return False

        self.x = move_x
        self.y = move_y
        return True

    def hit(self):
        """
        Returns if an enemy has died and removes one health
        each call
        :return:
        """
        self.health -= 1
        if self.heralth <= 0:
            return True