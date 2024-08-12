import os

import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img
 
BASE_IMG_PATH = 'data/images/'

def load_images(path):
    imgs = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        imgs.append(load_image(path + '/' + img_name))
        
        
    return imgs
class Animation:
    def __init__(self, images,img_dur=5, loop=True):
        self.images = images
        self.img_dur = img_dur
        self.loop = loop
        self.done = False
        self.frame = -1
         
    def copy(self):
        return Animation(self.images, self.img_dur, self.loop)
    def update(self):
      if self.loop:
        self.frame=(self.frame+1)%(self.img_dur*len(self.images))
         
      else: 
        if(self.frame<self.img_dur*len(self.images)-1):
           self.frame=self.frame+1
        else:
          self.done=True
          
                              
                                   
         
    def img(self):
        
       return self.images[self.frame // self.img_dur]