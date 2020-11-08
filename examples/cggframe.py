import pygame
import time

class cggframe():

    def __init__(self):

        pass

    def main(self,ti):

        self.endflag=0
        while self.endflag==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.endflag=1
                if event.type==pygame.KEYDOWN:
                    self.keyin(event.key) 
            pygame.display.flip() 
            self.statemanager()
            time.sleep(ti)

    def statemanager(self):

        if self.gamestate=="title":
            self.title()
        if self.gamestate=="play":
            self.routine()
        if self.gamestate=="gameover":
            self.gameover()

    def title(self):

        self.cgg.cls()
        self.cgg.setcolor(7)
        self.cgg.printc("title",5,9)

    def gameover(self):

        self.cgg.setcolor(2)
        self.cgg.printc("game over",15,10)

    def keyin(self,key):

        if self.gamestate=="title":
            if key==pygame.K_RETURN:
                self.gamestate="play"
        if self.gamestate=="play":
            if key==pygame.K_LEFT and self.x >= 1:
                self.x = self.x - 1 
            if key==pygame.K_RIGHT and self.x < 19:
                self.x = self.x + 1 
        if self.gamestate=="gameover":
            if key==pygame.K_RETURN:
                self.__init__()
                self.gamestate="title"

    def draw(self):

        pass

    def routine(self):

        self.draw()



