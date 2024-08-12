import sys
import pygame as p
class Game:
    def __init__(self) :
         
        p.init()

        p.display.set_caption("Ninja Game")

        self.icon=p.image.load("rika.jpg")

        p.display.set_icon(self.icon)
        
        self.screen=p.display.set_mode((640,480))
        self.cld1=p.image.load("data/images/clouds/cloud_1.png")
        self.clock =p.time.Clock()
        self.cld1_pos=[10,10]
        self.cld1_vertical=[False,False]
        self.cld1_horizontal=[False,False]
        self.cld1.set_colorkey((0,0,0))
        self.icon2=p.transform.scale(self.icon,tuple(i*0.2 for i in self.icon.get_size()))
        self.bool=True
    def run(self):
        while True:
            for event in p.event.get():
                if event.type==p.QUIT:
                    p.quit()
                    break
                if event.type==p.KEYDOWN:
                    if event.key==p.K_w or event.key==p.K_UP:
                        self.cld1_vertical[0]=True
                    if event.key==p.K_s or event.key==p.K_DOWN:
                        self.cld1_vertical[1]=True
                if event.type==p.KEYUP:
                    if event.key==p.K_w or event.key==p.K_UP:
                        self.cld1_vertical[0]=False
                    if event.key==p.K_s or event.key==p.K_DOWN:
                        self.cld1_vertical[1]=False
                if event.type==p.KEYDOWN:
                    if event.key==p.K_d or event.key==p.K_RIGHT:
                        self.cld1_horizontal[0]=True
                    if event.key==p.K_a or event.key==p.K_LEFT:
                        self.cld1_horizontal[1]=True
                if event.type==p.KEYUP:
                    if event.key==p.K_d or event.key==p.K_RIGHT:
                        self.cld1_horizontal[0]=False
                    if event.key==p.K_a or event.key==p.K_LEFT:
                        self.cld1_horizontal[1]=False
                if event.type==p.KEYUP:
                    if event.key==p.K_SPACE:
                        self.bool = not self.bool
                        # self.screen.fill((0,0,0))
                    
            else:
              
                if (self.bool):
                        temp=self.cld1
                else:
                        temp=self.icon2
                self.screen.blit(temp,self.cld1_pos)
                
                p.display.update()
                self.clock.tick(60) 
                self.cld1_pos[0]+=(self.cld1_horizontal[0]-self.cld1_horizontal[1])*2
                self.cld1_pos[1]+=(self.cld1_vertical[1]-self.cld1_vertical[0])*2
                 
                continue
            break

Game().run()

     
