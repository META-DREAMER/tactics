from powerups.base_powerup import powerup
import unit, helper, powerups
from tiles import Tile
import pygame

class attack_powerup(powerup):
    """
    The powerup that enhances unit speed.
    
    - Increases speed of tactical unit by 2
    """

    sprite = pygame.image.load("assets/Damage_PUP.png")

    def __init__(self, **keywords):
        #set the sprite image
        self._base_image = attack_powerup.sprite

        #load the base class
        super().__init__(**keywords)


        #set unit specific things.
        self.type = "attack_powerup"

    def activate_powerup(self):
        """
        Upgrades the damage of unit at given tile position by 2
        """
        #get unit at position of powerup
        powerup_unit = unit.base_unit.BaseUnit.get_unit_at_pos(self.tile_pos)

        #increase damage of the unit by 2 if its not a transport unit
        if not (powerup_unit.type == "Transport"):
            powerup_unit.damage += 2

        #remove the powerup
        self.deactivate()

powerups.powerup_types["attack_powerup"] = attack_powerup