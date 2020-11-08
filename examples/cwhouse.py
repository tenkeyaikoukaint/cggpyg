
"""chie no wa house the adventure game"""

import pygame
import time
from syskanaf import CGGPYG
from cggframe import cggframe

class txtscrm:

    def __init__(self,cgg):
        self.cgg=cgg
        self.sc=sc_start()
        self.scr=["","","","","","","","","","","","","","",""
                  "","","","","","","","","","","","","","","",""]
        self.cmd=""
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
                    self.scr[25]=self.scr[25][0:len(self.scr[25])-2]
            else:
                self.scr[25]=self.scr[25]+str("e"+chr)
                self.cmd=self.cmd+chr
        self.cgg.cls()
        self.cgg.setcolor(self.textcolor)
        for i in range(10,26):
            if i==25:
                self.cgg.printk("                              "+self.scr[i]+"e_",0,i)
            else:
                self.cgg.printk("                              "+self.scr[i],0,i)
        pygame.display.flip()

    def addstg(self,stg):
        for i in range(1,26):
            self.scr[i-1]=self.scr[i]
        self.scr[25]=stg
        time.sleep(0.01)
        self.cgg.cls()
        self.cgg.setcolor(self.textcolor)
        for i in range(10,26):
            self.cgg.printk("                              "+self.scr[i],0,i)
        pygame.display.flip()

class scene:

    def initmsg(self):
        pass

    def cmdexe(self,cmd):
        pass

    def cmd_common(self,cmd,gs):
        if cmd=="inventory" or cmd=="inv" or cmd=="i":
            gs.addstg("motimonoe:")
        if cmd=="go north" or cmd=="n":
            cmd="north"
        if cmd=="go south" or cmd=="s":
            cmd="south"
        if cmd=="go east" or cmd=="e":
            cmd="east"
        if cmd=="go west" or cmd=="w":
            cmd="west"
        if cmd=="go up" or cmd=="u":
            cmd="up"
        if cmd=="go down" or cmd=="d":
            cmd="down"
        if cmd=="help":
            gs.addstg("siyoxu  kanoxu  komanntodt:")
            gs.addstg("eneoereteh  eseoeueteh  eeeaeset  eweeeset")
            gs.addstg("eleoeoek  egeeet  emeoevee  eseeeaereceh")
            gs.addstg("eeeneteeer") 
        self.cmdexe(cmd,gs)
        return gs

class sc_start(scene):

    def initmsg(self,gs):
        gs.addstg("sutahhtoe:")
        gs.addstg("xanata  ha  xixe  no  maxeniwa  ni  ximasu")

    def cmdexe(self,cmd,gs):
        if cmd=="look":
            gs.addstg("kita  ni  hidtrue(ebeueieledeienege)  kadt  mixemasu")
            gs.addstg("miti  kadt  toxusadtxi  ni  tutudtxiteximasu")
        if cmd=="get":
            gs.addstg("nani  mo  toremasenn")
        if cmd=="search":
            gs.addstg("nani  mo  mixatarimasenn")
        if cmd=="look building":
            gs.addstg("huruhodtketa  hidtru  tedtsu")
        if cmd=="move building":
            gs.addstg("xukodtkasemasenn")
        if cmd=="north":
            gs.addstg("monn  wo  haxirimasu")
            gs.sc=sc_frontyard()
        if cmd=="east":
            gs.addstg("hikadtsi  ni  susumimasu")
            gs.sc=sc_acrosscafe()
        if cmd=="west":
            gs.addstg("nisi  ni  xikimasu")
            gs.sc=sc_busstop()
        return gs

class sc_frontyard(scene):

    def initmsg(self,gs):
        gs.addstg("xanata  ha  hidtru  no  maxeniwa  ni  ximasu")

    def cmdexe(self,cmd,gs):
        if cmd=="look":
            gs.addstg("kita  ni  hidtru  no  xirikudtti  kadt  xarimasu")
            gs.addstg("minami  ni  hidtru  no  monne(egeaeteee)  kadt  xarimasu")
            gs.addstg("hikadtsi  ni  tiyuxusiyasidtyoxu  kadt  xarimasu")
        if cmd=="south":
            gs.addstg("monn  wo  tedtmasu")
            gs.sc=sc_start()
        if cmd=="north":
            gs.addstg("hidtru  no  xirikudtti  ni  mukaximasu")
            gs.sc=sc_transport()
        if cmd=="east":
            gs.addstg("hikadtsi  ni  susumimasu")
            gs.sc=sc_parking()
        return gs

