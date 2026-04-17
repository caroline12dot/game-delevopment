import pgzrun
import random

WIDTH=800
HEIGHT=600

centerx=WIDTH/2
centery=HEIGHT/2
center=(centerx,centery)
final_level=6
startspeed=10
Items=["bag","battery","bottle","chips"]
gameover=False
gamecomplete=False
currentlevel=1
items=[]
animations=[]
def draw():
    global items, gameover, gamecomplete,currentlevel
    screen.clear()
    screen.blit("bground",(0,0))
    if gameover:
        screen.draw.text("Game over!",fontsize=30,center=center,color="Black")
    elif gamecomplete:
        screen.draw.text("Well done!",fontsize=30,center=center,color="Black")
    else:

        for i in items:
            i.draw()
def update():
    global items
    if len(items)==0:
        items=make_items(currentlevel)
def make_items(extra_items):
    items_tocreate=option_tocreate(extra_items)
    newitems=createitems(items_tocreate)
    layoutitems(newitems)
    animate_items(newitems)
    return newitems
def option_tocreate(extra_items):
    items_tocreate=["paper"]
    for i in range(0,extra_items):
        random_option=random.choice(Items)
        items_tocreate.append(random_option)
    return items_tocreate
def createitems(items_tocreate):
    newitems=[]
    for i in items_tocreate:
        item=Actor(i+"img")
        newitems.append(item)
    return newitems
def layoutitems(items_tolayout):
    gaps=len(items_tolayout)+1
    gapssize=WIDTH/gaps
    random.shuffle(items_tolayout)
    for i,g in enumerate(items_tolayout):
        newx=(i+1)*gapssize
        g.x=newx
def animate_items(items_toanimate):
    global animations
    for i in items_toanimate:
        duration=startspeed-currentlevel
        i.anchor=("center","bottom")
        animation=animate(i,duration=duration,on_finished=handle_gameover,y=HEIGHT)
        animations.append(animation)
def handle_gameover():
    global gameover
    gameover=True
def on_mouse_down(pos):
    global items,currentlevel
    for i in items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                handle_gamecomplete()
            else:
                handle_gameover()
def handle_gamecomplete():
    global currentlevel, items, animations, gamecomplete
    stop_animations(animations)
    if currentlevel==final_level:
        gamecomplete=True
    else:
        currentlevel+=1
        items=[]
        animations=[]
def stop_animations(animations_tostop):
    for i in animations_tostop:
        if i.running:
            i.stop()
pgzrun.go()
        