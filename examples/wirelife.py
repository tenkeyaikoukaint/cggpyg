import time
import random
import pygame
from syslogic import CGGPYG
from cggframe import cggframe

class wirelife(cggframe):

    def __init__(self):

        self.ct=0
        self.mtx=[]
        self.mtx2=[]
        self.cgg=CGGPYG("")
        for i in range(0,40):
            for j in range(0,80):
                self.mtx[len(self.mtx):]=[random.randint(0,1)]
                self.mtx2[len(self.mtx2):]=[0]
        self.gamestate="play"

    def readmtx(self,x,y):

        return self.mtx[y*80+x]

    def routine(self):

        for i in range(1,39):
            for j in range(1,79):
                ct=0
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                       if (k-i)==0 and (l-j)==0:
                           dummy=0
                       else:
                           ct=ct+self.readmtx(l,k) 
                if (ct==2 or ct==3) and self.readmtx(j,i)==1 or ct==3 and self.readmtx(j,i)==0:
                    self.mtx2[i*80+j]=1
                else:
                    self.mtx2[i*80+j]=0 
        for i in range(0,3200):
            self.mtx[i]=self.mtx2[i]
        self.draw()
        self.ct=self.ct+1

    def keyin(self,key):

        dummy=0

    def draw(self):

        self.cgg.cls()
        self.cgg.setcolor(5) 
        for i in range(1,39):
            for j in range(0,79):
                if self.mtx[i*80+j]==1:
                    for k in range(i-1,i+2):
                        for l in range(j-1,j+2):
                             if self.mtx[k*80+l]==1:
                                 self.cgg.line(j*8,i*8,l*8,k*8)

        self.cgg.setcolor(7)
        self.cgg.printc("time:"+str(self.ct),0,16)

life=wirelife()
life.main(0.5)
