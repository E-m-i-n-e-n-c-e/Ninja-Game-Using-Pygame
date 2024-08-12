import sys
import pygame as p
from scripts.entities import PhysicsEntity
from scripts.utils import *

class Game:
    def __init__(self):
        p.init()
        p.display.set_caption("Ninja Game")
        self.player = PhysicsEntity(self, 'player', (0, 0), (100, 100))  # Adjust the position and size accordingly

    def run(self):

        while True:
            self.screen.fill((0, 0, 255))
            self.player.update()  # Update player position
            self.player.render(self.screen)  # Render the player
            p.display.update()
            self.clock.tick(60)

            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
