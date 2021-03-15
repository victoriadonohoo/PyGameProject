class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # start alien invasion in inactive state 
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""

        # tells us when the player has run out of ships 
        self.ships_left = self.settings.ship_limit 

    