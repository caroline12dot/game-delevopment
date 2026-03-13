import random
import pgzrun

WIDTH=800
HEIGHT=800

total_stars=8
stars=[]
lines=[]
nextstar=0

def create_star():
    for i in range(total_stars):
        star=Actor("star")
        star.pos=random.randint(80,720),random.randint(80,720)
        stars.append(star)
def draw():
    screen.blit("galaxy",(0,0))
    n=1
    for i in stars:
        screen.draw.text(str(n),(i.pos[0],i.pos[1]+25))
        i.draw()
        n+=1
    for y in lines:
        screen.draw.line(y[0],y[1],color="White")
def update():
    pass
def on_mouse_down(pos):
    global nextstar,lines
    if nextstar<total_stars:
        if stars[nextstar].collidepoint(pos):
            if nextstar:
                lines.append((stars[nextstar-1].pos,stars[nextstar].pos))
            nextstar+=1
        else:
            lines=[]
            nextstar=0
 
create_star()
pgzrun.go()
