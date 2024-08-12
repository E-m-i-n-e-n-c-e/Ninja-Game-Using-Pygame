  
import pygame as p

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size,acc=0.1):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.vel = [0, 0]
        self.original = self.game.assets[self.type]
        self.acc=acc
        self.update_size(self.size)
        self.collisions={'UP':False,'DOWN':False,'LEFT':False,'RIGHT':False}
        self.temp_vel=0

        self.action=''
        self.anim_offset=[-2,-3]
        self.flip=False
        self.set_action("idle")
        
    def set_action(self,action):
        if action!=self.action:
            self.action=action
            self.animation=self.game.assets[self.type+'/'+self.action].copy()
            if(action=='idle'):
                if(self.flip):
                    self.anim_offset[0]-=1.1
                else:
                    self.anim_offset[0]+=2

             
            

        
         

    def rect(self):
        return p.FRect(*self.pos, *self.game.assets[self.type].get_size() )
    
    def update_size(self,size):
        # Update the size of the image based on the original to maintain quality
        self.game.assets[self.type] = p.transform.scale(self.original, size)
        
    def update(self,tilemap, movement=(0, 0)):
        # Apply velocity and additional movement to position
        
        if(self.collisions['UP'] or self.collisions['DOWN'] ):
            self.vel[0]+=movement[0]
            # if movement[0]>0:
            #  if(self.temp_vel<0):
            #      self.temp_vel=0
            #  self.temp_vel=min(self.temp_vel+movement[0]/10,1)
            #  self.vel[0]=self.temp_vel
            #  print(self.vel[0]," ")
             
            # elif movement[0]<0:
            #  if(self.temp_vel>0):
            #      self.temp_vel=0
            #  self.temp_vel=max(self.temp_vel+movement[0]/10,-1)
            #  self.vel[0]=self.temp_vel
            #  print("yep")
            # else:
            #     self.temp_vel=0
            

        if(self.vel[0]*movement[0]<0):
                self.vel[0]=0
        if(self.vel[1]*movement[1]<0):
                self.vel[1]=0
        
        
        
        self.collisions={'UP':False,'DOWN':False,'LEFT':False,'RIGHT':False}
        # print(self.vel[0], movement[0])
    
        frame_movement = (movement[0] + self.vel[0], movement[1] + self.vel[1])
        
                
        prev_size=self.game.assets[self.type].get_size()

        
        self.pos[0] += frame_movement[0]
        if prev_size[0]!=int(self.size[0]):
            self.update_size((self.size[0],prev_size[1]))
            print(prev_size[0],self.size[0])
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(entity_rect):
            if entity_rect.colliderect(rect):
                self.game.count=self.game.jump
                if frame_movement[0] >= 0:
                    entity_rect.right = rect.left
                    self.collisions["RIGHT"]=True
                     
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions["LEFT"]=True
                     
                self.pos[0] = entity_rect.x
                self.vel[0]=0
                
        self.pos[1] += frame_movement[1]
        prev_size=self.game.assets[self.type].get_size()
        if prev_size[1]!=int(self.size[1]):
            self.update_size(self.size)
            print(prev_size[1],self.size[1])
        e_rect= self.rect()
        for rect in tilemap.physics_rects_around(e_rect):
           
            if e_rect.colliderect(rect):
                self.game.count=self.game.jump
                
                if frame_movement[1] >= 0:
                    e_rect.bottom=rect.top
                    self.collisions["DOWN"]=True
                
                if frame_movement[1] < 0:
                    e_rect.top=rect.bottom
                    self.collisions["UP"]=True
                self.pos[1]=e_rect.y
        if(self.collisions['UP'] or self.collisions['DOWN'] ):
            self.vel[1]=0 
            self.vel[0]=0
        if(self.collisions['LEFT'] or self.collisions['RIGHT'] ):
             
            self.vel[0]=0
        self.vel[1]=min(5,self.vel[1]+self.acc)
        if(movement[0]<0):
          self.flip=True
        if(movement[0]>0):
          self.flip=False
        
        self.animation.update()
        # p.draw.rect(self.game.display,(255,255,0),self.rect())
        
        



  

    def render(self, surf,offset):
        # Draw the entity on the provided surface
        img= p.transform.flip(self.animation.img(),self.flip,False)
        
        surf.blit( img, (self.pos[0]-offset[0]+self.anim_offset[0],self.pos[1]-offset[1]+self.anim_offset[1]))

    
class Player(PhysicsEntity):
        def __init__(self,game,pos,size):
            super().__init__(game,'player',pos,size)
            self.airtime=0

        def update(self, tilemap, movement=(0, 0)):
            super().update(tilemap, movement=movement)
            self.airtime+=1
            if(self.collisions['DOWN']):
                self.airtime=0
            if(self.airtime>1):
                if(movement[0]!=0):
                    self.set_action('jump')
                    if( self.collisions['RIGHT']):
                        self.anim_offset[0]=-4.5
                    if( self.collisions['LEFT']):
                        self.anim_offset[0]=-1
                else:
                    self.set_action('idle')
                    
            elif(movement[0]!=0):
                self.set_action('run')
                if(self.collisions['RIGHT']  ):
                    self.anim_offset[0]=-4
                if(self.collisions['LEFT']  ):
                    self.anim_offset[0]=-2
                
            else:
                self.set_action('idle')
                
