"""extended-helmet an action RPG"""

import pygame
import random
import time
from syslogic import CGGPYG
from cggframe import cggframe

class exhelm(cggframe):

    def __init__(self):

        self.cgg=CGGPYG("")
        pygame.mixer.init()
        self.bgm=pygame.mixer.Sound("powa.wav")
        self.click=pygame.mixer.Sound("pin-re.wav")
        self.beep=pygame.mixer.Sound("pin-do.wav")
        self.m=[]
        for i in range(0,21):
            for j in range(0,41):
                self.m[len(self.m):] = [0]
        self.mx=0
        self.my=16
        self.sc=0
        self.goal="right"
        self.gamestate="play"
        self.miss=0
        self.ct=0
        self.level=5

    def keyin(self,key):

        if self.gamestate=="title" and key==pygame.K_RETURN:
            self.gamestate="play"
        if self.gamestate=="play":
            if key==pygame.K_RIGHT and self.mx<19:
                self.mx=self.mx+1
            if key==pygame.K_LEFT and self.mx>0:
                self.mx=self.mx-1
        if self.gamestate=="gameover" and key==pygame.K_RETURN:
            self.__init__()
            self.gamestate="play" 

    def draw(self):

        self.cgg.cls()
        """draw raindrops"""
        self.cgg.setcolor(5)
        for i in range(0,16):
            for j in range(1,19):
                if self.m[i*20+j]==1:
                    self.cgg.put("point",j,i)
        """draw floor of start and goal"""
        self.cgg.setcolor(6)
        self.cgg.put("fill",0,17)
        self.cgg.put("fill",19,17)
        """draw roof"""
        self.cgg.setcolor(2)
        self.cgg.put("sw",0,14)
        self.cgg.put("se",19,14)
        """draw road"""
        self.cgg.setcolor(4)
        for i in range(1,19):
            self.cgg.put("fill",i,17)
        """draw load"""
        if self.my<20:
            if self.goal=="right":
                self.cgg.setcolor(1)
                self.cgg.put("brick",self.mx,self.my-1)
            """draw player chr"""
            self.cgg.setcolor(7)
            self.cgg.put("spade",self.mx,self.my)
        """score display"""
        self.cgg.printc("score:"+str(self.sc)+" miss:"+str(self.miss),0,20) 
    def gameover(self):

        self.cgg.setcolor(2)
        self.cgg.printc("game over",15,10)

    def scroll(self):

        self.click.stop()
        self.click.play()
        pygame.display.flip()
        self.m[10*20]=1
        self.m[10*20+19]=1
        for i in range(0,19):
            r = random.randint(1,10)
            self.m[i] = 0
            if r == 1:
                self.m[i] = 1
        for i in range(16,-1,-1):
            for j in range(1,19):
                self.m[(i+1)*20+j] = self.m[i*20+j] 
        if self.m[(self.my-1)*20+self.mx]==1:
            self.miss=self.miss+1
            self.beep.play()
            if self.miss>=3:
                self.gamestate="gameover"
        if self.mx==19 and self.goal=="right":
            self.sc=self.sc+1
            self.bgm.play()
            pygame.display.flip()
            self.goal="left"
        if self.mx==0 and self.goal=="left":
            self.sc=self.sc+1
            self.bgm.play()
            pygame.display.flip()
            if self.sc%20==0 and self.level<7:
                self.level=self.level+1
            self.goal="right"
        self.draw()


    def routine(self):

        self.ct=self.ct+1
        if self.ct>=10-self.level:
            self.ct=0
            self.scroll()
        self.draw()

eh=exhelm()
eh.main(0.01)

