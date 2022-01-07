import pygame
import random
from syslogic import CGGPYG
from cggframe import cggframe
import time

pxmtx=[4,9,14]
rmtx=[4,3,2,4,3,2,3,2,2,3,2,2,2,2,2,2,2,2]

class fruits(cggframe):

    def __init__(self):
        self.cgg=CGGPYG("")
        pygame.mixer.init()
        self.gamestate="title"
        self.click=pygame.mixer.Sound("click.wav")
        self.hit=pygame.mixer.Sound("po.wav")
        self.misssound=pygame.mixer.Sound("pin-do.wav")
        self.fruit=[0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,
                    0,0,0]
        self.frame=0
        self.rnum=0
        self.px=pxmtx[2]
        self.mx=2
        self.sc=0
        self.ct=0
        self.ct2=0
        self.miss=0
        self.rseed=6

    def puttree(self,x,y,leg):
        self.cgg.setcolor(4)
        self.cgg.put("se",x+1,y)
        self.cgg.put("fill",x+2,y)
        self.cgg.put("sw",x+3,y)
        self.cgg.put("se",x+1,y+1)
        self.cgg.put("fill",x+2,y+1)
        self.cgg.put("sw",x+3,y+1)
        self.cgg.put("se",x,y+2)
        self.cgg.put("fill",x+1,y+2)
        self.cgg.put("fill",x+2,y+2)
        self.cgg.put("fill",x+3,y+2)
        self.cgg.put("sw",x+4,y+2)
        self.cgg.setcolor(2)
        for i in range(1,leg+1):
            self.cgg.put("fill",x+2,y+3+i-1)

    def update(self):
        if self.ct2==0:
            self.fruitset()
        self.click.play()
        self.ct=self.ct+1
        if self.ct>=3 and self.ct2==0:
            self.ct2=1
            self.ct=0
        elif self.ct>=3 and self.ct2>=1:
            self.ct=0
            self.ct2=0
        if self.fruit[24+self.ct]>0 and self.mx==self.ct:
            self.hit.play()
            self.draw()
            time.sleep(0.02)
            self.fruit[24+self.ct]=0
            self.sc=self.sc+1
            if self.sc%20==0 or self.sc%80==0 or (self.sc>=100 and self.sc%100==0):
                self.rnum=self.rnum+1
                self.rseed=rmtx[self.rnum];
                if self.rnum==17:
                    self.rnum=14
        for i in range(9,-1,-1):
            self.fruit[(i+1)*3+self.ct]=self.fruit[i*3+self.ct]
        self.fruit[self.ct]=0
        self.draw()
        if self.fruit[24+self.ct]>0 and self.mx==self.ct:
            self.hit.play()
            self.draw()
            time.sleep(0.02)
            self.fruit[24+self.ct]=0
            self.sc=self.sc+1
            if self.sc%20==0 or self.sc%80==0 or (self.sc>=100 and self.sc%100==0):
                self.rnum=self.rnum+1
                self.rseed=rmtx[self.rnum];
                if self.rnum==17:
                    self.rnum=14
        if self.fruit[27+self.ct]>0:
            self.miss=self.miss+1
            self.misssound.play()
            if self.miss>=3:
                self.gamestate="gameover"
                self.cgg.put("heart",pxmtx[self.ct%3],17)
        self.draw()

    def draw(self):
        self.cgg.cls()
        self.fruitdraw()
        self.puttrees()
        self.cgg.setcolor(6)
        self.cgg.put("v",pxmtx[self.mx],14)
        self.cgg.setcolor(7)
        self.cgg.put("s",1,19)
        self.cgg.put("c",2,19)
        self.cgg.put("o",3,19)
        self.cgg.put("r",4,19)
        self.cgg.put("e",5,19)
        self.putscore()
        if self.miss>=1:
            self.drawmiss()
        pygame.display.flip()

    def title(self):
        self.cgg.cls()
        self.cgg.setcolor(7)
        self.cgg.printc("fruits in the forest",5,5)
        self.cgg.printc("2021 tenkey aikoukai",5,7)
        self.cgg.printc("press enter key",5,9)
        pygame.display.flip()

    def gameover(self):
        self.cgg.setcolor(2)
        self.cgg.printc("game over",15,6)

    def keyin(self,key):
        if self.gamestate=="title":
            if key==pygame.K_RETURN:
                self.gamestate="play"
        if self.gamestate=="play":
            if key==pygame.K_LEFT and self.mx>=1:
                self.mx=self.mx-1
            if key==pygame.K_RIGHT and self.mx<=1:
                self.mx=self.mx+1
            time.sleep(0.005)
            if self.fruit[24+self.ct]>0 and self.mx==self.ct:
                self.hit.play()
                self.fruit[24+self.ct]=0
                self.sc=self.sc+1
                if self.sc%20==0 or self.sc%80==0 or (self.sc>=100 and self.sc%100==0):
                    self.rnum=self.rnum+1
                    self.rseed=rmtx[self.rnum];
                    if self.rnum==17:
                        self.rnum=14
                self.draw()
                time.sleep(0.02)
            self.draw()
        if self.gamestate=="gameover":
           if key==pygame.K_RETURN:
                self.__init__()
                self.gamestate="title" 

    def routine(self):
        self.frame=self.frame+1
        if self.frame==10:
            self.update()
            self.frame=0
        self.draw()

    def putscore(self):
        modsc=self.sc%10
        self.putnumchr(modsc,9,19)
        cursc=int(self.sc/10)
        modsc=cursc%10
        self.putnumchr(modsc,8,19)
        cursc=int(cursc/10)
        modsc=cursc%10
        self.putnumchr(modsc,7,19)

    def putnumchr(self,num,x,y):
        self.cgg.setcolor(7)
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

    def puttrees(self):
        x=3
        y=3
        self.puttree(x,y,9)
        x=8
        y=5
        self.puttree(x,y,7)
        x=13
        y=7
        self.puttree(x,y,5)

    def fruitset(self):
        r=random.randint(0,self.rseed)
        if r==1:
            if self.ct==0:
                self.fruit[0]=1
            elif self.ct==1:
                self.fruit[4]=1
            else:
                self.fruit[11]=1

    def fruitdraw(self):
        self.cgg.setcolor(3)
        for i in range(0,31):
            py=int(i/3)+6
            if self.fruit[i]==1:
                self.cgg.put("heart",pxmtx[i%3],py)

    def drawmiss(self):
        self.cgg.setcolor(7)
        self.cgg.put("m",11,19)
        self.cgg.put("i",12,19)
        self.cgg.put("s",13,19)
        self.cgg.put("s",14,19)
        self.cgg.put("spade",16,19)
        if self.miss>=2:
            self.cgg.put("spade",17,19)
        if self.miss>=3:
            self.cgg.put("spade",18,19)

fr=fruits()
fr.main(0.01)
