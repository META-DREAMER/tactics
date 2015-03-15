import pygame, unit, helper, bmpfont, effects
from pygame.sprite import Sprite

FRAME_MOVE_SPEED = 3/20
SIZE = 20

class powerup(Sprite):
    """
    The basic representation of a power up from which all other powerup types
    extend. Has a graphical representation and is stationary at specific
    locations on the map, and other units can consume it.
    
    Note: self._base_image MUST be set in subclasses! This is the tilesheet
    from which the unit renders its actual image.
    """
    
    active_units = pygame.sprite.LayeredUpdates()
    
    health_font = bmpfont.BitmapFont("assets/healthfont.png", 6, 7, 48)
    
    def __init__(self,
                 tile_x = None,
                 tile_y = None,
                 angle = 0,
                 activate = False,
                 **keywords):
        Sprite.__init__(self)

        # Take the keywords off
        self.tile_x = tile_x
        self.tile_y = tile_y
        self._angle = angle
