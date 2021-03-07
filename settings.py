class Settings:

    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # screen settings 
        # dimensions of the game window (1200 pixels wide / 800 pixels high)
        self.screen_width = 1200 
        self.screen_height = 800 
        
        # color 
        self.bg_color = (230, 230, 230)

        # speed of ship 
        self.ship_speed = 1.5 

        # Bullet Settings 
        self.bullet_speed = 1.0 
        self.bullet_width = 3
        self.bullet_height = 15 
        self.bullet_color = (60, 60, 60)
        # limits the player to 3 bullets at a time 
        self.bullets_allowed = 3