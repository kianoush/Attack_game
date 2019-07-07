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
        self.path = [(12, 551), (159, 549), (334, 548), (405, 539), (454, 475), (455, 401), (521, 332), (620, 329), (668, 370), (690, 439), (715, 510), (771, 544), (843, 548), (1065, 542), (1269, 542), (1338, 544), (1191, 550)] #  change area (614, 429) ---> [(648, 397), (690, 381), (725, 353), (749, 318), (760, 275), (776, 229), (804, 194), (853, 172), (900, 167), (953, 164), (1007, 162), (1056, 172), (1084, 179), (1109, 194), (1129, 211), (1154, 218), (1185, 218), (1196, 217)]
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
        self.max_health = 0


    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win:
        :return:
        """

        self.img = self.imgs[self.animation_count]


        win.blit(self.img, (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2 - 23))
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """
        length = 40
        move_by = round(length / self.max_health)
        lealth_bar = move_by * self.health

        pygame.draw.rect(win, (255,0,0),(self.x-35, self.y-50, length, 7), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x-35, self.y -50, lealth_bar, 7), 0)

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
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (1210, 560)
        else:
            x2, y2 = self.path[self.path_pos+1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


        self.move_count += 1
        dirn = ((x2-x1)*2, (y2-y1)*2)
        length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
        dirn = (dirn[0]/length, dirn[1]/length)


        # rotate the enemy
        if dirn[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = (self.x + dirn[0]), (self.y + dirn[1])
        self.dis += length

        self.x = move_x
        self.y = move_y

        # Go to next point
        if dirn[0] >= 0:  # moving right
            if dirn[1] >= 0:  # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                    if self.x >= x2 and self.y <= y2:
                        self.path_pos += 1
        else:  # moving left
            if dirn[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                    if self.x <= x2 and self.y <= y2:
                        self.path_pos += 1


    def hit(self, damage):
        """
        Returns if an enemy has died and removes one health
        each call
        :return:
        """
        self.health -= damage
        if self.health <= 0:
            return True
        return False
