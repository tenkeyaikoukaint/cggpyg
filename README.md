# cggpyg
python-pygame graphic character displaying framework

## require

python(2 or 3), pygame

## load module

from syslogic import CGGPYG
cgg=CGGPYG("")
(normal color)

from sysgreen import CGGPYG
cgg=CGGPYG("")
(green display)

from syslcd4l import CGGPYG
cgg=CGGPYG()
(LCD screen)

## methods

def put(chrname,x,y)

put character on 20*20 screen
chrnames:
"a","b".."z"
"0","1".."9"
"circle","block,"brick","se","ne","sw","nw"(triangles)
"slash","backslash"

def puth(chrname,x,y)

put character on 40*20 screen

def setcolor(cc)

cc:
0:black 1:blue 2:red 3:magenta 4:green 5:cyan 6:yellow 7:white

def cls()

clear screen
