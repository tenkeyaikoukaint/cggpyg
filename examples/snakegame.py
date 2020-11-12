import random
from syslogic import CGGPYG
from cggframe import cggframe
import pygame

class linetest13(cggframe):

    def __init__(self):

        self.x=[10,10,10,11,12,12,12,12,11,10]
        self.y=[10,11,12,12,12,13,14,15,15,15]
        self.dx=0
        self.dy=-1
        self.fx=5
        self.fy=5
        self.length=8
        self.cgg=CGGPYG("")
        self.gamestate="play"
        self.timerct=0
        pygame.mixer.init()
        self.beep=pygame.mixer.Sound("po.wav")
        self.sc=0

    def keyin(self,key):

        if self.gamestate=="play":
            if key==pygame.K_UP:
                self.dy=-1
                self.dx=0
            if key==pygame.K_DOWN:
                self.dy=1
                self.dx=0
            if key==pygame.K_RIGHT:
                self.dx=1
                self.dy=0
            if key==pygame.K_LEFT:
                self.dx=-1
                self.dy=0
        if self.gamestate=="gameover" and key==pygame.K_RETURN:
            self.gamestate="play"
            self.__init__()

    def routine(self):

        self.timerct=self.timerct+1

        if self.timerct==5:
            self.update()

        if self.timerct>=10:
            self.timerct=0

    def update(self):

        self.cgg.cls()
        for i in range(self.length-1,-1,-1):
            self.x[i+1]=self.x[i]
            self.y[i+1]=self.y[i]
        self.x[0]=self.x[0]+self.dx
        self.y[0]=self.y[0]+self.dy
        for i in range(1,self.length+1):
             if self.x[0]==self.x[i] and self.y[0]==self.y[i]:
                 self.gamestate="gameover"
        if self.x[0]<=0 or self.x[0]>=39 or self.y[0]<=0 or self.y[0]>=19:
             self.gamestate="gameover"
        if self.x[0]==self.fx and self.y[0]==self.fy:
             self.length=self.length+1
             self.beep.play()
             self.sc=self.sc+1
             self.x=self.x+[self.length-1]
             self.y=self.y+[self.length-1]
             checkflag=1
             while checkflag==1:
                 self.rx=random.randint(2,37)
                 self.ry=random.randint(2,17)
                 checkflag=0
                 for i in range(0,self.length+1):
                     if self.rx==self.x[i] and self.ry==self.y[i]:
                         checkflag=1
             self.fx=self.rx
             self.fy=self.ry
        self.cgg.setcolor(1)
        for i in range(0,40):
            self.cgg.puth("sharp",i,0)
            self.cgg.puth("sharp",i,19)
        for i in range(0,20):
            self.cgg.puth("sharp",0,i)
            self.cgg.puth("sharp",39,i)
        self.cgg.setcolor(7)
        self.cgg.printc("score:"+str(self.sc)+"",0,20)
        self.cgg.setcolor(4)
        for i in range(1,self.length):
            self.cgg.puth("circle",self.x[i],self.y[i])
        self.cgg.setcolor(7)
        self.cgg.puth("circle",self.x[0],self.y[0])
        self.cgg.setcolor(3)
        self.cgg.puth("heart",self.fx,self.fy)

lt=linetest13()
lt.main(0.01)
