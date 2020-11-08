import pygame
from syslcd4l import CGGPYG
import time
import random
from cggframe import cggframe

class gameobj:

    def __init__(self):

        self.mx=7
        self.my=2
        self.ex=32
        self.ey=random.randint(0,3)
        self.bx=0
        self.by=0
        self.bulletflag=False
        self.edy=random.randint(0,6)
        self.ct=0
        self.sc=0
        self.miss=0

class pokeshoot(cggframe):

    def __init__(self):

        self.cgg=CGGPYG()
        pygame.mixer.init()
        self.bgm=pygame.mixer.Sound("flute.wav")
        self.shotm=pygame.mixer.Sound("powa.wav")
        self.m=[0,0]
        self.gameflag=0
        for i in range(0,21):
            for j in range(0,21):
                self.m[len(self.m):] = [0] 

        self.gamestate="title"
        self.obj=gameobj()

    def title(self):

        self.cgg.cls()
        self.cgg.setcolor(5)
        self.cgg.printc("pocket shooting",0,1)
        self.cgg.printc("press ret key",0,2)

    def gameover(self):

        self.cgg.setcolor(2)
        self.cgg.printc("         ",15,2)
        self.cgg.printc("game over",15,2)

    def keyin(self,key):

        if self.gamestate=="title":
            if key==pygame.K_RETURN:
                self.gamestate="play"
        if self.gamestate=="play":
            if key==pygame.K_UP and self.obj.my>0:
                self.obj.my=self.obj.my-1
            if key==pygame.K_DOWN and self.obj.my<3:
                self.obj.my=self.obj.my+1
            if key==pygame.K_RIGHT:
                self.shotm.play()
                self.shoot()
        if self.gamestate=="gameover":
            if key==pygame.K_RETURN:
                self.__init__()

    def shoot(self):

        self.obj.bulletflag=True
        self.obj.bx=self.obj.mx
        self.obj.by=self.obj.my

    def routine(self):

        """move bullet"""
        if self.obj.bulletflag:
            self.obj.bx=self.obj.bx+1
            self.shootcheck()
        self.update()

    def shootcheck(self):
        """collide bullet to enemy"""
        if self.obj.bx==self.obj.ex and self.obj.by==self.obj.ey:
            self.obj.sc=self.obj.sc+1
            self.bgm.play()
            pygame.display.flip()
            self.egen()
        if self.obj.bx>=17:
            self.obj.bulletflag=False

    def egen(self):

        self.obj.ex=31
        self.obj.ey=random.randint(0,3)
        self.obj.edy=random.randint(0,6)

    def update(self):

        """enemy move and check"""
        if self.obj.ex>=9:
            self.obj.ex=self.obj.ex-1
        else:
            self.obj.miss=self.obj.miss+1
            if self.obj.miss>=5:
                self.gamestate="gameover"
            else:
                self.egen()
        if self.obj.bulletflag:
            self.shootcheck()
        """enemy vertical move with own algorhythm(1-6)"""
        if self.obj.edy==1:
            if self.obj.ey<=2:
                self.obj.ey=self.obj.ey+1
            else:
                self.obj.edy=2
        elif self.obj.edy==2:
            if self.obj.ey>=1:
                self.obj.ey=self.obj.ey-1
            else:
                self.obj.edy=1
        elif self.obj.edy==3:
            if self.obj.ey<=2:
                self.obj.ey=self.obj.ey+1
            else:
                self.obj.edy=4
        elif self.obj.edy==4:
            if self.obj.ey>=2:
                self.obj.ey=self.obj.ey-1
            else:
                self.obj.edy=3
        elif self.obj.edy==5:
            if self.obj.ey<=1:
                self.obj.ey=self.obj.ey+1
            else:
                self.obj.edy=6
        elif self.obj.edy==6:
            if self.obj.ey>=1:
                self.obj.ey=self.obj.ey-1
            else:
                self.obj.edy=5
        self.draw()

    def draw(self):

        self.cgg.cls()
        """draw my ship"""
        self.cgg.setcolor(7)
        self.cgg.puth("sw",self.obj.mx,self.obj.my)
        """draw enemy"""
        self.cgg.puth("spade",self.obj.ex,self.obj.ey)
        """draw bullet"""
        if self.obj.bulletflag:
            self.cgg.puth("-",self.obj.bx,self.obj.by)
        """display score and miss"""
        self.cgg.printc("score",0,0)
        self.cgg.printc(str(self.obj.sc),0,1)
        self.cgg.printc("miss",0,2)
        """display frame"""
        self.cgg.printc(str(self.obj.miss),0,3)
        for i in range(0,4):
            self.cgg.puth(":",5,i)

ps=pokeshoot()
ps.main(0.1)



