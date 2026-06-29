import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage projectiles fired from the player ship model."""

    def __init__(self, ai_game):
        """
        Initialize the bullet instance at the ship's current position.
        Sets up the bounding box geometry and captures precise decimal vertical coordinates.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """
        Advance the linear position of the projectile upward.
        Translates vertical coordinate offsets and synchronizes the tracking rect container.
        """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Render the surface geometry structure onto the active game display screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)