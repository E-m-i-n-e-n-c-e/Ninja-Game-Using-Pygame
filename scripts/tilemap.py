import pygame
NEIGHBOUR_OFFSETS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (0, 0), (1, -1), (1, 0), (1, 1))
PHYSICS_TILES={'grass','stone','water','sand','dirt','wood','tree','rock','air'}

class Tile:
    def __init__(self, type, variant, pos):
        self.type = type
        self.variant = variant
        self.pos = pos

class TileMap:
    def __init__(self, game, tile_size=16):
        self.tile_size = tile_size
        self.game = game
        self.tileMap = {}
        self.offgrid_tiles = []
        for i in range(0, 10):
            self.tileMap[str(3+i)+";10"] = Tile('grass', 1, (3+i, 10))
            self.tileMap[str(10)+";"+str(5+i)] = Tile('stone', 1, (10, 5+i))

    def tiles_around(self, rect):
        tiles = []
        pos = [(int(rect.left), int(rect.bottom)), (int(rect.left), int(rect.top)), (int(rect.right), int(rect.top)), (int(rect.right), int(rect.bottom))]

        for i in range(4):
            pos[i] = (int(pos[i][0] // self.tile_size), int(pos[i][1] // self.tile_size))
            for offset in NEIGHBOUR_OFFSETS:
                key = f"{pos[i][0] + offset[0]};{pos[i][1] + offset[1]}"
                if key in self.tileMap:
                    tiles.append(self.tileMap[key])

        for i in range(int(rect.left) // self.tile_size, (int(rect.right) // self.tile_size) + 1):
            for j in range(int(rect.top )// self.tile_size, (int(rect.bottom) // self.tile_size) + 1):
                # for offset in NEIGHBOUR_OFFSETS:
                    key = f"{i};{j}"
                    if key in self.tileMap:
                        tiles.append(self.tileMap[key])

        tiles = list(set(tiles))  # Remove duplicates by converting to set and back to list
        return tiles

             

    def physics_rects_around(self, rect):
      rects=[]
      for tile in self.tiles_around(rect):
        if tile.type in PHYSICS_TILES:
          rects.append(pygame.Rect(tile.pos[0]*self.tile_size, tile.pos[1]*self.tile_size, self.tile_size, self.tile_size))
        
      return rects
    def render(self, surf,offset=(0,0)):
       
        for x in range(int(offset[0]//self.tile_size),int((offset[0]+self.game.display.get_width())//self.tile_size+1)):
          for y in range(int(offset[1]//self.tile_size),int((offset[1]+self.game.display.get_height())//self.tile_size+1)):
            if f"{x};{y}" in self.tileMap:
              surf.blit(self.game.assets[self.tileMap[f"{x};{y}"].type][self.tileMap[f"{x};{y}"].variant], (x*self.tile_size-offset[0],y*self.tile_size-offset[1]))
        for loc in self.offgrid_tiles:
            tile = self.offgrid_tiles[loc]
            surf.blit(self.game.assets[tile.type][tile.variant], tile.pos[0]-offset[0],tile.pos[1]-offset[1])