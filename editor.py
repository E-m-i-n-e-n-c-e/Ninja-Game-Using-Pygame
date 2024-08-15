import sys
import pygame as p
from scripts.entities import *
from scripts.utils import *
from scripts.tilemap import *
from scripts.clouds import *
# from temp import *
class Editor:
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
            'player': load_image("entities/player.png"),
            'decor':load_images("tiles/decor"),
            'grass': load_images("tiles/grass"),
            'large_decor': load_images("tiles/large_decor"),
            'spawners': load_images("tiles/spawners"),
            'stone': load_images("tiles/stone"),
            'background': load_image("background.png"),
            'clouds': load_images("clouds"),
            'player/idle':Animation(load_images('entities/player/idle'),img_dur=8),
            'player/run':Animation(load_images('entities/player/run'),img_dur=4),
            'player/jump':Animation(load_images('entities/player/jump'),img_dur=5),
            'player/slide':Animation(load_images('entities/player/slide'),img_dur=5),
            'player/wall_slide':Animation(load_images('entities/player/wall_slide'),img_dur=5)
            

        }
        self.tilemap=TileMap(self)
       
        self.player=Player(self,(70,10),(8,15))
    
        self.display=p.Surface(tuple(i/2 for i in self.screen.get_size() ))
        self.jump=100
        self.count=self.jump
        self.collisionarea=p.Rect(100/2,100/2,175/2,175/2)
        self.gameover=p.image.load("gameover.png")
        self.gameover=p.transform.scale(self.gameover,(320,240))
        self.gameover_bool=False
        self.scroll=[0,0]
        self.clouds=Clouds(self.assets['clouds'])
        self.tick=60
    
    def run(self):
        while True:
            # p.transform.scale(self.assets['background'],self.display.get_size())
            self.display.blit(self.assets['background'],(0,0))
            self.scroll[0]+=(self.player.rect().centerx-self.display.get_width()/2-self.scroll[0])/30
             
            if(self.player.pos[1]<300):
                self.scroll[1]+=(self.player.rect().centery-self.display.get_height()/2-self.scroll[1])/30
            render_scroll=list(int(i) for i in self.scroll)
            self.clouds.update()
            self.clouds.render(self.display,offset=render_scroll)
            self.tilemap.render(self.display,offset=render_scroll)
            self.player.update(self.tilemap,((self.horizontal[0]-self.horizontal[1])*1,(self.vertical[1]-self.vertical[0])*2))
            
           
             
         
            self.player.render(self.display,offset=render_scroll)
            if(self.player.pos[1]-self.scroll[1]>260 and self.player.pos[1]>240):
               self.display.blit(self.gameover,(0,0))
               self.gameover_bool=True
               self.player.pos[1]=self.scroll[1]+400
                
            
            self.screen.blit(p.transform.scale(self.display,self.screen.get_size()),(0,0))
            
            p.display.update()
            self.clock.tick(self.tick) 
            
            
          
            for event in p.event.get():
                if event.type==p.QUIT:
                    p.quit()
                    sys.exit()
                
                if event.type==p.KEYDOWN:
                    if (event.key==p.K_w or event.key==p.K_UP) :
                        if(self.count!=0):
                            self.player.vel[1]=-2.5
                            self.count-=1
                    if (event.key==p.K_s or event.key==p.K_DOWN) :
                        self.vertical[1]=True
                    if event.key==p.K_d or event.key==p.K_RIGHT  :
                        self.horizontal[0]=True
                    if event.key==p.K_a or event.key==p.K_LEFT  :
                        self.horizontal[1]=True
                    if  event.key==p.K_RETURN :
                        self.tick=2
                if event.type==p.KEYUP:
                    # if event.key==p.K_w or event.key==p.K_UP:
                    #     self.vertical[0]=False
                    if (event.key==p.K_d or event.key==p.K_RIGHT)  :
                        self.horizontal[0]=False
                    if (event.key==p.K_a or event.key==p.K_LEFT) :
                        self.horizontal[1]=False
                    if event.key==p.K_s or event.key==p.K_DOWN:
                        self.vertical[1]=False
                    if  event.key==p.K_SPACE:
                        self.player.size=tuple(i*1.25 for i in self.player.size)
                    if  event.key==p.K_RETURN and self.gameover_bool:

                        self.player=Player(self,(70,10),(8,15))
                        self.gameover_bool=False
                    if  event.key==p.K_RETURN:
                        self.tick=60
                    
                        

                 
                 
                   
                       
                
                  
                            
             

                
                 
                 

Editor().run()
