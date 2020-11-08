
import pygame
from syslogic import CGGPYG
import time
import random

class pokeshoot():

    def __init__(self):

        self.cgg=CGGPYG("")
        self.m=[0,0]
        self.gameflag=0
        for i in range(0,21):
            for j in range(0,21):
                self.m[len(self.m):] = [0] 

        self.wy=[]
        self.wf=[]
        for i in range(0,20):
            self.wy[len(self.wy):]=[0]
            self.wf[len(self.wf):]=[0]
        self.wy[0]=random.randint(10,16)
        for i in range(1,20):
            self.wy[i]=self.wy[i-1]+random.randint(0,2)-1

        self.gamestate="title"
        self.sc = 0 
        self.mx = 0
        self.my = 2
        self.ex = 31
        self.ey = random.randint(0,3)
        self.bx = 0
        self.by = 0
        self.shoot = 0
        self.edy=random.randint(0,6)
        self.dw=1
        self.jumpct=0
        self.boaty=0
        self.boaty2=0
        self.miss=0

    def statemanager(self):

        if self.gamestate=="title":
            self.title()
        if self.gamestate=="play":
            self.routine()
        if self.gamestate=="gameover":
            self.gameover()

    def title(self):

        self.cgg.cls()
        self.cgg.setcolor(4)
        self.cgg.printc("cggpyg bmx game",12,8)
        self.cgg.printc("press ret key",12,10)

    def gameover(self):

        self.cgg.setcolor(2)
        self.cgg.printc("game over",15,10)

    def keyin(self,key):

        if self.gamestate=="title":
            if key==pygame.K_RETURN:
                self.gamestate="play"
        if self.gamestate=="play":
            if key==pygame.K_UP and self.jumpct==0:
                self.jumpct=1
                self.boaty=self.wy[3]
        if self.gamestate=="gameover":
            if key==pygame.K_RETURN:
                self.__init__()

    def draw(self):

        self.cgg.cls()
        if self.jumpct==0:self.boaty=self.wy[3]
        if self.jumpct>0:
             if self.jumpct<10:
                 self.boaty=self.boaty-1
             else:
                 if self.boaty<self.wy[3]:
                     self.boaty=self.boaty+1
        if self.jumpct==0:self.boaty2=self.wy[4]
        if self.jumpct>0:
            if self.jumpct<10:
                self.boaty2=self.boaty2-1
            else:
                if self.boaty2<self.wy[4]:
                    self.boaty2=self.boaty2+1
        for i in range(0,20):
            if self.wf[i]==0:
                self.cgg.setcolor(4)
                self.cgg.put("fill",i,self.wy[i])
            elif self.wf[i]==1:
                self.cgg.setcolor(2)
                self.cgg.put("fill",i,self.wy[i])
            else:
                self.cgg.setcolor(6)
                self.cgg.put("fill",i,self.wy[i])
        self.cgg.setcolor(0)
        self.cgg.put("fill",3,self.boaty)
        self.cgg.setcolor(7)
        self.cgg.put("circle",3,self.boaty)
        self.cgg.put("circle",4,self.boaty2)
        self.cgg.line(32*3+16,self.boaty*20+10,32*4+16,self.boaty2*20+10)
        self.cgg.line(32*4+16,self.boaty2*20+10,32*4+16,self.boaty2*20-10)
        self.cgg.line(32*4+16,self.boaty2*20-10,32*4-16,self.boaty2*20-10)
        self.cgg.printc("score:"+str(self.sc)+" miss:"+str(self.miss),1,20)

    def routine(self):

        self.sc=self.sc+1
        if self.jumpct>0:
            self.jumpct=self.jumpct+1
        if self.jumpct>=20:
            self.jumpct=0

        if self.wy[3]==self.boaty and self.wf[3]==1:
            self.miss=self.miss+1
            if self.miss>=30:
                self.gamestate="gameover"
        if self.wy[3]==self.boaty and self.wf[3]==2:
            self.miss=0
        for i in range(0,19):
            self.wy[i]=self.wy[i+1]
            self.wf[i]=self.wf[i+1]
        r=random.randint(0,10)
        if r==5:self.dw=-self.dw
        self.wy[19]=self.wy[18]+self.dw
        if self.wy[19]<=10 and self.dw<0:
            self.dw=-self.dw
        if self.wy[19]>=19 and self.dw>0:
            self.dw=-self.dw
        if random.randint(0,5)==1:
            self.wf[19]=1
        elif random.randint(0,1000)==1:
                self.wf[19]=2
        else:self.wf[19]=0


        self.draw()


ps=pokeshoot()
gameflag=0
endflag=0
while endflag==0:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            endflag=1
        if event.type==pygame.KEYDOWN:
            ps.keyin(event.key) 
    pygame.display.flip() 
    ps.statemanager()
    time.sleep(0.05)


