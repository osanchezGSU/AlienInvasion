class GameStats():
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics for Alien Invasion."""
        self.settings = ai_game.settings
        self.reset_stats()

        #High score should never reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        sel