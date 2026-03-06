import pgzrun
import random

WIDTH=800
HEIGHT=800

score=0

ant=Actor("ant")
candy=Actor("candy")

ant.pos=90,40
candy.pos=400,400

def draw():
    screen.blit("grass",(0,0))
    ant.draw()
    candy.draw()
    screen.draw.text("score "+str(score),color="Black",midtop=(WIDTH/2,10))


def move():
    candy.x=random.randint(40,(WIDTH-40))
    candy.y=random.randint(80,(HEIGHT-80))

def update():
    global score
    if keyboard.w:
        ant.y-=5
    elif keyboard.a:
        ant.y+=5
    elif keyboard.s:
        ant.x-=5
    elif keyboard.d:
        ant.x+=5
    candycollected=ant.colliderect(candy)

    if candycollected:
        move()
        score+=1
    

pgzrun.go()