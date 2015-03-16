from powerups.base_powerup import powerup
import unit, helper, powerups
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


        #set powerup specific things.
        self.type = "speed_powerup"


    def activate_powerup(self, pos):
        """
        Upgrades the speed of unit at given tile position by 2
        """
        powerup_unit = unit.base_unit.BaseUnit.get_unit_at_pos(pos)
        powerup_unit.speed += 2

powerups.powerup_types["speed_powerup"] = speed_powerup