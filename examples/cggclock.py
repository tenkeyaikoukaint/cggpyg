from cggframe import cggframe
import time
import datetime
from syslcd1l import CGGPYG

class cggclock(cggframe):

    def __init__(self):

        self.cgg=CGGPYG()
        self.gamestate="play"

    def routine(self):

        dt=datetime.datetime.now()
        self.cgg.cls()
        self.cgg.setcolor(7)
        self.cgg.printc(dt.strftime("%H:%M:%S"),0,0)

clock=cggclock()
clock.main(0.1)
