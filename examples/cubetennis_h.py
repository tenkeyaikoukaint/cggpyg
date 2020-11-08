import pygame
import random
from systennis import CGGPYG 
import time
from cggframe import cggframe

class cubetennis(cggframe):

    def __init__(self):

        self.cgg=CGGPYG("")
        self.bx=200
        self.by=400
        self.bz=200
        self.dx=10
        self.dy=10
        self.dz=10
        self.mx=4
        self.sc=0
        self.gamestate="title"
        self.ct=0
        pygame.mixer.init()
        self.click=pygame.mixer.Sound("pin-fa.wav")
        self.beep=pygame.mixer.Sound("po.wav")

    def trans(self,a,b):

        val=float(a)
        z=float(b) 
        return int(val/z*100+(500-50000/z)/2)

    def keyin(self,key):

        if self.gamestate=="title":
            if key==pygame.K_RETURN:
                self.gamestate="play"
        if self.gamestate=="play":
            pass
        if self.gamestate=="gameover":
           if key==pygame.K_RETURN:
                self.__init__()
                self.gamestate="title" 


    def title(self):

        self.cgg.cls()
        self.cgg.setcolor(7)
        self.cgg.printc("cubetennis",5,5)
        self.cgg.printc("2018 tenkey aikoukai",5,7)
        self.cgg.printc("press ret key",5,9)
        pygame.display.flip()

    def gameover(self):

        self.cgg.setcolor(2)
        self.cgg.printc("game over",11,10)

    def routine(self):

        self.ct=self.ct+1
        if self.ct>=5:
            self.update()
            self.ct=0
        self.draw()

    def update(self):

        if self.dx<0 and self.bx<=0:
            self.dx=-self.dx
        if self.dx>0 and self.bx>=400:
            self.dx=-self.dx
        if self.dy<0 and self.by<=0:
            self.dy=-self.dy
        if self.dy>0 and self.by>=400:
            self.dy=-self.dy
            self.click.play()
        pygame.display.flip()
        if self.dz<0 and self.bz<250:
            mx,my = pygame.mouse.get_pos()
            tbx1=self.trans(self.bx,self.bz)
            tby1=self.trans(self.by,self.bz)
            tbx2=self.trans(self.bx+100,self.bz)
            tby2=self.trans(self.by+100,self.bz)
            if mx>tbx1 and mx<tbx2 and my>tby1 and my<tby2:
                self.sc=self.sc+1
                self.dz=-self.dz
                self.click.play()
                pygame.display.flip()
                """self.beep.play()"""
            elif self.bz<50:
                self.gamestate="gameover"
                self.dz=-self.dz
        if self.dz>0 and self.bz>500:
            self.dz=-self.dz
            self.click.play()
            pygame.display.flip()
        self.bx=self.bx+self.dx
        self.by=self.by+self.dy
        self.bz=self.bz+self.dz
        self.draw()

    def draw(self):

        self.cgg.cls()
        self.cgg.setcolor(1)
        self.cgg.line(300,300,500,500)
        self.cgg.line(200,300,0,500)
        self.cgg.line(200,300,300,300)
        self.cgg.line(0,500,500,500)
        for i in range(1,5):
            self.cgg.line(200+i*20,300,100*i,500)
        for i in range(1,15):
            if i==9:
                self.cgg.setcolor(7)
            else:
                self.cgg.setcolor(1)
            lx1=self.trans(0,i*30)
            lx2=self.trans(500,i*30)
            ly=self.trans(500,i*30)
            self.cgg.line(lx1,ly,lx2,ly)
        self.cgg.setcolor(5)
        x1=self.trans(self.bx,self.bz)
        y1=self.trans(self.by,self.bz)
        x2=self.trans(self.bx+100,self.bz)
        y2=self.trans(self.by+100,self.bz)
        x3=self.trans(self.bx,self.bz-20)
        x4=self.trans(self.bx+100,self.bz-20)
        y3=self.trans(self.by,self.bz-20)
        y4=self.trans(self.by+100,self.bz-20)

        self.cgg.line(x1,y1,x2,y1)
        self.cgg.line(x2,y1,x2,y2)
        self.cgg.line(x2,y2,x1,y2)
        self.cgg.line(x1,y2,x1,y1)

        self.cgg.line(x3,y3,x4,y3)
        self.cgg.line(x4,y3,x4,y4)
        self.cgg.line(x4,y4,x3,y4)
        self.cgg.line(x3,y4,x3,y3)

        self.cgg.line(x1,y1,x3,y3)
        self.cgg.line(x2,y1,x4,y3)
        self.cgg.line(x1,y2,x3,y4)
        self.cgg.line(x2,y2,x4,y4)
        """
        if self.bz>=300:
            pygame.draw.rect(self.cgg.cvs,(0,0,0),(x1+1,y1+1,(x2-x1)-1,(y2-y1)-1))
        self.cgg.setcolor(7)
        """
        self.cgg.setcolor(7)
        self.cgg.printc("score "+str(self.sc),1,1)

cube=cubetennis()
cube.main(0.002)








