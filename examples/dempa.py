import time
import random
import pygame
from syslogic import CGGPYG

class Dempa():

    def __init__(self):
        self.cgg=CGGPYG()
        self.tim="noon"
        self.counter=0
        self.sunct=0
        self.birdct=0
        self.sunx=[19,18,16,14,12,10,8,6,4,3,2,2]
        self.suny=[10,7,4,3,2,2,2,3,5,7,10,10]

    def drawscene(self):
        if self.tim=="noon":
            self.cgg.setcolor(5)
            for i in range(0,20):
                for j in range(0,20):
                    self.cgg.put("fill",i,j)
            self.cgg.setcolor(0)
            for i in range(7,16):
                for j in range(8,13):
                    self.cgg.put("fill",i,j)
        if self.tim=="evening":
            self.cgg.setcolor(2)
            for i in range(0,20):
                for j in range(0,20):
                    self.cgg.put("fill",i,j)
            self.cgg.setcolor(0)
            for i in range(7,16):
                for j in range(8,13):
                    self.cgg.put("fill",i,j)
        if self.tim=="night":
            self.cgg.setcolor(0) 
            for i in range(0,20):
                for j in range(0,20):
                    self.cgg.put("fill",i,j)
        for i in range(7,16):
            if self.tim=="noon" or self.tim=="evening":
                self.cgg.setcolor(7)
            if self.tim=="night" and i%2==0 and self.counter%2==0 or self.tim=="night" and i%2==1 and self.counter%2==1:
                self.cgg.setcolor(7)
            if self.tim=="night" and i%2==0 and self.counter%2==1 or self.tim=="night" and i%2==1 and self.counter%2==0:
                self.cgg.setcolor(6)
            self.cgg.put("circle",i,8)
            self.cgg.put("circle",i,12)
        for i in range(8,12):
            if self.tim=="night" and i%2==0 and self.counter%2==0 or self.tim=="night" and i%2==1 and self.counter%2==1:
                self.cgg.setcolor(6)
            if self.tim=="night" and i%2==0 and self.counter%2==1 or self.tim=="night" and i%2==1 and self.counter%2==0:
                self.cgg.setcolor(7)
            self.cgg.put("circle",7,i)
            self.cgg.put("circle",15,i)
        if self.tim=="noon" or self.tim=="evening":
            self.cgg.setcolor(7)
        if self.tim=="night":
            self.cgg.setcolor(0)
        for i in range(7,16):
            for j in range(13,20):
                self.cgg.put("fill",i,j)
        if self.tim=="noon" or self.tim=="evening":
            self.cgg.setcolor(5)
        if self.tim=="night":
            self.cgg.setcolor(6)
        self.putwindow(8,14)
        self.putwindow(12,14)
        self.putwindow(8,17)
        self.putwindow(12,17)
        if self.tim=="noon" or self.tim=="evening":
            self.cgg.setcolor(7)
        if self.tim=="night":
            self.cgg.setcolor(7)
        self.cgg.put("d",9,9)
        self.cgg.put("e",10,9)
        self.cgg.put("m",11,9)
        self.cgg.put("p",12,9)
        self.cgg.put("a",13,9)
        self.cgg.put("b",10,11)
        self.cgg.put("l",11,11)
        self.cgg.put("d",12,11)
        self.cgg.put("g",13,11)
        if self.tim=="noon":
            self.cgg.setcolor(6)
            self.cgg.put("circle",self.sunx[self.sunct],self.suny[self.sunct])
        if self.counter%2==0:
            self.sunct=self.sunct+1
        if self.sunct>=10:
            self.sunct=0
        if self.tim=="evening":
            self.cgg.setcolor(0)
            if self.birdct%2==0:
                self.cgg.put("se",20-self.birdct,3)
            if self.birdct%2==1:
                self.cgg.put("ne",20-self.birdct,3)
            self.birdct=self.birdct+1
            if self.birdct>=20:
                self.birdct=0

    def putwindow(self,x,y):

        for i in range(y,y+2):
            for j in range(x,x+3):
                self.cgg.put("fill",j,i)

    def routine(self):
        offset=0
        self.counter=self.counter+1
        if self.counter>=20:
            offset=0
            if self.tim=="noon":
                self.tim="evening"
                offset=1
            if self.tim=="night":
                self.tim="noon"
            if self.tim=="evening" and offset==0:
                self.tim="night"
            self.counter=0
        self.drawscene()


dp=Dempa()
endflag=0
while endflag==0:
    dp.routine()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:endflag=1
    pygame.display.flip()  
    time.sleep(0.5)




 

