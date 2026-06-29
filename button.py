import pygame.font

class Button:
    """A class to build, customize, and render interactive UI buttons."""

    def __init__(self, ai_game, msg):
        """
        Initialize button attributes, set dimensional constraints, 
        define color properties, and calculate center alignment positions.
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """
        Convert a raw text string into a rendered graphical surface image 
        and accurately center it over the button's background container.
        """
        self.msg_image = self.font.render(msg, True, self.text_color,
                 self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        Render button assets onto the display: draws the colored background 
        surface array followed by the text image layer.
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)