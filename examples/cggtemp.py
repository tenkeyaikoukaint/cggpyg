"""extended-helmet an action RPG"""

import pygame
import random
import time
from syslogic import CGGPYG
from cggframe import cggframe

class cggtemp(cggframe):

    def __init__(self):

        self.cgg=CGGPYG("")
        self.m=[]
        for i in range(0,21):
            for j in range(0,41):
                self.m[len(self.m):] = [0]
        self.mx=0
        self.my=16
        self.sc=0
        self.gamestate="play"
        self.miss=0

    def keyin(self,key):

        if self.gamestate=="title" and key==pygame.K_RETURN:
            self.gamestate="play"
        if self.gamestate=="play":
            if key==pygame.K_RIGHT and self.mx<19:
                self.mx=self.mx+1
            if key==pygame.K_LEFT and self.mx>0:
                self.mx=self.mx-1
        if self.gamestate=="gameover" and key==pygame.K_RETURN:
            self.__init__()
            self.gamestate="play" 

    def draw(self):

        self.cgg.cls()
        self.cgg.setcolor(2)
    def gameover(self):

        self.cgg.setcolor(2)
        self.cgg.printc("game over",15,10)

    def routine(self):

        self.draw()

ct=cggtemp()
ct.main(0.1)

