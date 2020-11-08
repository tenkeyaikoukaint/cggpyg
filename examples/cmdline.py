"""SWAC(Single-Window Application Component)"""
"""apply to adventure game, RPG, simulation game"""
"""text screen manager"""

import pygame
import time
from syskana import CGGPYG
from cggframe import cggframe
import os
import subprocess as sub
import datetime

class cmdline:

    def cmdexe(self,cmd,gs):
        if cmd=="ls":
            stg1=str(os.listdir(os.getcwd()))
            gs.slicestg(stg1)
        if cmd=="path":
            stg=str(os.path.abspath("."))
            gs.addstg(stg)
        if cmd=="time":
            stg=str(datetime.datetime.now().strftime("%H:%M:%S"))
            gs.addstg(stg)
        if cmd=="date":
            stg=str(datetime.datetime.now().strftime("%Y/%m/%d"))
            gs.addstg(stg)
        """
        else:
            sub.call([cmd])
        """

class txtscrm:

    def __init__(self,cgg):
        self.cgg=cgg
        self.sc=cmdline()
        self.scr=["","","","","","","","","","","","","","",""
                  "","","","","","","","","","","","","","","",""]
        self.cmd=""

    def slicestg(self,stg):
        self.addstg(stg[0:40])
        if len(stg)>40:
            self.slicestg(stg[40:len(stg)])

    def getcmd(self):
        cmd=self.cmd
        self.cmd=""
        return cmd

    def addcmd(self,chr):
        if chr!="ret" and chr!="":
            if chr=="bs":
                if len(self.cmd)>0:
                    self.cmd=self.cmd[0:len(self.cmd)-1]
                    self.scr[23]=self.scr[23][0:len(self.scr[23])-1]
            else:
                self.scr[23]=self.scr[23]+str(chr)
                self.cmd=self.cmd+chr
        self.cgg.cls()
        self.cgg.setcolor(7)
        for i in range(0,24):
            if i==23:
                self.cgg.printc(self.scr[i]+"_",0,i)
            else:
                self.cgg.printc(self.scr[i],0,i)
        pygame.display.flip()

    def addstg(self,stg):
        for i in range(1,24):
            self.scr[i-1]=self.scr[i]
        self.scr[23]=stg
        time.sleep(0.01)
        self.cgg.cls()
        self.cgg.setcolor(7)
        for i in range(0,24):
            self.cgg.printc(self.scr[i],0,i)
        pygame.display.flip()

class controller(cggframe):

    def __init__(self):
        self.cgg=CGGPYG("")
        self.gamestate="play"
        self.advm=txtscrm(self.cgg)
        self.advm.addstg("cggpyg command line")
        self.advm.addstg("2020 tenkey aikoukai")
        self.advm.addstg("")
        self.advm.addstg("command:")
        self.advm.addcmd("")

    def keyin(self,key):
        if self.gamestate=="title" and key==pygame.K_RETURN:
            self.gamestate="play"
        if self.gamestate=="play":
            chr=""
            if key==pygame.K_k:
                chr="k"
            if key==pygame.K_l:
                chr="l"
            if key==pygame.K_r:
                chr="r"
            if key==pygame.K_s:
                chr="s"
            if key==pygame.K_m:
                chr="m"
            if key==pygame.K_g:
                chr="g"
            if key==pygame.K_o:
                chr="o"
            if key==pygame.K_p:
                chr="p"
            if key==pygame.K_q:
                chr="q"
            if key==pygame.K_e:
                chr="e"
            if key==pygame.K_f:
                chr="f"
            if key==pygame.K_a:
                chr="a"
            if key==pygame.K_b:
                chr="b"
            if key==pygame.K_c:
                chr="c"
            if key==pygame.K_d:
                chr="d"
            if key==pygame.K_t:
                chr="t"
            if key==pygame.K_n:
                chr="n"
            if key==pygame.K_r:
                chr="r"
            if key==pygame.K_h:
                chr="h"
            if key==pygame.K_i:
                chr="i"
            if key==pygame.K_j:
                chr="j"
            if key==pygame.K_v:
                chr="v"
            if key==pygame.K_w:
                chr="w"
            if key==pygame.K_x:
                chr="x"
            if key==pygame.K_y:
                chr="y"
            if key==pygame.K_z:
                chr="z"
            if key==pygame.K_u:
                chr="u"
            if key==pygame.K_SPACE:
                chr=" "
            if key==pygame.K_BACKSPACE:
                chr="bs"
            if key==pygame.K_RETURN:
                chr="ret"
                cmd=self.advm.getcmd()
                gs=self.advm.sc.cmdexe(cmd,self.advm)
                self.advm.addstg("command:")
            self.advm.addcmd(chr)
        if self.gamestate=="gameover" and key==pygame.K_RETURN:
            self.__init__()
            self.gamestate="play" 

    def gameover(self):
        pass

    def routine(self):
        pass

ctrl=controller()
ctrl.main(0.01)

