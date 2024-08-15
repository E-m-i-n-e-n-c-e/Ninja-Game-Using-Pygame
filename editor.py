import sys
import pygame as p
from scripts.utils import load_images,load_image
from scripts.tilemap import TileMap
from scripts.clouds import Clouds
# from temp import *
class Editor:
    def __init__(self) :
         
         
        p.init()

        p.display.set_caption("Level Editor")

        icon=p.image.load("data/images/rika.jpg")
        
        p.display.set_icon(icon)

        self.screen=p.display.set_mode((640,480))
        
        self.clock =p.time.Clock()
        
        self.vertical=[False,False]
        self.horizontal=[False,False]
        self.assets={
           
            'decor':load_images("tiles/decor"),
            'grass': load_images("tiles/grass"),
            'large_decor': load_images("tiles/large_decor"),
            'stone': load_images("tiles/stone"),
            'background': load_image("background.png"),
            'clouds': load_images("clouds"),
          
            

        }
    #     self.tilemap=TileMap(self)
        
    
    #     self.display=p.Surface(tuple(i/2 for i in self.screen.get_size() ))
       
         
         
    #     self.scroll=[0,0]
    #     self.clouds=Clouds(self.assets['clouds'])
    #     self.tile_list=list(i for i in list(self.assets.keys())[:4])
    #     self.tile_group=0
    #     self.tile_variant=0
    #     self.shift=False
         
    
    # def run(self):
    #     while True:
    #         self.curr_tile=self.assets[self.tile_list[self.tile_group]][self.tile_variant].copy()
    #         self.curr_tile.set_alpha(100)
        
    #         self.display.blit(self.assets['background'],(0,0))
    #         self.display.blit(self.curr_tile,(5,5))
             
             
    #         render_scroll=list(int(i) for i in self.scroll)
    #         self.clouds.update()
    #         self.clouds.render(self.display,offset=render_scroll)
    #         self.tilemap.render(self.display,offset=render_scroll)
            
           
             
         
            
             
                
            
    #         self.screen.blit(p.transform.scale(self.display,self.screen.get_size()),(0,0))
            
    #         p.display.update()
    #         self.clock.tick(60) 
            
            
    #         print("hello")
    #         for event in p.event.get():
    #             if event.type==p.QUIT:
    #                 p.quit()
    #                 sys.exit()
    #             if event.type==p.MOUSEBUTTONDOWN:
    #                 if event.button==1:
    #                     self.left_click=True
    #                 if event.button==2:
    #                     self.middle_click=True
    #                 if event.button==3:
    #                     self.right_click=True
    #                 if event.button==4:
    #                     if(not self.shift):
    #                         self.tile_group=(self.tile_group+1)%len(self.tile_list)
    #                         self.tile_variant=0
    #                     else:
    #                         self.tile_variant=(self.tile_variant+1)%len(self.assets[self.tile_list[self.tile_group]])
    #                 if event.button==5:
    #                     if(not self.shift):
    #                         self.tile_group=(self.tile_group-1)%len(self.tile_list)
    #                         self.tile_variant=0
    #                     else:
    #                         self.tile_variant=(self.tile_variant-1)%len(self.assets[self.tile_list[self.tile_group]])
                
    #             if event.type==p.MOUSEBUTTONDOWN:
    #                 if event.button==1:
    #                     self.left_click=False
    #                 if event.button==2:
    #                     self.middle_click=False
    #                 if event.button==3:
    #                     self.right_click=False
                
    #             if event.type==p.KEYDOWN:
    #                 if (event.key==p.K_w or event.key==p.K_UP) :
    #                      self.vertical[0]=True

    #                 if (event.key==p.K_s or event.key==p.K_DOWN) :
    #                     self.vertical[1]=True
    #                 if event.key==p.K_d or event.key==p.K_RIGHT  :
    #                     self.horizontal[0]=True
    #                 if event.key==p.K_a or event.key==p.K_LEFT  :
    #                     self.horizontal[1]=True
    #                 if event.key==p.K_LSHIFT:
                       
    #                     self.shift= not self.shift
                    
    #             if event.type==p.KEYUP:
    #                 if event.key==p.K_w or event.key==p.K_UP:
    #                     self.vertical[0]=False
    #                 if (event.key==p.K_d or event.key==p.K_RIGHT)  :
    #                     self.horizontal[0]=False
    #                 if (event.key==p.K_a or event.key==p.K_LEFT) :
    #                     self.horizontal[1]=False
    #                 if event.key==p.K_s or event.key==p.K_DOWN:
    #                     self.vertical[1]=False
             
                  
                 
                    
                        

                 
                 
                   
                       
                
                  
                            
             

                
                 
                 

Editor().run()
