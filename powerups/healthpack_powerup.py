from powerups.base_powerup import powerup
import unit, helper, powerups
from tiles import Tile
import pygame

class healthpack_powerup(powerup):
    """
    The powerup that enhances unit speed.
    
    - Increases speed of tactical unit by 2
    """

    sprite = pygame.image.load("assets/Health_PUP.png")

    def __init__(self, **keywords):
        #set the sprite image
        self._base_image = healthpack_powerup.sprite

        #load the base class
        super().__init__(**keywords)


        #set powerup specific things.
        self.type = "healthpack_powerup"

    def activate_powerup(self):
        """
        Upgrades the health of unit that picked up the powerup by 10 upto its max health
        """
        #get unit at position of powerup
        powerup_unit = unit.base_unit.BaseUnit.get_unit_at_pos(self.tile_pos)

        #add 10 to units health
        powerup_unit.health += 10

        #cap health at max
        if (powerup_unit.health > powerup_unit.max_health):
            powerup_unit.health = powerup_unit.max_health

        #redraw unit and remove powerup
        powerup_unit._update_image()
        self.deactivate()

powerups.powerup_types["healthpack_powerup"] = healthpack_powerup