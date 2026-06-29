class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Игра запускается в неактивном состоянии (ожидает клика по кнопке Play)
        self.game_active = False

        # Абсолютный рекорд (High Score) инициализируется один раз и не обнуляется
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit  # Восстановление жизней
        self.score = 0                              # Обнуление текущих очков
        self.level = 1                              # Возврат на 1 уровень