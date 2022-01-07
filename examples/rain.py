import pygame
import random
import time
from syslogic import CGGPYG
from cggframe import cggframe

class rainfall(cggframe):

    def __init__(self):

        self.cgg=CGGPYG("")
        self.m=[]
        for i in range(0,21):
            for j in range(0,41):
                self.m[len(self.m):] = [0]
        for i in range(0,19):
            r = random.randint(1,10)
            if r == 1:
                self.m[1*40 +i] = 1
            else:
                self.m[i*40+ 1] = 0
        self.gamestate="play"

    def draw(self):

        self.cgg.cls()
        self.cgg.setcolor(5)
        for i in range(0,19):
            for j in range(0,39):
                if self.m[i*40+j]>0:
                    self.cgg.puth("circle",j,i)

    def scroll(self):

        for i in range(0,39):
            r = random.randint(1,40)
            self.m[1*40+i] = 0
            if r == 1:
                self.m[1*40+i] = 2
            if r == 2:
                self.m[1*40+i] = 6 
        for i in range(18,0,-1):
            for j in range(0,39):
                self.m[(i+1)*40+j] = self.m[i*40+j] 
        self.draw() 


    def routine(self):

        self.scroll()

rf=rainfall()
rf.main(0.02)


