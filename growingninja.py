import sys
import pygame as p
from scripts.entities import *
from scripts.utils import *

class Game:
    def __init__(self) :
         
        p.init()

        p.display.set_caption("Ninja Game")

        icon=p.image.load("rika.jpg")

        p.display.set_icon(icon)

        self.screen=p.display.set_mode((640,480))
         
        self.clock =p.time.Clock()
        
        self.vertical=[False,False]
        self.horizontal=[False,False]
        self.assets={
            'player': load_image("entities/player.png")
        }
        
        self.player=PhysicsEntity(self,"player",(10,10),(16,30))
        

        self.collisionarea=p.Rect(100,100,175,175)
    def run(self):
        while True:
            self.screen.fill((0,0,255))
            self.player.update(((self.horizontal[0]-self.horizontal[1])*3,(self.vertical[1]-self.vertical[0])*3))
            
             
            player_rect=p.Rect(*self.player.pos,*self.player.size)
            
            if player_rect.colliderect(self.collisionarea):
                p.draw.rect(self.screen,(255,255,0),self.collisionarea)
                self.player.size=tuple(i*1.001 for i in self.player.size)
                self.player.update_size()

                
            else:
                p.draw.rect(self.screen,(0,0,0),self.collisionarea)
            self.player.render(self.screen)
            # self.player.update_size()
            p.display.update()
            self.clock.tick(60) 
            
          
            for event in p.event.get():
                if event.type==p.QUIT:
                    p.quit()
                    sys.exit()
                
                if event.type==p.KEYDOWN:
                    if event.key==p.K_w or event.key==p.K_UP:
                        self.vertical[0]=True
                    if event.key==p.K_s or event.key==p.K_DOWN:
                        self.vertical[1]=True
                if event.type==p.KEYUP:
                    if event.key==p.K_w or event.key==p.K_UP:
                        self.vertical[0]=False
                    if event.key==p.K_s or event.key==p.K_DOWN:
                        self.vertical[1]=False
                    if  event.key==p.K_SPACE:
                        self.player.size=tuple(i*1.1 for i in self.player.size)

                if event.type==p.KEYDOWN:
                    if event.key==p.K_d or event.key==p.K_RIGHT:
                        self.horizontal[0]=True
                    if event.key==p.K_a or event.key==p.K_LEFT:
                        self.horizontal[1]=True
                if event.type==p.KEYUP:
                    if event.key==p.K_d or event.key==p.K_RIGHT:
                        self.horizontal[0]=False
                    if event.key==p.K_a or event.key==p.K_LEFT:
                        self.horizontal[1]=False
                 
                   
                       
                
                  
                            
             

                
                 
                 

Game().run()
