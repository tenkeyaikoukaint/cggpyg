import pygame
import random
from syslogic import CGGPYG 
import time
from cggframe import cggframe

class squash80(cggframe):

    def __init__(self):

        self.cgg=CGGPYG("")
        self.bx=random.randint(1,9)
        self.by=16
        self.dx=-1
        self.dy=-1
        self.mx=4
        self.sc=0
        self.gamestate="title"
        self.ct=0
        self.wx=[]
        self.wy=[]
        self.wf=[]
        pygame.mixer.init()
        self.beep=pygame.mixer.Sound("po.wav")
        for i in range(0,40):
            self.wx[len(self.wx):]=[(i%9)+2]
            self.wy[len(self.wy):]=[int(i/9)+2]
            if i<=26:
                self.wf[len(self.wf):]=[1]
            else:
                self.wf[len(self.wf):]=[0]

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
        self.cgg.printc("breakout in pygame",5,5)
        self.cgg.printc("2018 tenkey aikoukai",5,7)
        self.cgg.printc("press ret key",5,9)
        pygame.display.flip()

    def gameover(self):

        self.cgg.setcolor(2)
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
        if self.dx==1 and self.bx>=11:
            self.dx=-1
        if self.dy==-1 and self.by<=1:
            self.dy=1
        hitflag=0
        for i in range(0,27):
            if hitflag==0:
                if self.wx[i]==self.bx and self.wy[i]==self.by+1 and self.wf[i]==1:
                    self.dy=1
                    self.sc=self.sc+1
                    self.wf[i]=0
                    hitflag=1
        for i in range(0,27):
            if hitflag==0:
                if self.wx[i]==self.bx+self.dx and self.wy[i]==self.by+self.dy and self.wf[i]==1 and self.wf[i+9]==0:
                    self.dx=-1*self.dx
                    self.dy=1
                    self.sc=self.sc+1
                    self.wf[i]=0 
                    hitflag=1
        if hitflag==0:
            self.bx=self.bx+self.dx
            self.by=self.by+self.dy
        if hitflag==1:
            self.beep.stop()
            self.beep.play()
            pygame.display.flip()
        if self.by==16 and self.dy==1:
            if (self.mx-self.bx)>=-3 and (self.mx-self.bx)<=0:
                self.dy=-1
        if self.by>=18:
            self.gamestate="gameover" 
        self.draw()

    def draw(self):

        self.cgg.cls()
        self.cgg.setcolor(7)
        self.cgg.printc("score "+str(self.sc),1,21)
        self.cgg.setcolor(2)
        for i in range(0,27):
            if self.wf[i]==1:
                self.cgg.put("brick",self.wx[i],self.wy[i])
        self.cgg.setcolor(6)
        self.cgg.put("circle",self.bx,self.by)
        self.cgg.setcolor(7)
        for i in range(0,3):
            self.cgg.put("equal",self.mx+i,17)
        self.cgg.setcolor(1)
        for i in range(0,20):
            self.cgg.put("brick",0,i)
            self.cgg.put("brick",12,i)
        for i in range(0,13):
            self.cgg.put("brick",i,0)
            self.cgg.put("brick",i,19)

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