class sc_acrosscafe(scene):

    def initmsg(self,gs):
        gs.addstg("xanata  ha  xoxutadtnnhotodtxu  no  maxe  ni  ximasu")

    def cmdexe(self,cmd,gs):
        if cmd=="look":
            gs.addstg("minami  no  xoxutadtnnhotodtxu  no  mukaxi  ni  kittsatenn  kadt  xarimasu")
            gs.addstg("hikadtsi  nisi  minami  ni  susumemasu")
        if cmd=="west":
            gs.addstg("nisi  ni  susumimasu")
            gs.sc=sc_start()
        if cmd=="south":
            gs.addstg("xoxutadtnnhotodtxu  wo  watarimasu")
            gs.sc=sc_frontcafe()
        return gs

class sc_frontcafe(scene):

    def initmsg(self,gs):
        gs.addstg("xanata  ha  kittsatenn  no  maxe  ni  ximasu")

    def cmdexe(self,cmd,gs):
        if cmd=="look":
            gs.addstg("minami  ni  kittsatenn  kadt  xarimasu")
            gs.addstg("kita  ni  xoxutadtnnhotodtxu  kadt  xarimasu")
        if cmd=="north":
            gs.addstg("xoxutadtnnhotodtxu  wo  watarimasu")
            gs.sc=sc_acrosscafe()
        return gs

class sc_cafe(scene):

    def initmsg(self,gs):
        gs.addstg("xanata  ha  kittsatenn  no  naka  ni  ximasu")

    def cmdexe(self,cmd,gs):
        return gs

class sc_parkfront(scene):

    def initmsg(self,gs):
        gs.addstg("xanata  ha  koxuxenn  no  maxe  ni  ximasu")

    def cmdexe(self,cmd,gs):
        return gs
       
class sc_park(scene):

    def initmsg(self,gs):
        gs.addstg("xanata  ha  koxuxenn  ni  ximasu")

    def cmdexe(self,cmd,gs):
        return gs

class sc_transport(scene):

    def initmsg(self,gs):
        gs.addstg("hidtru  no  hannniyuxu  suhepthhsu  tedtsu")

    def cmdexe(self,cmd,gs):
        if cmd=="look":
            gs.addstg("nikaxi  no  xirikudtti  ni  mukaxu  nohodtri  kaxitadtnn  to")
            gs.addstg("tika  ni  mukaxu  kaxitadtnn  kadt  xarimasu")
            gs.addstg("hannniyuxukoxue(egeaeteee)  kadt  xarimasu")
        if cmd=="look gate":
            gs.addstg("simattteximasu")
        if cmd=="enter gate":
            gs.addstg("haxiremasenn")
        if cmd=="south":
            gs.addstg("minami  ni  yukimasu")
            gs.sc=sc_frontyard()
        return gs

class sc_busstop(scene):

    def initmsg(self,gs):
        gs.addstg("xanata  ha  hadtsutexi  ni  ximasu")

    def cmdexe(self,cmd,gs):
        return gs

class sc_parking(scene):

    def initmsg(self,gs):
        gs.addstg("xanata  ha  tiyuxusiyasidtyoxu  ni  ximasu")

    def cmdexe(self,cmd,gs):
        if cmd=="look":
            gs.addstg("kurumae(eceaere)  kadt  xarimasu")
        return gs

class sc_backyard(scene):

    def initmsg(self,gs):
        gs.addstg("xanata  ha  xuraniwa  ni  ximasu")

    def cmdexe(self,cmd,gs):
        return gs

class sc_entrancefront(scene):

    def initmsg(self,gs):
        gs.addstg("xanata  ha  nikaxi  no  kedtnnkannmaxe  ni  ximasu")

    def initmsg(self,cmd,gs):
        return gs

class building(cggframe):

    def __init__(self):
        self.cgg=CGGPYG("")
        self.gamestate="play"
        self.advm=txtscrm(self.cgg)
        self.advm.addstg("tixenowa  haxusu  e:  tekisuto  xatodthedtnntiyae-")
        self.advm.addstg("e2e0e2e0  eteeenekeeey  eaeiekeoeuekeaei")
        self.advm.addstg("")
        self.advm.sc.initmsg(self.advm)
        self.advm.addstg("eceoememeaenede:")
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
                self.advm.sc.initmsg(self.advm)
                self.advm.addstg("eceoememeaenede:")
            self.advm.addcmd(chr)
        if self.gamestate=="gameover" and key==pygame.K_RETURN:
            self.__init__()
            self.gamestate="play" 

    def gameover(self):
        pass

    def routine(self):
        pass

bl=building()
bl.main(0.01)

