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


        #set powerup specific things.
        self.type = "speed_powerup"

powerups.powerup_types["speed_powerup"] = speed_powerup