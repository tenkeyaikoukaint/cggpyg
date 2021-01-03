# cggpyg
python-pygame graphic character displaying framework

## require

python(2 or 3), pygame

## load module

from syslogic import CGGPYG<br />
cgg=CGGPYG("")<br />
(normal color)

from sysgreen import CGGPYG<br />
cgg=CGGPYG("")<br />
(green display)

from syslcd4l import CGGPYG<br />
cgg=CGGPYG()<br />
(LCD screen)

## methods

def put(chrname,x,y)

put character on 20*20 screen<br />
chrnames:<br />
"a","b".."z"<br />
"0","1".."9"<br />
"circle","block,"brick","se","ne","sw","nw"(triangles)<br />
"slash","backslash"

def puth(chrname,x,y)

put character on 40*20 screen

def setcolor(cc)

cc:<br />
0:black 1:blue 2:red 3:magenta 4:green 5:cyan 6:yellow 7:white

def cls()

clear screen
