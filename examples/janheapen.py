import random
import time
import pygame
from syslcd1l import CGGPYG
from cggframe import cggframe

class gamevals:

    def __init__(self):

        self.sc=0
        self.chr="r"
        self.emtx=["","","","","","","","","","","","","","","","","","","","",""]
        self.ex=20
        self.mx=0
        self.ct=0


class jantris(cggframe):

    def __init__(self):

        self.cgg=CGGPYG()
        pygame.mixer.init()
        self.hit=pygame.mixer.Sound("po.wav")
        self.bgm=pygame.mixer.Sound("pin-re.wav")
        self.gamestate="title"
        self.gv=gamevals()
        self.cgg.setcolor(7)

    def keyin(self,key):

        if self.gamestate=="title" and key==pygame.K_RETURN:
            self.gamestate="play"
        if self.gamestate=="play":
            if key==pygame.K_DOWN:
                if self.gv.chr=="r":
                    self.gv.chr="s"
                elif self.gv.chr=="s":
                    self.gv.chr="p"
                else:
                    self.gv.chr="r"
            if key==pygame.K_UP:
                if self.gv.chr=="p":
                    self.gv.chr="s"
                elif self.gv.chr=="s":
                    self.gv.chr="r"
                else:
                    self.gv.chr="p"
            if key==pygame.K_RIGHT:
                self.gv.mx=self.gv.mx+1
            self.draw()
            self.check()

        if self.gamestate=="gameover" and key==pygame.K_RETURN:
            self.gamestate="title"
            self.__init__()

    def title(self):

        self.cgg.cls()
        self.cgg.setcolor(7)
        self.cgg.printc("janheap hit ret key",0,0)

    def gameover(self):

        self.cgg.cls()
        self.cgg.setcolor(7)
        self.cgg.printc("score:"+str(self.gv.sc),0,0)

    def draw(self):

        self.cgg.cls()
        self.cgg.setcolor(7)
        self.cgg.puth(self.gv.chr,self.gv.mx,0)
        for i in range(self.gv.ex,20):
            self.cgg.puth(self.gv.emtx[i],i,0)

    def check(self):

        if self.gv.mx==self.gv.ex-1:
            h1=self.gv.chr
            h2=self.gv.emtx[self.gv.ex]
            if (h1=="r" and h2=="s") or (h1=="s" and h2=="p") or (h1=="p" and h2=="r"):
                self.gv.emtx[self.gv.ex]=""
                self.gv.ex=self.gv.ex+1
                self.gv.sc=self.gv.sc+1
                self.hit.play()
                pygame.display.flip()
            self.gv.mx=0

    def emove(self):

        self.gv.ex=self.gv.ex-1
        for i in range(self.gv.ex,20):
            self.gv.emtx[i]=self.gv.emtx[i+1]
        r=random.randint(0,2)
        if r==0:
            self.gv.emtx[19]="r"
        if r==1:
            self.gv.emtx[19]="s"
        if r==2:
            self.gv.emtx[19]="p"
        self.draw()
        if self.gv.ex<=0:
            self.gamestate="gameover"
        if self.gv.ex-1==self.gv.mx:
            self.check()
            self.draw()

    def routine(self):

        self.gv.ct=self.gv.ct+1
        if self.gv.sc<100:
            gap=21-int(self.gv.sc/10)
        else:
            gap=10
        if self.gv.ct>=gap:
            self.emove()
            self.gv.ct=0
            self.bgm.play()
        self.draw()

jt=jantris()
jt.main(0.05)
