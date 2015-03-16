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
    
    active_powerups = pygame.sprite.LayeredUpdates()
    
    def __init__(self,
                 tile_x = None,
                 tile_y = None,
                 activate = False,
                 **keywords):
        
        Sprite.__init__(self)

        # Take the keywords off
        self.tile_x = tile_x
        self.tile_y = tile_y

        #set default active state to be false
        self._active = False

        #set required pygame things.
        self.image = None
        self.rect = pygame.Rect(0, 0, SIZE, SIZE)
        self._update_image()
        
        if activate:
            self.activate()


    @staticmethod
    def get_powerup_at_pos(pos):
        """
        Returns the active powerup at the given tile position, or None if no powerup
        is present.
        """
        for p in powerup.active_powerups:
            if (p.tile_x, p.tile_y) == pos:
                return p
        
        return None
    
    @property
    def active(self):
        """
        Returns whether this is active.
        """
        return self._active

    @property
    def tile_pos(self):
        """
        Returns the unit's tile position.
        """
        return (self.tile_x, self.tile_y)

    def _update_image(self):
        """
        Re-renders the powerup's image.
        """
        # Pick out the right sprite depending on the team
        subrect = pygame.Rect(0,
                              0,
                              self.rect.w,
                              self.rect.h)
        try:
            subsurf = self._base_image.subsurface(subrect)
        except ValueError:
            # No sprite for this team
            raise ValueError(
                "Class {} does not have a sprite for team {}!".format(
                    self.__class__.__name__, self.team))
        except AttributeError:
            # No image is loaded
            return
        
        # Rotate the sprite
        self.image = pygame.transform.rotate(subsurf, 0)

    def activate(self):
        """
        Adds this powerup to the active roster.
        """
        if not self._active:
            self._active = True
            powerup.active_powerups.add(self)
    
    def deactivate(self):
        """
        Removes this powerup from the active roster.
        """
        if self._active:
            self._active = False
            powerup.active_powerups.remove(self)
            print("deactivated")