"""SWAC(Single-Window Application Component)"""
"""apply to adventure game, RPG, simulation game"""
"""text screen manager"""

import pygame
import time
from syslcd4l import CGGPYG
from cggframe import cggframe

class txtscrm:

    def __init__(self,cgg):
        self.cgg=cgg
        self.sc=sc_start()
        self.scr=["","","","","","","","","","","","","","",""
                  "","","","","","","","","","","","","","","",""]
        self.flag={'key':'hidden','door':'locked'}
        self.cmd=""
        self.gameflag=True
        self.textcolor=5

    def getcmd(self):
        cmd=self.cmd
        self.cmd=""
        return cmd

    def addcmd(self,chr):
        if chr!="ret" and chr!="":
            if chr=="bs":
                if len(self.cmd)>0:
                    self.cmd=self.cmd[0:len(self.cmd)-1]
                    self.scr[3]=self.scr[3][0:len(self.scr[3])-1]
            else:
                self.scr[3]=self.scr[3]+str(chr)
                self.cmd=self.cmd+chr
        self.cgg.cls()
        self.cgg.setcolor(self.textcolor)
        for i in range(0,4):
            if i==3:
                self.cgg.printc(self.scr[i]+"_",0,i)
            else:
                self.cgg.printc(self.scr[i],0,i)
        pygame.display.flip()

    def addstg(self,stg):
        for i in range(1,4):
            self.scr[i-1]=self.scr[i]
        self.scr[3]=stg
        time.sleep(0.01)
        self.cgg.cls()
        self.cgg.setcolor(self.textcolor)
        for i in range(0,4):
            self.cgg.printc(self.scr[i],0,i)
        pygame.display.flip()

class scene:

    def initmsg(self):
        pass

    def cmdexe(self,cmd):
        pass

    def cmd_common(self,cmd,gs):
        if cmd=="inventory" or cmd=="inv" or cmd=="i":
            gs.addstg("inventory:")
            if gs.flag['key']=='get':
                gs.addstg("key")
            else:
                gs.addstg("nothing")
        elif cmd=="help":
            gs.addstg("commands you can use:")
            gs.addstg("get enter move unlock open")
        else:
            self.cmdexe(cmd,gs)
        return gs

class sc_start(scene):

    def initmsg(self,gs):
        gs.addstg("start:you are on the road")

    def cmdexe(self,cmd,gs):
        if cmd=="look":
            gs.addstg("there is a house")
        elif cmd=="get":
            gs.addstg("you can not get anything")
        elif cmd=="search":
            gs.addstg("you can not find anything")
        elif cmd=="look house":
            gs.addstg("it seems old")
        elif cmd=="move house":
            gs.addstg("you can not move it")
        elif cmd=="enter house":
            gs.addstg("you enter the door")
            gs.sc=sc_entrance()
        else:
            gs.addstg("invalid input")
        return gs

class sc_entrance(scene):

    def initmsg(self,gs):
        gs.addstg("you are in the entrance hall")

    def cmdexe(self,cmd,gs):
        if cmd=="look":
            gs.addstg("there are a picture and a door")
            if gs.flag['key']=='appear':
                gs.addstg("there is a key")
        elif cmd=="look picture":
            gs.addstg("it is portrait of a lady")
        elif cmd=="move picture":
            gs.addstg("you found a key")
            gs.flag['key']='appear'
        elif cmd=="get key":
            gs.addstg("you got a key")
            gs.flag['key']='get'
        elif cmd=="unlock door":
            if gs.flag['key']=='get':
                gs.addstg("you unlock the door")
                gs.flag['door']='unlocked'
            else:
                gs.addstg("you do not have keys")
        elif cmd=="open door":
            if gs.flag['door']=='unlocked':
                gs.addstg("you open the door")
                gs.flag['door']='open'
            elif gs.flag['door']=='locked':
                gs.addstg("the door is locked")
            else:
                gs.addstg("it already opened")
        elif cmd=="enter door":
            if gs.flag['door']=='open':
                gs.addstg("you go through it")
                gs.sc=sc_dining()
            else:
                gs.addstg("it is closed")
        else:
            gs.addstg("invalid input")
        return gs

class sc_dining(scene):

    def initmsg(self,gs):
        gs.addstg("you are in the dining room")

    def cmdexe(self,cmd,gs):
        if cmd=="look":
            gs.addstg("there are a lady and a table")
        elif cmd=="look lady":
            gs.addstg("a beautiful lady")
        elif cmd=="look table":
            gs.addstg("a luxury table")
        elif cmd=="talk lady":
            gs.addstg("welcome adventurer")
            gs.addstg("shall we have tea")
            gs.addstg("**game end**")
            gs.addstg("hit ret to replay")
            gs.gameflag=False
        else:
            gs.addstg("invalid input")
        return gs

class spadv(cggframe):

    def __init__(self):
        self.cgg=CGGPYG()
        self.gamestate="play"
        self.advm=txtscrm(self.cgg)
        self.advm.addstg("python simplest adventure")
        self.advm.sc.initmsg(self.advm)
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
                gs=self.advm.sc.cmd_common(cmd,self.advm)
                if self.advm.gameflag==False:
                    self.gamestate="gameover"
                else:
                    self.advm.sc.initmsg(self.advm)
                    self.advm.addstg("command:")
            self.advm.addcmd(chr)
        elif self.gamestate=="gameover" and key==pygame.K_RETURN:
            self.__init__()
            self.gamestate="play" 

    def gameover(self):
        pass

    def routine(self):
        pass

adv=spadv()
adv.main(0.01)

