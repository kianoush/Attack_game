import pygame
import os

pygame.font.init()

star = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "star.png")), (40, 40))

class Buttom:
    """
    Button class for menu objects
    """
    def __init__(self,x,y, img, name):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def click(self, X, Y):
        """
        return if the position has collided with the menu
        :param X: int
        :param Y: int
        :return: bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <=self.y + self.height and Y >= self.y:
                return True
        return False

    def draw(self,win):
        win.blit(self.img, (self.x , self.y))


class Menu:
    """
    menu for holding items
    """
    def __init__(self,tower,x,y,img,item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.item_cost = item_cost
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont("comicsans", 28)
        self.tower = tower

    def add_btn(self, img, name):
        """
        adds button to menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.items += 1
        btn_x = self.x - self.bg.get_width()/2 +10
        btn_y = self.y - 120 +10
        self.buttons.append(Buttom(btn_x, btn_y, img, name))


    def draw(self, win):
        """
        draws btns and menu bg
        :param win: surface
        :return: None
        """
        win.blit(self.bg, (self.x - self.bg.get_width()/2, self.y - 120))
        for item in self.buttons:
            item.draw(win)
            win.blit(star, (item.x + item.width + 6 , item.y + 1))
            text = self.font.render(str(self.item_cost[self.tower.level - 1]), 1, (255,255,255))
            win.blit(text, (item.x + item.width + 27 - text.get_width()/2,  item.y + star.get_height()-2))


    def get_clicked(self,X,Y):
        """
        return the clicked item from the menu
        :param x: int
        :param y: int
        :return: str
        """
        for btn in self.buttons:
            if btn.click(X,Y):
                return btn.name
        return None