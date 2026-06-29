import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet army."""

    def __init__(self, ai_game):
        """
        Initialize the alien instance, load its visual bitmap texture,
        and establish its baseline grid position at the top-left region.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """
        Evaluate horizontal screen bounding limits to detect collision.
        Returns True if the asset rect reaches or exceeds the left or right perimeter.
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """
        Execute positional displacement translations across the screen.
        Advances horizontal coordinate offsets according to speed and direction constants.
        """
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x