"""extended-helmet an action RPG"""

import pygame
import random
import time
from syskana import CGGPYG
from cggframe import cggframe

class advmanager:

    def __init__(self,cgg):
        self.scr=["","","","","","","","","","","","","","",""
                  "","","","","","","","","","","","",""]
        self.sc=sc_start()
        self.cgg=cgg
        self.flag=[0,0,0,0,0]

    def addcmd(self,stg):
        self.scr[23]=self.scr[23]+stg
        self.cgg.cls()
        self.cgg.setcolor(5)
        for i in range(0,24):
            self.cgg.printk(self.scr[i],0,i)
        pygame.display.flip()
        time.sleep(0.3)

    def addstg(self,stg):
        for i in range(1,24):
            self.scr[i-1]=self.scr[i]
        self.scr[23]=stg
        time.sleep(0.01)
        self.cgg.cls()
        self.cgg.setcolor(5)
        for i in range(0,24):
            self.cgg.printk(self.scr[i],0,i)
        pygame.display.flip()

class scene:

    def initmsg(self):
        pass
    def cmdexe(self,cmd):
        pass

class sc_start(scene):

    def initmsg(self,gs):
        gs.addstg("sutahhtoe:")
        gs.addstg("xanata  ha  minato  ni  xiru")
        gs.addstg("eahhmiru  ebhhhune  ni  noru")

    def cmdexe(self,cmd,gs):
        if cmd=="a":
           gs.addstg("kita  ni  hune  kadt  mixeru")
        if cmd=="b":
           gs.addstg("hune  ni  notuta")
           gs.sc=sc_kanpan()
        return gs

class sc_kanpan:

    def initmsg(self,gs):
        gs.addstg("xanata  ha  hune  no  kannhaptnn  ni  ximasu")
        gs.addstg("eahhmiru  ebhhsoxutadtsitu  ni  haxiru")

    def cmdexe(self,cmd,gs):
        if cmd=="a":
            gs.addstg("soxutadtsitu  kadt  mixemasu")
        return gs

class cggtemp(cggframe):

    def __init__(self):
        self.cgg=CGGPYG("")
        self.stg=["","","","","","","","","",""]
        self.gamestate="play"
        self.gs=advmanager(self.cgg)
        self.gs.addstg("hoptnnhoptnnsenn  xatodthedtnntiyahh")
        self.gs.addstg("e2e0e2e0  eteeenekeeey  eaeiekeoeuekeaei")
        self.gs.addstg("")
        self.gs.sc.initmsg(self.gs)
        self.gs.addstg("eceoememeaenede:")

    def keyin(self,key):
        if self.gamestate=="title" and key==pygame.K_RETURN:
            self.gamestate="play"
        if self.gamestate=="play":
            cmd=""
            if key==pygame.K_a:
                cmd="a"
                self.gs.addcmd("ea")
            if key==pygame.K_b:
                cmd="b"
                self.gs.addcmd("eb")
            gs=self.gs.sc.cmdexe(cmd,self.gs)
            self.gs.sc.initmsg(self.gs)
            self.gs.addstg("eceoememeaenede:")
        if self.gamestate=="gameover" and key==pygame.K_RETURN:
            self.__init__()
            self.gamestate="play" 

    def gameover(self):
        self.cgg.setcolor(2)
        self.cgg.printc("game over",15,10)

    def routine(self):
        pass

ct=cggtemp()
ct.main(0.1)

