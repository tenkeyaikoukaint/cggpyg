"""SWAP(Single-Window Application Component)"""
"""apply to adventure game, RPG, simulation game"""

import pygame
import time
from syslcdk import CGGPYG
from cggframe import cggframe

class advmanager:

    def __init__(self,cgg):
        self.scr=["","","","","","","","","","","","","","",""
                  "","","","","","","","","","","","",""]
        self.ct=0
        self.cgg=cgg

    def addcmd(self,stg):
        self.scr[3]=self.scr[3]+stg
        self.cgg.cls()
        self.cgg.setcolor(5)
        for i in range(0,4):
            self.cgg.printk(self.scr[i],0,i)
        pygame.display.flip()
        time.sleep(0.3)

    def addstg(self,stg):
        for i in range(1,4):
            self.scr[i-1]=self.scr[i]
        self.scr[3]=stg
        time.sleep(0.01)
        self.cgg.cls()
        self.cgg.setcolor(5)
        for i in range(0,4):
            self.cgg.printk(self.scr[i],0,i)
        pygame.display.flip()

class book:

    def initmsg(self,gs):
        if gs.ct==0:
            gs.addstg("")
            gs.addstg("katakana  todtxuwa")
        if gs.ct==1:
            gs.addstg("")
        if gs.ct==2:
            gs.addstg("xaxinn  ha  mori  no  naka  ni  xita")
        if gs.ct==3:
            gs.addstg("xaxinn  ha  mori  wo  xaruku")
        if gs.ct==4:
            gs.addstg("xaxinn  ha  notodt  kadt  kawaxita")
        if gs.ct==5:
            gs.addstg("xaxinn  ha  xisudtmi  wo  mituketa")
        if gs.ct==6:
            gs.addstg("xaxinn  ha  kawaki  wo  xiyasita")
        if gs.ct==7:
            gs.addstg("xaxinn  ha  todtxukutu  wo  mituketa")
        if gs.ct==8:
            gs.addstg("xaxinn  ha  todtxukutu  ni  haxittteyuku")
        if gs.ct==9:
            gs.addstg("hikaru  kenn  wo  mituketa")
        if gs.ct==10:
            gs.addstg("xaxinn  ha  todtxukutu  wo  tedtta")
        if gs.ct==11:
            gs.addstg("xaxinn  ha  taxoretexiru  sidtyosexi  wo  mituketa")
        if gs.ct==12:
            gs.addstg("xaxinn  ha  sidtyosexi  wo  tasuketa")
        if gs.ct==13:
            gs.addstg("xaxinn  ha  maxoxu  no  xihadtsiyo  wo  sittta")
        if gs.ct==14:
            gs.addstg("xaxinn  ha  koxori  no  yama  wo  mesadtsita")
        if gs.ct==15:
            gs.addstg("xaxinn  ha  maxoxu  wo  taxosita")
        gs.ct=gs.ct+1
        return gs

class cggbook(cggframe):

    def __init__(self):
        self.cgg=CGGPYG()
        self.bk=book()
        self.advm=advmanager(self.cgg)
        self.gamestate="play"
        self.cgg.cls()
        self.advm.addstg("eheiet  ereeeteueren  ekeeey  eteo  esecereoelel")

    def keyin(self,key):
        if self.gamestate=="title" and key==pygame.K_RETURN:
            self.gamestate="play"
        if self.gamestate=="play":
            if key==pygame.K_RETURN:
                self.advm=self.bk.initmsg(self.advm)
        if self.gamestate=="gameover" and key==pygame.K_RETURN:
            self.__init__()
            self.gamestate="play" 

    def gameover(self):
        pass

    def routine(self):
        pass

cb=cggbook()
cb.main(0.01)

