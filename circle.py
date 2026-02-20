import pgzrun
import random
WIDTH=600
HEIGHT=600

def draw():
    screen.fill("red")
    radius=200
    for i in range(10):
        r=0
        g=0
        b=random.randint(0,255)
        screen.draw.filled_circle((300,300),radius,(r,g,b))
        screen.draw.line((0,600),(600,0),color="white")
        screen.draw.text("HOME",(300,400),color="white",fontsize=100)
        radius-=10

pgzrun.go()
        