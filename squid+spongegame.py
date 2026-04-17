import pgzrun
import random

WIDTH=800
HEIGHT=800

score=0

squid=Actor("squid")
sponge=Actor("sponge")

squid.pos=90,40
sponge.pos=400,400

def draw():
    screen.blit("sea",(0,0))
    squid.draw()
    sponge.draw()
    screen.draw.text("score "+str(score),color="WHITE",midtop=(WIDTH/2,10,))


def move():
    sponge.x=random.randint(40,(WIDTH-40))
    sponge.y=random.randint(80,(HEIGHT-80))

def update():
    global score
    if keyboard.w:
        squid.y-=3
    elif keyboard.s:
        squid.y+=3
    elif keyboard.a:
        squid.x-=3
    elif keyboard.d:
        squid.x+=3
    spongecollected=squid.colliderect(sponge)

    if spongecollected:
        move()
        score+=10
    

pgzrun.go()