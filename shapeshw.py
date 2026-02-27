import pgzrun
import random
WIDTH=600
HEIGHT=600

def draw():
    screen.fill("black")
    w=400
    h=300
    radius=140
    for i in range(15):
     rect1=Rect((0,0),(w,h))
     r=random.randint(0,255)
     g=random.randint(0,255)
     b=0
     rect1.center=(300,300)
     screen.draw.rect(rect1,(r,g,b))
     w+=10
     h-=10
     r=3
     g=90
     b=200
     
     screen.draw.circle((300,300),radius,(r,g,b))
     radius-=10


pgzrun.go()