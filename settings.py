class Settings:

    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings."""
        # screen settings 
        # dimensions of the game window (1200 pixels wide / 800 pixels high)
        self.screen_width = 1200 
        self.screen_height = 800 
        self.bg_color = (230, 230, 230)

        # Ship settings 
        self.ship_limit = 3

        # Bullet Settings 
        # bullet speed 
        self.bullet_width = 3
        self.bullet_height = 15 
        self.bullet_color = (60, 60, 60)
        # limits the player to 3 bullets at a time 
        self.bullets_allowed = 3

        # Alien settings 
        # how quickly the fleet drops down the screen each time an alien reaches either edge 
        self.fleet_drop_speed = 10 
    
        # how quickly the game speeds up 
        self.speedup_scale = 1.1 

        # how quickly alien point values increase 
        self.score_scale = 1.5 

        # initialize the values for attributes 
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game. """
        self.ship_speed = 1.5 
        self.bullet_speed = 1.5 
        self.alien_speed = 1.0 
        # fleet direction of 1 represents right (addition to x coordinate value); -1 represents left (subtraction from x coordinate value)
        # we dont use 'left' or 'right' because we would need if-elif statements testing direction 
        # use 1 and -1 because there are only two directions 
        self.fleet_direction = 1 

        # increase each aliens point value as the game progresses 
        #   we place it in initialize_dynamic_settings() to make sure this is reset every time a new game starts 
        self.alien_points = 50 

    def increase_speed(self):
        """Increase the speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        # increase the point value of each hit 
        self.alien_points = int(self.alien_points * self.score_scale)
        # see the value of each alien 
        print(self.alien_points)
