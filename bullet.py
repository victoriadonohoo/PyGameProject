import pygame 
from pygame.sprite import Sprite 

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color 

        # create a bullet rect at (0, 0) and then set correct position. 
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
         
        # set the bullet's midtop attribute to match the ships midtop attribute
        # makes the bullet emerge from the top of the ship 
        self.rect.midtop = ai_game.ship.rect.midtop 

        # store the bullets position as a decimal value 
        self.y = float(self.rect.y)

    # update method manages the bullets position 
    def update(self):
        """Move the bullet up the screen."""
        # update the decimal position of the bullet 
        # when a bullet is fired it moves up the screen (decreasing y coordinate value)
        self.y -= self.settings.bullet_speed
        # update the rect position
        # use self.y value to set self.rect.y 
        self.rect.y = self.y 

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        # fills the part of the screen defined by the bullets rect with the 
        #   color stored in self.color
        pygame.draw.rect(self.screen, self.color, self.rect)
