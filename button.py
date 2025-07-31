import pygame
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    def __init__(self, game: 'AlienInvasion', msg: str) -> None:
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        # Load custom font
        self.font = pygame.font.Font(self.settings.font_file, 40)

        # Load Play button image
        self.button_image = pygame.image.load(self.settings.button_image)
        self.button_image = pygame.transform.scale(
            self.button_image,
            (self.settings.button_w, self.settings.button_h)
        )
        self.button_rect = self.button_image.get_rect()
        self.button_rect.center = self.screen_rect.center

        # Render text message
        self._prep_msg(msg)

    def _prep_msg(self, msg: str):
        """Render the message text and center it on the button."""
        self.msg_image = self.font.render(msg, True, (255, 255, 255))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.button_rect.center

    def draw(self) -> None:
        """Draw the button image and then the message."""
        self.screen.blit(self.button_image, self.button_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos) -> bool:
        """Check if the play button was clicked."""
        return self.button_rect.collidepoint(mouse_pos)
