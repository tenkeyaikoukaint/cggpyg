import pygame
import time
import random
from syssnake import CGGPYG

class NumberSnake:

    def __init__(self):
        self.mx=0
        self.my=0
        self.d=1
        self.mtx=[]
        self.currentnum=1
        self.sc=0
        self.gameflag=1
        self.gamestate="title"
        self.cgg=CGGPYG("")
        pygame.mixer.init()
        self.bgm=pygame.mixer.Sound("pin-re.wav")
        self.hit=pygame.mixer.Sound("po.wav")
        self.ct=0

        for i in range(0,21):
            for j in range(0,21):
                self.mtx[len(self.mtx):]=[0]
        for i in range(1,11):
            flag=0
            r1=0
            r2=0
            while(flag==0):
                r1=random.randint(1,17)
                r2=random.randint(1,17)

                """11-19:number 20:my address"""

                if(self.mtx[r2*20+r1]==0):
                    self.mtx[r2*20+r1]=10+i
                    flag=1
        self.mx=r1
        self.my=r2

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

        self.cgg.printc("number snake game",1,4)
        self.cgg.printc("the action game",2,6)

        self.cgg.printc("2018 tenkey aikoukai",0,8)

        self.cgg.printc("press ret key",3,10)


    def gameover(self):

        if self.gameflag==2:
            self.cgg.setcolor(2)

            self.cgg.printc("game over",6,10)
        if self.gameflag==3:
            self.cgg.setcolor(5)

            self.cgg.printc("game clear",5,10)
    def keyin(self,key):

        if self.gamestate=="title":

            if key==pygame.K_RETURN:

                self.gamestate="play"

        if self.gamestate=="play":

            if key==pygame.K_LEFT:
                self.d=4 
            if key==pygame.K_RIGHT:
                self.d=2 
            if key==pygame.K_UP:
                self.d=1 
            if key==pygame.K_DOWN:
                self.d=3 
        if self.gamestate=="gameover":

            if key==pygame.K_RETURN:

                self.__init__()

                self.gamestate="title"


 
    def draw(self):
        self.cgg.cls()
        for i in range(0,20):
            for j in range(0,20):
                if self.mtx[i*20+j]==1:
                    self.cgg.setcolor(4)
                    self.cgg.puth("circle",j,i)
                if self.mtx[i*20+j]==11:
                    self.cgg.setcolor(6)
                    self.cgg.puth("1",j,i)
                if self.mtx[i*20+j]==12:
                    self.cgg.setcolor(6)
                    self.cgg.puth("2",j,i)
                if self.mtx[i*20+j]==13:
                    self.cgg.setcolor(6)
                    self.cgg.puth("3",j,i)
                if self.mtx[i*20+j]==14:
                    self.cgg.setcolor(6)
                    self.cgg.puth("4",j,i)
                if self.mtx[i*20+j]==15:
                    self.cgg.setcolor(6)
                    self.cgg.puth("5",j,i)
                if self.mtx[i*20+j]==16:
                    self.cgg.setcolor(6)
                    self.cgg.puth("6",j,i)
                if self.mtx[i*20+j]==17:
                    self.cgg.setcolor(6)
                    self.cgg.puth("7",j,i)
                if self.mtx[i*20+j]==18:
                    self.cgg.setcolor(6)
                    self.cgg.puth("8",j,i)
                if self.mtx[i*20+j]==19:
                    self.cgg.setcolor(6)
                    self.cgg.puth("9",j,i)
                if i==self.my and j==self.mx:
                    self.cgg.setcolor(7)
                    self.cgg.puth("circle",j,i)
        self.cgg.setcolor(7)
        self.cgg.line(320,0,320,400)
        self.cgg.line(0,400,320,400)
        self.cgg.setcolor(7)

    def routine(self):

        self.ct=self.ct+1
        if self.ct>=10:
            self.update()
            self.ct=0

    def update(self):

        self.mtx[self.my*20+self.mx]=1

        """up:1 and clockwise"""

        if self.d==1:
            self.my=self.my-1
        if self.d==2:
            self.mx=self.mx+1
        if self.d==3:
            self.my=self.my+1
        if self.d==4:
            self.mx=self.mx-1
        self.bgm.stop()
        self.bgm.play()
        self.draw()
        if self.mtx[self.my*20+self.mx]>10 and self.mtx[self.my*20+self.mx]!=self.currentnum+10 or self.mtx[self.my*20+self.mx]==1 or self.mx<0 or self.mx>19 or self.my<0 or self.my>19:
            self.gameflag=2
            self.gamestate="gameover"

        if self.mtx[self.my*20+self.mx]==self.currentnum+10:
            self.hit.play()
            pygame.display.flip()
            self.sc=self.sc+1
            self.currentnum=self.currentnum+1
        if self.currentnum>=10:
            self.gamestate="gameover"
            self.gameflag=3

ns=NumberSnake()
gameflag=0

endflag=0
while endflag==0:
    ns.statemanager()
    pygame.display.flip() 
    for i in range(0,5):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:endflag=1
            if event.type==pygame.KEYDOWN:

                ns.keyin(event.key)
        time.sleep(0.01)

