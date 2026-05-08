import pgzrun
import random

WIDTH=1200
HEIGHT=600

castle=Actor("castle")
castle.pos=(WIDTH/2,HEIGHT-60)
speed=4
sword=[]
dragon=[]

direction=1
castle.dead=False
castle.countdown=90
for i in range(9):
    for j in range(4):

      dragon.append(Actor("dragon"))
      dragon[-1].x=100+50*i
      dragon[-1].y=80+50*j
score=0
def gameover():
    screen.draw.text("GAMEOVER",(550,300))
def update():
    global score, direction
    movedown=False
    if castle.dead==False:
        if keyboard.d:
            castle.x-=speed
            if castle.x<=0:
                castle.x=0
        if keyboard.a:
            castle.x+=speed
            if castle.x>=WIDTH:
                castle.x=WIDTH
    for i in sword:
        if i.y<=0:
            sword.remove(i)
        else:
            i.y-=10
    if len(dragon)==0:
        gameover()
    if len(dragon)>0 and(dragon[-1].x>WIDTH-80 or dragon[0].x <80):
        movedown=True
        direction=direction*-1
    for i in dragon:
        i.x+=4*direction
        if movedown==True:
            i.y+=100
        if i.y > HEIGHT:
            dragon.remove(i)
        for j in sword:
            if i.colliderect(j):
                score+=5
                sword.remove(j)
                dragon.remove(i)
                if len(dragon)==0:
                    gameover()
        if i.colliderect (castle):
            castle.dead=True
    if castle.dead:
        castle.countdown-=1
    if castle.countdown==0:
        castle.dead=False
        castle.countdown=90
def draw():
    screen.clear()
    screen.fill("Blue")
    for i in dragon:
        i.draw()
    for i in sword:
        i.draw()
    if castle.dead==False:
        castle.draw()
    screen.draw.text(str(score),(50,30))
    if len(dragon)==0:
        gameover()

def on_key_down(key):
    if castle.dead==False:   
        if key==keys.S:
            sword.append(Actor("sword"))
            sword[-1].x=castle.x
            sword[-1].y=castle.y-50
    

pgzrun.go()