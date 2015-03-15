from unit.water_unit import WaterUnit
import unit, helper, effects
from tiles import Tile
import pygame

class PT_boat(WaterUnit):
    """
    A Super fast boat. Basically, the underdog of the ocean. Causes less damage
    but can quickly get away with it. 
    
    Armour: Medium
    Speed: Super fast
    Range: High
    Damage: Medium
    
    Other notes:
    - Despite its medium stats, this unit is smart, quick and dependable.
    """
    sprite = pygame.image.load("assets/PT-boat.png")
    
    def __init__(self, **keywords):
        #load the image for the base class.
        self._base_image = PT_boat.sprite

        #load the base class
        super().__init__(**keywords)
        
        #sounds
        self.hit_sound = "ArtilleryFire"

        #set unit specific things.
        self.type = "PT_boat"
        self.speed = 12
        self.max_atk_range = 6
        self.damage = 4
        self.defense = 1
        self.hit_effect = effects.Explosion

        self.health = 12
        self.max_health = self.health

        self._update_image()

unit.unit_types["PT_boat"] = PT_boat
