import time
import random
import pygame
from cggframe import cggframe
from pokedisp import displaymanager

class gamevals:

    def __init__(self):

        self.njp=["","mark/merchant","precious metal","george/knight","old gem","map","gem of man","maria/princess","herb","mineral","robin/thief","gem of forest","dragon","dragons nail","gem of dragon","gem of god","gem of sky","gem of earth","coin","vulture","antique merchant","farmer","priest","",""]
        self.plname=["can not go","gate of the town","public square","antique market","inn","highway","highway","gate of village","vegitable field","farm house","wilderness","wilderness","ruin","wilderness","cave","highway","mountain","forest path","mountain path","pass","shrine","nest of vulture","cliff path","top of mountain","forest","forest","forest","forest","forest","forest","",""]
        """pos:99=hidden 50=players possesion"""
        self.pos=[0,15,99,4,99,99,99,18,99,99,29,99,14,99,99,99,99,99,99,21,3,9,20,0]
        self.mapfw=[0,5,0,0,2,6,15,0,0,0,0,13,11,14,0,24,17,18,0,22,0,0,23,0,25,29,28,0,0,0,0,0]
        self.maprt=[0,2,3,0,0,0,7,8,9,0,6,10,0,0,0,16,0,0,19,20,0,22,0,0,0,0,25,26,0,0,0,0]
        self.maplt=[0,0,1,2,0,0,10,6,7,8,11,0,0,0,0,0,15,0,0,18,19,0,21,0,0,26,27,0,0,0,0]
        self.mapbk=[0,0,4,0,0,1,5,0,0,0,0,12,0,11,13,6,0,16,17,0,0,0,19,22,15,24,0,0,26,25,0,0]
        self.person=[0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,1,0,0]
        self.pl=1
        self.gold=0
        self.gameflag=1
        self.str=["","","","","","",""]
        self.scroll=False

