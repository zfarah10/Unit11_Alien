import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:

    def __init__(self, game: 'AlienInvasion', msg) -> None:
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.button_font_size)
        self.rect = pygame.Rect(0,0,self.settings.button_w, self.settings.bullet_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg) -> None:
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self) -> None:
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos) -> bool:
        return self.rect.collidepoint(mouse_pos)