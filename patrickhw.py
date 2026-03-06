import pgzrun
import random
WIDTH=1200
HEIGHT=1200
messege=""
pat=Actor("pat1")
def draw():
    screen.fill("white")
    pat.draw()
    screen.draw.text(messege,center=(400,20),fontsize=40, color="black")
def update():
    if keyboard.l:
        pat.x-=10
    elif keyboard.p:
        pat.x+=10
    elif keyboard.o:
        pat.y-=10
    elif keyboard.k:
        pat.y+=10
def positions():
    pat.x=random.randint(80,720)
    pat.y=random.randint(80,720)
def on_mouse_down(pos):
    global messege
    if pat.collidepoint(pos):
        positions()
        messege="amazing"
    else:
        messege="restart"
    

pgzrun.go()