class model:

    def move(self,gs,func,dir):

        if func>0:
            gs.str[0]="you go "+str(dir)+"."
            gs.pl=func
        else:
            gs.str[0]="you can not go this direction."
        return gs

    def search(self,gs):

        gs.str[0]=""
        if gs.pl==28 and gs.pos[10]==50 and gs.pos[11]==99:
            gs.str[1]="robin find a (gem of forest)"
            gs.pos[11]=50
        elif gs.pl==27 and gs.pos[7]==50 and gs.pos[8]==99:
            gs.str[1]="maria find a (herb)."
            gs.pos[8]=50
        elif gs.pl==22 & gs.pos[9]==99:
            gs.str[1]="you find a piece of (mineral)."
            gs.pos[9]=50
        elif gs.pl==12 and gs.pos[10]==50 and gs.pos[4]==99:
            gs.str[1]="robin find a (old gem)."
            gs.pos[4]=50
        elif gs.pl==12 and gs.pos[10]==50 and gs.pos[2]==99:
            gs.str[1]="robin find a piece of (precious matal)."
            gs.pos[2]=50
        else:
            gs.str[1]="you can find nothing special."
        if gs.pos[4]==50 and gs.pos[6]==50 and gs.pos[11]==50 and gs.pos[14]==50 and gs.pos[15]==50 and gs.pos[16]==50 and gs.pos[17]==50:
            gs.str[1]="you solve a game Anekgard!"
            gs.gameflag=0
        return gs

    def reportf(self,gs):

        mes0="fellow:"
        mes1=""
        mes2=""
        for i in range(1,22):
            if gs.pos[i]==50 and gs.person[i]==1:
                mes0=mes0+ gs.njp[i]+" "
        if len(mes0)>32:
            mes1=mes0[32:len(mes0)-1]
        mes2="coin:"+str(gs.gold)+""
        gs.str[0]=mes0
        gs.str[1]=mes1
        gs.str[2]=mes2
        return gs

    def reporti(self,gs):
        mes0="inventory:"
        mes1=""
        mes2=""
        for i in range(1,22):
            if gs.pos[i]==50 and gs.person[i]==0:
                mes0=mes0+gs.njp[i]+"/"
        if len(mes0)>32:
            mes1=mes0[32:len(mes0)+1]
        if len(mes1)>32:
            mes2=mes1[32:len(mes1)+1]
        gs.str[0]=mes0
        gs.str[1]=mes1
        gs.str[2]=mes2
        return gs

    def help(self,gs):
        mes0="arrow:move m:map a:attack s:search t:talk i:inventory f:fellow and coin"
        mes1=""
        mes2=""
        if len(mes0)>32:
            mes1=mes0[32:len(mes0)+1]
        if len(mes1)>32:
            mes2=mes1[32:len(mes1)+1]
        gs.str[0]=mes0
        gs.str[1]=mes1
        gs.str[2]=mes2
        return gs

    def map(self,gs):

        gs.str[0]="  n:"+gs.plname[gs.mapfw[gs.pl]]
        gs.str[1]="w:"+gs.plname[gs.maplt[gs.pl]]+" e:"+gs.plname[gs.maprt[gs.pl]]
        gs.str[2]="  s:"+gs.plname[gs.mapbk[gs.pl]]

        return gs

    def fight(self,gs):

        if gs.pl==14 and gs.pos[3]==50 and gs.pos[12]==14:
            gs.str[0]="dragon escapes"
            gs.str[1]="you get a nail of dragon and gem of dragon."
            gs.pos[12]=99
            gs.pos[13]=50
            gs.pos[14]=50
        if gs.pl==14 and gs.pos[3]!=50:
            gs.str[1]="enemy defences!"
        if gs.pl==21:
            gs.str[1]="enemy defences!"
        if gs.pl==3 or gs.pl==9 or gs.pl==10 or gs.pl==4 and gs.pos[3]==4 or gs.pl==15 and gs.pos[1]==15 or gs.pl==29 and gs.pos[10]==29 or gs.pl==18 and gs.pos[7]==18:
            gs.str[0]="do not attack"
            gs.str[1]="innocent people"
        if gs.pos[4]==50 and gs.pos[6]==50 and gs.pos[11]==50 and gs.pos[14]==50 and gs.pos[15]==50 and gs.pos[16]==50 and gs.pos[17]==50:
            gs.str[1]="you solve game anekgard!"
            gs.gameflag=0

        return gs

    def talk(self,gs):

        gs.str[0]=""
        if gs.pl==3 and gs.pos[2]==50:
            gs.str[1]="you sell a precious metal"
            gs.pos[2]=0
            gs.gold=gs.gold+1
        if gs.pl==3 and gs.pos[8]==50:
            gs.str[1]="you sell a herb."
            gs.pos[8]=0
            gs.gold=gs.gold+1
        if gs.pl==3 and gs.pos[9]==50:
            gs.str[1]="you sell a mineral."
            gs.pos[9]=0
            gs.gold=gs.gold+1
        if gs.pl==3 and gs.pos[13]==50:
            gs.str[1]="you sell nail of dragon."
            gs.pos[13]=0
            gs.gold=gs.gold+1
        if gs.pl==3 and gs.pos[1]==50 and gs.pos[6]==99 and gs.gold>0 and gs.pos[1]==50:
            gs.str[1]="you get a gem of man by mark"
            gs.pos[6]=50
            gs.gold=gs.gold-1
        if gs.pl==4 and gs.pos[3]==4:
            gs.str[1]="george join you."
            gs.pos[3]=50
        if gs.pl==9 and gs.pos[17]==99 and gs.gold>0 and gs.pos[1]==50:
            gs.str[0]="you get a gem of earth by mark" 
            gs.pos[17]=50
            gs.gold=gs.gold-1
        if gs.pl==15 and gs.pos[1]==15:
            gs.str[1]="mark join you"
            gs.pos[1]=50
        if gs.pl==18 and gs.pos[7]==18:
            gs.str[1]="maria join you."
            gs.pos[7]=50
        if gs.pl==20 and gs.pos[15]==99 and gs.pos[7]==50:
            gs.str[1]="you get gem of god with maria"
            gs.pos[15]=50 
        if gs.pl==21 and gs.pos[16]==99 and gs.pos[7]==50:
            gs.str[1]="you get gem of sky with maria"
            gs.pos[16]=50
        if gs.pl==29 and gs.pos[10]==29:
            gs.str[1]="robin join you"
            gs.pos[10]=50
        if gs.pos[4]==50 and gs.pos[6]==50 and gs.pos[11]==50 and gs.pos[14]==50 and gs.pos[15]==50 and gs.pos[16]==50 and gs.pos[17]==50:
            gs.str[1]="you solve game anekgard"
            gs.gameflag=0

        return gs



    def cmdexe(self,gs,stginp):

        gs.str[0]=""
        gs.str[1]=""
        gs.str[2]=""
        if stginp=="north":
            func=gs.mapfw[gs.pl]
            dir="north"
            gs=self.move(gs,func,dir)
            gs=self.conds(gs)
            gs=self.showdrct(gs)
        elif stginp=="south":
            func=gs.mapbk[gs.pl]
            dir="south"
            gs=self.move(gs,func,dir)
            gs=self.conds(gs)
            gs=self.showdrct(gs)
        elif stginp=="east":
            func=gs.maprt[gs.pl]
            dir="east"
            gs=self.move(gs,func,dir)
            gs=self.conds(gs)
            gs=self.showdrct(gs)
        elif stginp=="west":
            func=gs.maplt[gs.pl]
            dir="west"
            gs=self.move(gs,func,dir)
            gs=self.conds(gs)
            gs=self.showdrct(gs)
        elif stginp=="attack":
            gs=self.fight(gs)
            gs=self.showdrct(gs)
        elif stginp=="report":
            gs=self.report(gs)
        elif stginp=="search":
            gs=self.search(gs)
            gs=self.showdrct(gs)
        elif stginp=="talk":
            gs=self.talk(gs)
            gs=self.showdrct(gs)
        elif stginp=="map":
            gs=self.map(gs)
        elif stginp=="inv":
            gs=self.reporti(gs)
        elif stginp=="fellow":
            gs=self.reportf(gs)
        elif stginp=="q":
            gs.gameflag=0
        elif stginp=="help":
            gs=self.help(gs)
        else:
            gs=self.showdrct(gs)
            gs=self.conds(gs)
        return gs



    def conds(self,gs):

        gs.str[1]="you are at " + gs.plname[gs.pl]
        for i in range(1,21):
            if gs.pos[i]==gs.pl:
                gs.str[1]="there is "+gs.njp[i] + ""
        return gs

    def showdrct(self,gs):

        mes="you can go "
        if gs.mapfw[gs.pl]>0:
            mes+= "north "
        if gs.maprt[gs.pl]>0:
            mes+= "east "
        if gs.maplt[gs.pl]>0:
            mes+= "west "
        if gs.mapbk[gs.pl]>0:
            mes+= "south "
        mes=mes+"]"
        gs.str[2]=mes

        return gs

