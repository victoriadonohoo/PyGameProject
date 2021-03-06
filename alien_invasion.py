import sys 
import pygame
from settings import Settings

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

        # set the background color to light grey
        self.bg_color = (230, 230, 230)
    def run_game(self):
        """Start the main loop for the game."""
        # run_game() method controls the game and the while loop will run continuously 
        while True:

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
            # redraw the screen during each pass through the loop - argument is from the settings class
            self.screen.fill(self.settings.bg_color)
            # make the most recently drawn screen visible - display is updated continuously to show the new positions of the game 
            #   and hide old ones, creating illusion of smooth movement
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()