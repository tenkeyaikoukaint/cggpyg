import pygame
from syslcd4l import CGGPYG
import time

class displaymanager():

    def __init__(self):

        self.counter=0
        self.cmdstr="command:"
        self.str=["","","",""]
        self.cgg=CGGPYG()
        self.cmdflag=False
        self.inputflag=False

    def reset(self):

        self.counter=0

    def printstr(self,str,y):

        self.str[y]=str

    def inputmode(self,str):

        if self.inputflag==False and str=="on":
            self.inputflag=True
        if self.inputflag and str=="off":
            self.inputflag=False

    def inputc(self,key):

        self.cmdstr="command:"+str(key)
        self.draw()
        self.reset()
        self.cmdflag=True

    def draw(self):

        self.cgg.cls()
        self.cgg.setcolor(7)
        for i in range(0,3):
            self.cgg.printc(self.str[i],0,i)
        if self.inputflag:
            self.cgg.printc(self.cmdstr,0,3)

    def tick(self):

        self.counter=self.counter+1
        if self.cmdflag:
            if self.counter>=20:
                self.cmdstr="command:"
                self.cmdflag=False



