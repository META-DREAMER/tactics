from powerups.base_powerup import powerup
import unit, helper
from tiles import Tile
import pygame

class speed_powerup(powerup):
    """
    The powerup that enhances unit speed.
    
    - Increases speed of tactical unit by 2
    """

    sprite = pygame.image.load("assets/Speed_PUP.png")

    def __init__(self, **keywords):
        #set the sprite image
        self._base_image = speed_powerup.sprite

        #load the base class
        super().__init__(**keywords)


        #set unit specific things.
        self.type = "Speed Powerup"
        
    def speed_up(self, tile, pos):
        """
        Returns whether or not this unit can move over a certain tile.
        """
        # Return default
        if not super().is_passable(tile, pos):
            return False
            
        # We can't pass through enemy units.
        u = BaseUnit.get_unit_at_pos(pos)
        if u and u.team != self.team and isinstance(u, GroundUnit):
            return False
        
        #ground units can't travel over water or through walls
        if (tile.type == 'water' or tile.type == 'wall'):
            return False

        return True