class pokegard(cggframe):

    def __init__(self):

        self.dm=displaymanager()
        self.gamestate="title"
        self.gv=gamevals()
        self.adv=model()
        self.str=["","",""]

    def title(self):

        self.dm.printstr("anekgard the role playing game",0)
        self.dm.printstr("2019 tenkey aikoukai",1)
        self.dm.printstr("press ret key",2)
        self.dm.draw()

    def gameover(self):

        dummy=0

    def keyin(self,key):

        if self.gamestate=="title":
            if key==pygame.K_RETURN:
                self.dm.inputmode("on")
                self.gamestate="play"
                self.gv=self.adv.showdrct(self.gv)
                self.gv=self.adv.conds(self.gv)
        elif self.gamestate=="play":
            cmd=""
            if key==pygame.K_s:
                self.dm.inputc("search")
                cmd="search"
            if key==pygame.K_t:
                self.dm.inputc("talk")
                cmd="talk"
            if key==pygame.K_a:
                self.dm.inputc("attack")
                cmd="attack"
            if key==pygame.K_m:
                self.dm.inputc("show map")
                cmd="map"
            if key==pygame.K_f:
                self.dm.inputc("show fellow and coin")
                cmd="fellow"
            if key==pygame.K_i:
                self.dm.inputc("show inventory")
                cmd="inv"
            if key==pygame.K_h or key==pygame.K_RETURN:
                self.dm.inputc("help")
                cmd="help"
            if key==pygame.K_UP:
                self.dm.inputc("go north")
                cmd="north"
            if key==pygame.K_DOWN:
                self.dm.inputc("go south")
                cmd="south"
            if key==pygame.K_LEFT:
                self.dm.inputc("go west")
                cmd="west"
            if key==pygame.K_RIGHT:
                self.dm.inputc("go east")
                cmd="east"
            gv=self.adv.cmdexe(self.gv,cmd)
        if self.gamestate=="gameover":
            if key==pygame.K_RETURN:
                self.__init__()
                self.gamestate="title"

    def routine(self):

        self.dm.tick()
        self.dm.printstr(self.gv.str[0],0)
        self.dm.printstr(self.gv.str[1],1)
        self.dm.printstr(self.gv.str[2],2)
        self.dm.draw()

pg=pokegard()
pg.main(0.05)

