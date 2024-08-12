import pygame as p
import random as r
class Cloud:

    def __init__(self, img, pos, speed, depth):
        self.img = img
        self.pos = list(pos)
        self.speed = speed
        self.depth = depth


    def update(self):
      self.pos[0] += self.speed

    def render(self,surf,offset=(0,0)):
        render_pos=tuple(i-j*self.depth for i,j in zip(self.pos,offset))
        
        surf.blit(self.img,tuple(i%(surf.get_size()[j]+self.img.get_size()[j])-self.img.get_size()[j] for i,j in zip(render_pos,range(2))))

class Clouds:
        def __init__(self,cloud_imgs,count=16):
            self.clouds=[]
            for i in range(count):
                self.clouds.append(Cloud(r.choice(cloud_imgs),tuple(i*r.random()*9999 for i in (1,1)),r.random()*0.05+0.05,0.2+r.random()*0.6))
            self.clouds.sort(key=lambda x:x.depth)
        
        def update(self):
            
            for  cloud in self.clouds:
                cloud.update()
        def render(self,surf,offset=(0,0)):
            for  cloud in self.clouds:
                cloud.render(surf,offset)
                
