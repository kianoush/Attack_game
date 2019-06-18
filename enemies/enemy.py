""" Enemy Class """
import pygame
import math

class Enemy:


    def __init__(self):

        self.width = 64
        self.health = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(10, 553), (56, 549), (111, 548), (166, 550), (223, 551), (285, 551), (341, 547), (379, 516), (396, 464), (405, 415), (422, 390), (455, 352), (505, 343), (552, 341), (582, 359), (602, 386), (615, 428), (629, 462), (641, 496), (659, 519), (698, 542), (750, 547), (787, 545), (823, 547), (877, 548), (942, 553), (1006, 554), (1057, 551),(1070, 551), (1090, 550),(1124, 551), (1135, 550),(1155, 551), (1175, 550), (1198, 551), (1191, 550),(0, 0)] #  change area (614, 429) ---> [(648, 397), (690, 381), (725, 353), (749, 318), (760, 275), (776, 229), (804, 194), (853, 172), (900, 167), (953, 164), (1007, 162), (1056, 172), (1084, 179), (1109, 194), (1129, 211), (1154, 218), (1185, 218), (1196, 217)]
        #self.path = [(25, 223), (106, 223), (175, 234), (233, 269), (310, 272), (384, 271), (450, 270), (518, 268), (566, 255), (607, 213), (621, 158), (646, 101), (711, 63), (770, 67), (807, 106), (824, 144), (839, 195), (860, 242), (916, 274), (969, 281), (1014, 318), (1039, 380), (1033, 441), (992, 484), (921, 494), (811, 494), (749, 500), (701, 535), (634, 556), (552, 554), (169, 554), (108, 510), (87, 449), (68, 393), (35, 355), (0, 339), (-20, 359)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.imgs = []
        self.flipped = False


    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win:
        :return:
        """

        self.img = self.imgs[self.animation_count]
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))
        self.move()


    def collide (self, X, Y):
        """
        Returns if position has hit enemy
        :param X: int
        :param Y: int
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
        print(len(self.path))
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (1210, 560)
        else:
            x2, y2 = self.path[self.path_pos+1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.move_count += 1
        dirn = (x2-x1, y2-y1)

        if dirn[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)


        move_x, move_y = ((self.x + dirn[0] + self.move_count), (self.y + dirn[1] + self.move_count))
        self.dis += (math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2))

        self.x = move_x
        self.y = move_y

        # Go to next point
        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1
            if self.path_pos >= len(self.path):
                return False


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