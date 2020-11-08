import pygame
import random
from syslogic import CGGPYG 
import time
from cggframe import cggframe

class squash80(cggframe):

    def __init__(self):

        self.cgg=CGGPYG("")
        pygame.mixer.init()
        self.bgm=pygame.mixer.Sound("noisebeep.wav")
        self.bx=6
        self.by=16
        self.dx=-1
        self.dy=-1
        self.mx=4
        self.sc=0
        self.gamestate="title"
        self.ct=0

    def keyin(self,key):

        if self.gamestate=="title":
            if key==pygame.K_RETURN:
                self.gamestate="play"
        if self.gamestate=="play":
            if key==pygame.K_LEFT and self.mx>=2:
                self.mx=self.mx-1
            if key==pygame.K_RIGHT and self.mx<=8:
                self.mx=self.mx+1
        if self.gamestate=="gameover":
           if key==pygame.K_RETURN:
                self.__init__()
                self.gamestate="title" 


    def title(self):

        self.cgg.cls()
        self.cgg.setcolor(7)
        self.cgg.printc("8bit squash in pygame",5,5)
        self.cgg.printc("2018 tenkey aikoukai",5,7)
        self.cgg.printc("press ret key",5,9)
        pygame.display.flip()

    def gameover(self):

        self.cgg.printc("game over",8,9)

    def routine(self):

        self.ct=self.ct+1
        if self.ct>=5:
            self.update()
            self.ct=0
        self.draw()

    def update(self):

        if self.dx==-1 and self.bx<=1:
            self.dx=1
        if self.dx==1 and self.bx>=12:
            self.dx=-1
        if self.dy==-1 and self.by<=1:
            self.dy=1
        self.bx=self.bx+self.dx
        self.by=self.by+self.dy
        if self.by==16 and self.dy==1:
            if (self.mx-self.bx)>=-3 and (self.mx-self.bx)<=0:
                self.dy=-1
                self.sc=self.sc+1
                self.bgm.play()
                pygame.display.flip()
        if self.by>=18:
            self.gamestate="gameover" 
        self.draw()

    def draw(self):

        self.cgg.cls()
        self.cgg.setcolor(7)
        self.cgg.put("s",15,5)
        self.cgg.put("c",16,5)
        self.cgg.put("o",17,5)
        self.cgg.put("r",18,5)
        self.cgg.put("e",19,5)
        self.cgg.setcolor(7)
        self.putscore()
        self.cgg.setcolor(7)
        self.cgg.put("circle",self.bx,self.by)
        for i in range(0,3):
            self.cgg.put("equal",self.mx+i,17)
        for i in range(0,20):
            self.cgg.put("fill",0,i)
            self.cgg.put("fill",12,i)
        for i in range(0,13):
            self.cgg.put("fill",i,0)
            self.cgg.put("fill",i,19)

    def putscore(self):

        self.modsc=self.sc%10
        self.putnumchr(self.modsc,19,7)
        self.cursc=int(self.sc/10)
        self.modsc=self.cursc%10
        self.putnumchr(self.modsc,18,7)
        self.cursc=int(self.cursc/10)
        self.modsc=self.cursc%10
        self.putnumchr(self.modsc,17,7)

    def putnumchr(self,num,x,y):

        if num==0:
            self.cgg.put("0",x,y)
        if num==1:
            self.cgg.put("1",x,y)
        if num==2:
            self.cgg.put("2",x,y)
        if num==3:
            self.cgg.put("3",x,y)
        if num==4:
            self.cgg.put("4",x,y)
        if num==5:
            self.cgg.put("5",x,y)
        if num==6:
            self.cgg.put("6",x,y)
        if num==7:
            self.cgg.put("7",x,y)
        if num==8:
            self.cgg.put("8",x,y)
        if num==9:
            self.cgg.put("9",x,y)

sq=squash80()
sq.main(0.002)








