import pygame 
# needed because we write text to the screen 
import pygame.font 
from pygame.sprite import Group 
from ship import Ship 

class Scoreboard:
    """A class to report scoring information."""
    # we need ai_game parameter so it can access the settings, screen, and stats objects 
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats 

        # font settings for scoring info 
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial score images 
        self.prep_score()
        # show high schore on scoreboard 
        self.prep_high_score()
        # show level on scoreboard 
        self.prep_level()
        # show how many ships on scoreboard 
        self.prep_ships()
    
    def prep_score(self):
        """Turn the score into a rendered image."""

        # round function rounds value to nearest 10, 100, 1000 because we pass a negative number as the second argument 
        # stores value in rounded_score
        rounded_score = round(self.stats.score, -1)
        # insert commas into numbers when converting numerical value to a string 
        score_str = "{:,}".format(rounded_score)
        # turn the numerical value into a string 
        score_str = str(self.stats.score)
        # pass this string to render() which creates the image ( pass the background color and text color to render )
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # display the score at the top right of the screen 
        # create rect 
        self.score_rect = self.score_image.get_rect()
        # sets right edge of rect 20 pixels from the  right edge of the screen 
        self.score_rect.right = self.screen_rect.right - 20 
        # place the top edge 20 pixels down from the screen 
        self.score_rect.top = 20 

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        # round high score to the nearest 10 
        high_score = round(self.stats.high_score, -1)
        # format with commas 
        high_score_str = "{:,}".format(high_score)
        # generate an image for high score 
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # center the high score at the top of the screen 
        self.high_score_rect = self.high_score_image.get_rect()
        # center the high score rect horizontally 
        self.high_score_rect.centerx = self.screen_rect.centerx 
        # sets top attribute to match the top of the score image 
        self.high_score_rect.top = self.score_rect.top 

    def prep_level(self):
        """Turn the level into a rendered image."""
        # converts value in stats.level to a str and sets level_str = to that 
        level_str = str(self.stats.level)
        # generate an image for the level from the value store in stats.level 
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # position the level below the score 
        self.level_rect = self.level_image.get_rect()
        # sets the images right attribute to match the scores right attribute 
        self.level_rect.right = self.score_rect.right 
        # sets top attribute 10 pixels beneath the bottom of the score image 
        #   leave space between score and level 
        self.level_rect.top = self.score_rect.bottom + 10 

    def prep_ships(self):
        """Show how many ships are left."""
        # creates an empty group to hold the ship instances 
        self.ships = Group()
        # loop runs once for every ship the player has left to fill the group 
        for ship_number in range(self.stats.ships_left):
            #create a new ship inside group 
            ship = Ship(self.ai_game)
            # set x coordinate so that ships appear next to eachother with a 10 pixel margin on 
            #   the left side of the group of ships 
            ship.rect.x = 10 + ship_number * ship.rect.width 
            # set y coordinate 10 pixels down from the top of the screen so ships appear in 
            #   upper left corner 
            ship.rect.y = 10 
            # add each new ship to the group of ships 
            self.ships.add(ship)
        

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            # update high scores image 
            self.prep_high_score()

    def show_score(self):
        """Draw the scores, level, and ships to the screen."""
        # draw the score to the screen to a specific location specified in rect 
        self.screen.blit(self.score_image, self.score_rect)
        # draw the high score to the screen to a specific location specified in rect 
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # draw the level to the screen to a location specified in rect 
        self.screen.blit(self.level_image, self.level_rect)
        # draw ship to the screen 
        self.ships.draw(self.screen)

