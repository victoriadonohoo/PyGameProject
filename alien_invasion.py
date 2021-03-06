import sys 
import pygame
from settings import Settings
from ship import Ship

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
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # assign the ship instance to self.ship 
        # the argument self refers to the current instance of AlienInvasion
        # this gives the ship access to the game's resources 
        self.ship = Ship(self)

        # set the background color to light grey
        self.bg_color = (230, 230, 230)
    # create check_events method to simplify run_game() and isolate the event management loop.
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
                # if user presses right arrow key, game moves the ship to the right 
                if event.key == pygame.K_RIGHT:
                    # set moving_right to true (indirectly moves ship to the right)
                    self.ship.moving_right = True 
                # if user presses left arrow key, game moves ship to the left 
                elif event.key == pygame.K_LEFT:
                    # set moving_left to true
                    self.ship.moving_left = True
            # when the player releases the key, we set moving_right and moving_left to false
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # redraw the screen during each pass through the loop - argument is from the settings class
        self.screen.fill(self.settings.bg_color)
        # placed here so image appears on top of the background 
        # draw the ship on the screen 
        self.ship.blitme()
        # make the most recently drawn screen visible - display is updated continuously to show the new positions of the game 
        #   and hide old ones, creating illusion of smooth movement
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        # run_game() method controls the game and the while loop will run continuously 
        while True:
            # call check events method 
            self._check_events()
            # call update method from ship file 
            self.ship.update()
            # call update events method
            self._update_screen()
if __name__ == '__main__':
    # make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()