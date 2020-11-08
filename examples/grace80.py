import pygame
from syslogic import CGGPYG
import time
import random

class Grace80():

    def __init__(self):

        self.cgg=CGGPYG("")
        pygame.mixer.init()
        self.bgm=pygame.mixer.Sound("pin-fa.wav")
        self.beep=pygame.mixer.Sound("po.wav")
        self.curx=20
        self.cury=80
        self.num=50
        self.ct=0
        self.m=[0,0]
        self.gameflag=0
        for i in range(0,21):
            for j in range(0,41):
                self.m[len(self.m):] = [0] 
        self.gamestate="title"
        self.msg=""
        self.sc = 0 
        self.x = 10
        self.y = 18
        self.counter=0
        self.chaincounter=0
        self.chainflag=0
        self.k=1
        self.m[self.y*40+self.x] = 3

    def statemanager(self):

        if self.gamestate=="title":
            self.title()
        if self.gamestate=="play":
            self.routine()
        if self.gamestate=="gameover":
            self.gameover()

    def title(self):

        self.cgg.cls()
        self.cgg.setcolor(7)
        self.cgg.printc("lost and found the action game",5,5)
        self.cgg.printc("2018 tenkey aikoukai",5,7)
        self.cgg.printc("press ret key",5,9)

    def gameover(self):

        self.cgg.setcolor(2)
        self.cgg.printc("game over",15,10)

    def keyin(self,key):

        if self.gamestate=="title":
            if key==pygame.K_RETURN:
                self.gamestate="play"
        if self.gamestate=="play":
            if key==pygame.K_LEFT and self.x >= 1:
                self.x = self.x - 1 
            if key==pygame.K_RIGHT and self.x < 39:
                self.x = self.x + 1 
        if self.gamestate=="gameover":
            if key==pygame.K_RETURN:
                self.__init__()
                self.gamestate="title"

    def draw(self):

        self.cgg.cls()
        for i in range(0,19):
            for j in range(0,39):
                if self.m[i*40+j]==1:
                    self.cgg.setcolor(4)
                    self.cgg.puth("sharp",j,i)
                if self.m[i*40+j]==2:
                    self.cgg.setcolor(6)
                    self.cgg.puth("circle",j,i)
                if self.m[i*40+j]==3:
                    self.cgg.setcolor(7)
                    self.cgg.puth("a",j,i)
        self.cgg.setcolor(7)
        self.cgg.printc("score "+str(self.sc),2,20)
        self.cgg.printc(self.msg,2,21)

    def scroll(self):

        """scroll screen"""

        for i in range(18,0,-1):
            for j in range(0,40):
                self.m[(i+1)*40+j] = self.m[i*40+j]

        """enemy generate"""

        for i in range(0,39):
            r = random.randint(1,20)
            if r == 1:
                self.m[40+i] = 1
            else:
                self.m[40+i] = 0

        """coin generate"""

        if self.counter==20:
            r = random.randint(0,40)
            self.m[40+r] = 2

        """collide check"""

        if self.m[self.y*40+self.x] == 1:
            self.cgg.printc("GAME OVER",2,20)
            self.gamestate="gameover"

        """collide with coin"""

        if self.m[self.y*40+self.x]==2 and self.chaincounter<=1:
            self.msg="get"
            self.sc=self.sc+100
            self.beep.play()
            self.counter=0
            self.chainflag=1
            self.chaincounter=self.chaincounter+1

        """chain check"""

        if self.m[self.y*40+self.x]==2 and self.chaincounter>=2:
            self.msg=str(self.chaincounter)+" chain"
            self.sc=self.sc+100*self.chaincounter
            self.chainflag=1
            self.chaincounter=self.chaincounter+1
            self.beep.play()
            self.counter=0

        """draw myself"""

        if self.m[self.y*40+self.x]!=1 and self.m[self.y*40+self.x]!=2:
            self.m[self.y*40+self.x] = 3

        self.draw() 
        self.sc=self.sc+1
        self.counter=self.counter+1
        self.cgg.setcolor(7)

        """counter caliculate"""

        if self.counter==25 and self.chainflag==0:
            self.chaincounter=0
            self.counter=0
        if self.counter==25 and self.chainflag==1:
            self.chainflag=0
            self.counter=0
        self.bgm.stop()
        self.bgm.play()
        self.draw()

    def routine(self):

        if self.gameflag==0:
            self.ct=self.ct+1
            if self.ct>=10:
                self.ct=0
                self.scroll()

gr=Grace80()
gameflag=0
endflag=0
while endflag==0:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:endflag=1
        if event.type==pygame.KEYDOWN:
            gr.keyin(event.key) 
    pygame.display.flip() 
    gr.statemanager()
    time.sleep(0.006)


