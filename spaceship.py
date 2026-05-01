import pgzrun
import random

WIDTH=1200
HEIGHT=600

ship=Actor("galaga")
ship.pos=(WIDTH/2,HEIGHT-60)
speed=5
bullets=[]
bugs=[]

direction=1
ship.dead=False
ship.countdown=90
for i in range(9):
    for j in range(4):

      bugs.append(Actor("bug"))
      bugs[-1].x=100+50*i
      bugs[-1].y=80+50*j
score=0
def gameover():
    screen.draw.text("GAMEOVER",(550,300))
def update():
    global score, direction
    movedown=False
    if ship.dead==False:
        if keyboard.d:
            ship.x-=speed
            if ship.x<=0:
                ship.x=0
        if keyboard.a:
            ship.x+=speed
            if ship.x>=WIDTH:
                ship.x=WIDTH
    for i in bullets:
        if i.y<=0:
            bullets.remove(i)
        else:
            i.y-=10
    if len(bugs)==0:
        gameover()
    if len(bugs)>0 and(bugs[-1].x>WIDTH-80 or bugs[0].x <80):
        movedown=True
        direction=direction*-1
    for i in bugs:
        i.x+=5*direction
        if movedown==True:
            i.y+=100
        if i.y > HEIGHT:
            bugs.remove(i)
        for j in bullets:
            if i.colliderect(j):
                score+=10
                bullets.remove(j)
                bugs.remove(i)
                if len(bugs)==0:
                    gameover()
        if i.colliderect (ship):
            ship.dead=True
    if ship.dead:
        ship.countdown-=1
    if ship.countdown==0:
        ship.dead=False
        ship.countdown=90
def draw():
    screen.clear()
    screen.fill("Blue")
    for i in bugs:
        i.draw()
    for i in bullets:
        i.draw()
    if ship.dead==False:
        ship.draw()
    screen.draw.text(str(score),(50,30))
    if len(bugs)==0:
        gameover()

def on_key_down(key):
    if ship.dead==False:   
        if key==keys.S:
            bullets.append(Actor("bullet"))
            bullets[-1].x=ship.x
            bullets[-1].y=ship.y-50
    

pgzrun.go()
