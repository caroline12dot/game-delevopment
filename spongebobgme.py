import pgzrun
import random
WIDTH=800
HEIGHT=800
messege=""
sponge=Actor("spongebob")
def draw():
    screen.fill("white")
    sponge.draw()
    screen.draw.text(messege,center=(400,20),fontsize=40, color="black")
def update():
    if keyboard.d:
        sponge.x-=5
    elif keyboard.a:
        sponge.x+=5
    elif keyboard.w:
        sponge.y-=5
    elif keyboard.s:
        sponge.y+=5
def positions():
    sponge.x=random.randint(80,720)
    sponge.y=random.randint(80,720)
def on_mouse_down(pos):
    global messege
    if sponge.collidepoint(pos):
        positions()
        messege="well done"
    else:
        messege="try again"
    

pgzrun.go()
