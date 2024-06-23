from turtle import *
bgcolor("#222"), setup(500,400)
hideturtle(), tracer(0), penup()
def Text(txt, col:tuple, x, y, shader:bool, size):
    font = ("Consolas",size,"bold")
    for i in range(shader + 1):
        goto(-2*i+x, 4*i+y)
        color(col) if i|(not shader) else color(0,0,0)
        write(txt,font=font,align="center")

from math import sin, cos
from datetime import datetime
def _Oneo_Kuu():
    update(), clear()
    c = datetime(2024,1,1) - datetime.today()
    TITLE = ["ngày", "giờ", "phút", "giây"]
    COUNTDOWN = [ c.days, c.seconds//3600,
        (c.seconds%3600)//60, c.seconds%60 ]
    if not any(COUNTDOWN) or COUNTDOWN[0]<0:
        COUNTDOWN = [2,0,2,4]
        TITLE = ["happy", "new", "year", "!"]
    Text("Countdown 2024", (0,0,0), 0, 80, False, 42)
    for i in range(len(COUNTDOWN)):
        color = (cos(i-2)/2+.5,.5,cos(i+2)/2+.5)
        Text(COUNTDOWN[i], color, -150+120*i-30, -25, True, 54)
        Text(TITLE[i], color, -150+120*i-30, -50, False, 18)
    ontimer(_Oneo_Kuu, 200)
_Oneo_Kuu()
mainloop()