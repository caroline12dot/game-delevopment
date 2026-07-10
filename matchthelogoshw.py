import pygame

pygame.init()
screen=pygame.display.set_mode((600,700))
screen.fill("purple")
font=pygame.font.SysFont("calibri",25)
dominos=pygame.image.load("venv//pro game development//images//dominos.png")
screen.blit(dominos,(60,10))
text1=font.render("DOMINOS",True,"blue")
screen.blit(text1,(300,390))
apple=pygame.image.load("venv/pro game development/images/apple.png")
screen.blit(apple,(60,190))
text2=font.render("APPLE",True,"blue")
screen.blit(text2,(300,590))
instagram=pygame.image.load("venv/pro game development/images/instagram.png")
screen.blit(instagram,(60,390))
text3=font.render("INSTAGRAM",True,"blue")
screen.blit(text3,(300,10))
tiktok=pygame.image.load("venv/pro game development/images/tiktok.png")
screen.blit(tiktok,(60,590))
text4=font.render("TIKTOK",True,"blue")
screen.blit(text4,(300,190))
pygame.display.update()
while True:
    event=pygame.event.poll()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    if event.type==pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        pygame.draw.circle(screen,"pink",(pos),15)
        pygame.display.update()
    elif event.type==pygame.MOUSEBUTTONUP:
        pos1=pygame.mouse.get_pos()
        pygame.draw.line(screen,"pink",(pos),(pos1),5)
        pygame.draw.circle(screen,"pink",(pos1),15)
        pygame.display.update()