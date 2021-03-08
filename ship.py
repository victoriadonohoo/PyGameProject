import pygame 

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position."""
        # assign the screen to an attribute of ship 
        self.screen = ai_game.screen

        # create a settings attribute for Ship so we can use it in update()
        self.settings = ai_game.settings

        # access the the screens rect attribute using the get_rect() method so we can place the image in the right 
        #   place on the screen 
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen by assigning the midbottom attribute of a rect 
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal position 
        self.x = float(self.rect.x)

        # initialize the moving_right attribute  
        # movement flag 
        self.moving_right = False 
        # initialize the moving_left attribute 
        self.moving_left = False 

    # method that moves the ship right if the flag is true 
    def update(self):
        """Update the ship's position based on the movement flag."""
        # value of self.x is updated based on the amount stored in settings.ship_speed 
        # update the ships x value not the rect 
        # checks the position of the ship before changing the value of self.x
        # if the x cordinate of the right edge of the ships rect is less than the value 
        #   returned by self.screen_rect.right, the ship hasnt reached the edge of the screen.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # two seperate if statements makes movements more accurate when switching from right to left 
        # if the value of the left side of the rect is greater than zero, the ship hasn't reached 
        #   the left edge of the screen 
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed 
        
        # update rect object
        # rect object controls the position of the ship ( only the integer portion of self.x 
        # will be stored in self.rect.x )
        self.rect.x = self.x 

    def blitme(self):
        """Draw the ship at its current location."""
        # draws the image to the screen at the specified position of self.rect
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom 
        # reset self.x attribute to track the ship's exact position 
        self.x = float(self.rect.x)

        # we don't make more than one ship, we just recenter the ship after it has been hit 
        
        

