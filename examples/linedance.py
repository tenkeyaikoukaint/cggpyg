import time
import random
import pygame
from syslogic import CGGPYG
from cggframe import cggframe

class linetest(cggframe):

    def __init__(self):

        self.cgg=CGGPYG("")
        self.gamestate="play"

        """x1,y1:startpoint x2,y2:endpoint of line"""

        self.x1=100
        self.x2=400
        self.y1=100
        self.y2=400
        self.dx1=10
        self.dy1=10
        self.dx2=10
        self.dy2=10
        self.ct=0

    def routine(self):

        self.ct=self.ct+1
        if self.ct>=100:
            self.cgg.cls()
            self.ct=0
        self.x1=self.x1+self.dx1
        self.y1=self.y1+self.dy1
        self.x2=self.x2+self.dx2
        self.y2=self.y2+self.dy2
        if self.x1<0 and self.dx1<0:self.dx1=-self.dx1
        if self.x2<0 and self.dx2<0:self.dx2=-self.dx2
        if self.y1<0 and self.dy1<0:self.dy1=-self.dy1
        if self.y2<0 and self.dy2<0:self.dy2=-self.dy2
        if self.x1>640 and self.dx1>0:self.dx1=-self.dx1
        if self.x2>640 and self.dx2>0:self.dx2=-self.dx2
        if self.y1>400 and self.dy1>0:self.dy1=-self.dy1
        if self.y2>400 and self.dy2>0:self.dy2=-self.dy2
        self.draw()

    def keyin(self,key):

        if self.gamestate=="play" and key==pygame.K_SPACE:
            self.dx1=-self.dx1
            self.dx2=-self.dx2
            self.dy1=-self.dy1
            self.dy2=-self.dy2

    def draw(self):

        self.cgg.setcolor(4)
        self.cgg.line(self.x1,self.y1,self.x2,self.y2)

lt=linetest()
lt.main(0.2)
