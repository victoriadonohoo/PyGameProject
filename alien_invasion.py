import sys 
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien 

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # initializes the background settings pygame needs to function properly 
        pygame.init()
        # create an instance of settings
        self.settings = Settings()
        # we assign an object (surface) to self.screen that formats the display window 
        # when the game's animation loop is activated by the run_game method the surface will be redrawn on every pass 
        #   through the loop based on user input. 
        # FULLSCREEN mode - tells pygame to figure out a windpw size that fills the screen 
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # update the settings object after the screen is created using the width and height attributes 
        #   of the screens rect
        self.settings.screen_width = self.screen.get_rect().width 
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # assign the ship instance to self.ship 
        # the argument self refers to the current instance of AlienInvasion
        # this gives the ship access to the game's resources 
        self.ship = Ship(self)

        #create the group to store bullets in 
        self.bullets = pygame.sprite.Group()

        #create the group to store aliens in 
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # set the background color to light grey
        self.bg_color = (230, 230, 230)
    # create check_events method to simplify run_game() and isolate the event management loop.

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        # if user presses right arrow key, game moves the ship to the right 
        if event.key == pygame.K_RIGHT:
            #set moving_right to true (indirectly moves ship to the right)
            self.ship.moving_right = True 
        # if user presses left arrow key, game moves ship to the left 
        elif event.key == pygame.K_LEFT:
            # set moving_left to true
            self.ship.moving_left = True
        # press Q to exit 
        elif event.key == pygame.K_q:
            sys.exit()
        # when space bar is pressed, we call _fire_bullet()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # when the player releases the key, we set moving_right and moving_left to false
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if  len(self.bullets) < self.settings.bullets_allowed:
            # create an instance of Bullet 
            new_bullet = Bullet(self)
            # add the instance to the bullets group
            self.bullets.add(new_bullet)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        #  the event loop makes our program respond to events and perform appropriate tasks depending on the 
        #       kinds of events that occur  
        # the function pygame.event.get() returns a list of events that have taken place since the last time 
        #   the function was called. 
        # Any mouse movement or keyboard clicks are events.
        for event in pygame.event.get():
            # when user clicks the game windows close button, a pygame.QUIT event is detected and we call sys.exit() 
            #   to exit the game  
            if event.type == pygame.QUIT:
                sys.exit()
            # checks if user pressed keys 
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # redraw the screen during each pass through the loop - argument is from the settings class
        self.screen.fill(self.settings.bg_color)
        
        # placed here so image appears on top of the background 
        # draw the ship on the screen 
        self.ship.blitme()

        # loop through the sprites in bullets and call draw_bullet() on each one
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # make an alien appear 
        self.aliens.draw(self.screen)

        # make the most recently drawn screen visible - display is updated continuously to show the new positions of the game 
        #   and hide old ones, creating illusion of smooth movement
        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions 
        # call update ship method 
        self.bullets.update()
        # get rid of bullets that disappeared 
        # allows us to modify bullets inside the loop
        for bullet in self.bullets.copy():
            # check if the bullet has disappeared 
            if bullet.rect.bottom <= 0:
                # if it has we remove it from bullets
                self.bullets.remove(bullet)
            # print how many bullets currently exist in the game and verify that they're being deleted when they reach the 
            #   top of the screen 
        print(len(self.bullets))
    
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # make an alien 
        # create an instance of an alien and adding it to the group 
        alien = Alien(self)
        self.aliens.add(alien)

    def run_game(self):
        """Start the main loop for the game."""
        # run_game() method controls the game and the while loop will run continuously 
        while True:
            # call check events method 
            self._check_events()
            # call update method from ship file 
            self.ship.update()
            # call update bullets method 
            self._update_bullets()
            # call update events method
            self._update_screen()
if __name__ == '__main__':
    # make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()