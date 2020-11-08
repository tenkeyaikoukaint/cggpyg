from syslogic import CGGPYG 
import pygame
import random
import time 
class Aquarium:
    def __init__(self):
        self.fishx=[0,2,4,2,7,15,10,12]
        self.fishy=[0,5,6,9,12,15,10,8]
        self.fishd=[0,1,3,1,3,3,1,1]
        self.kombud=[0,1,2]
        self.cgg=CGGPYG("marine")

 
    def routine(self):
        """"beep(1)"""
        for i in range(1,7):
            r=random.randint(0,3)
            if r==1 and self.fishy[i]>3:
                self.fishy[i]=self.fishy[i]-1
            if r==2 and self.fishy[i]<18:
                self.fishy[i]=self.fishy[i]+1
            self.fishx[i]=self.fishx[i]+self.fishd[i]-2
            if self.fishd[i]==1 and self.fishx[i]<3:
                self.fishd[i]=3
            if self.fishd[i]==3 and self.fishx[i]>17:
                self.fishd[i]=1
        if self.kombud[1]==1:
            self.kombud[1]=2
        else:
            self.kombud[1]=1
        if self.kombud[2]==1:
            self.kombud[2]=2
        else:
            self.kombud[2]=1
        self.cgg.cls()
        self.drawchr()
        self.drawwave()
 
    def drawchr(self):

        """draw fish"""

        for i in range(1,7):
            self.cgg.setcolor(i)
            if self.fishd[i]==1:
                self.cgg.put("se",self.fishx[i],self.fishy[i])
                self.cgg.put("sw",self.fishx[i]+1,self.fishy[i])
                self.cgg.put("se",self.fishx[i]+2,self.fishy[i])

            else:
                self.cgg.put("sw",self.fishx[i],self.fishy[i])
                self.cgg.put("se",self.fishx[i]-1,self.fishy[i])
                self.cgg.put("sw",self.fishx[i]-2,self.fishy[i])


        """draw kombu"""

        self.cgg.setcolor(4)
        if self.kombud[1]==1:
            self.cgg.put("se",5,14)
            self.cgg.put("ne",5,15)
            self.cgg.put("sw",6,16)
            self.cgg.put("nw",6,17)
            self.cgg.put("se",5,18)
            self.cgg.put("ne",5,19)

        if self.kombud[1]==2:
            self.cgg.put("sw",6,14)
            self.cgg.put("nw",6,15)
            self.cgg.put("se",5,16)
            self.cgg.put("ne",5,17)
            self.cgg.put("sw",6,18)
            self.cgg.put("nw",6,19)

        if self.kombud[2]==1:
            self.cgg.put("se",15,14)
            self.cgg.put("ne",15,15)
            self.cgg.put("sw",16,16)
            self.cgg.put("nw",16,17)
            self.cgg.put("se",15,18)
            self.cgg.put("ne",15,19)

        if self.kombud[2]==2:
            self.cgg.put("sw",16,14)
            self.cgg.put("nw",16,15)
            self.cgg.put("se",15,16)
            self.cgg.put("ne",15,17)
            self.cgg.put("sw",16,18)
            self.cgg.put("nw",16,19)

    def drawwave(self):

        for i in range(0,39):
            if i<=10 or i>=14:
             r=random.randint(0,1)
            self.cgg.setcolor(5)
            self.cgg.put("wave",i,r)

aq=Aquarium()
endflag=0
while endflag==0:
    aq.routine()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:endflag=1
    pygame.display.flip() 
    time.sleep(0.5)




