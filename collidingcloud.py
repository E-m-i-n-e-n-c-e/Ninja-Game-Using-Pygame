import sys
import pygame as p
class Game:
    def __init__(self) :
         
        p.init()

        p.display.set_caption("Ninja Game")

        icon=p.image.load("rika.jpg")

        p.display.set_icon(icon)

        self.screen=p.display.set_mode((640,480))
        self.cld1=p.image.load("data/images/clouds/cloud_1.png")
        self.cld1.set_colorkey((0,0,0))
        self.clock =p.time.Clock()
        self.cld1_pos=[10,10]
        self.cld1_vertical=[False,False]
        self.cld1_horizontal=[False,False]
        self.cld1=p.transform.scale(self.cld1,tuple(i*1.25 for i in self.cld1.get_size()))
        self.collisionarea=p.Rect(100,100,175,175)
    def run(self):
        while True:
            self.screen.fill((0,0,255))
            
            cld_rect=p.Rect(*self.cld1_pos,*self.cld1.get_size())
            
            if cld_rect.colliderect(self.collisionarea):
                p.draw.rect(self.screen,(0,0,0),self.collisionarea)
            else:
                p.draw.rect(self.screen,(255,255,0),self.collisionarea)
            self.screen.blit(self.cld1,self.cld1_pos)
            p.display.update()
            self.clock.tick(60) 
            self.cld1_pos[1]+=(self.cld1_vertical[1]-self.cld1_vertical[0])*2 
            self.cld1_pos[0]+=(self.cld1_horizontal[0]-self.cld1_horizontal[1])*2
          
            for event in p.event.get():
                if event.type==p.QUIT:
                    p.quit()
                    sys.exit()
                
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
            
                            
             

                
                 
                 

Game().run()
