import pygame as p
import sys
p.init()
clock =p.time.Clock()
# for i in range(10,0,-1):
#     clock.tick(1)
#     print(i)
icon=p.image.load("rika.jpg")

screen=p.display.set_mode((640,480))
font = p.font.Font(None, 74)

 
for i in range(10,0,-1):
    for event in p.event.get():
        if event.type==p.QUIT:
            p.quit()
            sys.exit()
    text=font.render(str(i),True,(255, 255, 255))
    screen.blit(text,(300,200))
    p.display.update()
    screen.fill((0, 0, 0))
    clock.tick(1)
screen.blit(icon,(0,0))
while True:
            for event in p.event.get():
                if event.type==p.QUIT:
                    p.quit()
                    break
            else:
                p.display.update()
                clock.tick(60) 
                continue
            break