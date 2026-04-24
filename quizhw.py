import pgzrun

TITLE="Quiz master"
WIDTH=800
HEIGHT=600

mbox=Rect(0,0, 800,90)
qbox=Rect(0,0, 650,170)
tbox=Rect(0,0, 110,170)
abox1=Rect(0,0, 300,100)
abox2=Rect(0,0, 300,100)
abox3=Rect(0,0, 300,100)
abox4=Rect(0,0, 300,100)
sbox=Rect(0,0, 110,250)

score=0
timeleft=10
question_file="venv//questhw.txt"
msg=""
gameover=False
abox=[abox1,abox2,abox3,abox4]
questions=[]
count=0
index=0

mbox.move_ip(0,0)
qbox.move_ip(15,100)
tbox.move_ip(680,100)
abox1.move_ip(15,300)
abox2.move_ip(350,300)
abox3.move_ip(15,450)
abox4.move_ip(350,450)
sbox.move_ip(680,300)

def draw():
    global msg
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(mbox,"White")
    screen.draw.filled_rect(qbox,"Blue")
    screen.draw.filled_rect(tbox,"Blue")
    screen.draw.filled_rect(sbox,"Red")
    for i in abox:
        screen.draw.filled_rect(i,"White")
    msg="Welcome to quizmaster "
    msg=msg+f"Q:{index} of {count}"
    screen.draw.textbox(msg,mbox,color="Black")
    screen.draw.textbox(str(timeleft),tbox,color="Black")
    screen.draw.textbox("SKIP",sbox,color="Black")
    screen.draw.textbox(question[0].strip(),qbox,color="Black")    
    i=1
    for j in abox:
        screen.draw.textbox(question[i].strip(),j,color="Black")
        i+=1
def readquestion():
    global count,questions
    file=open(question_file,"r")
    for i in file:
        questions.append(i)
        count+=1
    file.close()
def readnextquestion():
    global index
    index+=1
    return questions.pop(0).split(",")
def movemsg():
    mbox.x-=2
    if mbox.right<0:
        mbox.left=WIDTH
def update():
    movemsg()
def on_mouse_down(pos):
    i=1
    for j in abox:
        if j.collidepoint(pos):
            if i is int(question[5]):
                correctanswer()
            else:
                game_over()
        i+=1
    if sbox.collidepoint(pos):
        skipquestion()
def correctanswer():
    global score,question,timeleft,questions
    score+=1
    if questions:
        question=readnextquestion()
        timeleft=10
    else:
        game_over()
def game_over():
    global question,timeleft,gameover
    msg=f"gameover\nyou got {score} questions correct"
    question=[msg,"-","-","-","-",5]
    timeleft=0
    gameover=True
def skipquestion():
    global question,timeleft
    if questions and not gameover:
        question=readnextquestion()
        timeleft=10
    else:
        game_over()
def  timer():
    global timeleft
    if timeleft:
        timeleft-=1
    else:
        game_over()



readquestion()
question=readnextquestion()
clock.schedule_interval(timer,1)
pgzrun.go()