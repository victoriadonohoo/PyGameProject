import sys 
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # initializes the background settings pygame needs to function properly 
        pygame.init()
        # creates a display window where we will draw all the graphical elements. 
        # the argument (1200, 800) is a tuple that defines the dimensions of the game window (1200 pixels wide / 800 pixels high)
        # we assign this display window to the attribute self.screen so it will be available in all methods of the class. 
        # the object (surface) display.set_mode() represents the entire game window.
        # when the game's animation loop is activated by the run_game method the surface will be redrawn on every pass 
        #   through the loop based on user input. 
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

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
            # make the most recently drawn screen visible - display is updated continuously to show the new positions of the game 
            #   and hide old ones, creating illusion of smooth movement
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()