import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        self.create_custom_fleet()

    
    def create_custom_fleet(self):
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        center_x = screen_w // 2
        center_y = screen_h // 4

        spacing = 50
        layers = 5

        for i in range(layers):
            # Spiral layer going right
            x = center_x + i * spacing
            y = center_y + (i % 2) * spacing
            self._create_alien(x, y)

            # Spiral layer going left
            x = center_x - i * spacing
            y = center_y + ((i + 1) % 2) * spacing
            self._create_alien(x, y)


    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space)//2)
        y_offset = int((half_screen-fleet_vertical_space)//2)
        return x_offset,y_offset


    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h) -> any:
        fleet_w = (screen_w // alien_w)
        fleet_h = ((screen_h /2)//alien_h)
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2


        return int(fleet_w), int(fleet_h)
    

    def _create_alien(self, current_x: int, current_y: int) -> None:
        new_alien = Alien(self.game, current_x, current_y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self) -> None:
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break


    def _drop_alien_fleet(self) -> None:
        for alein in self.fleet:
            alein.y += self.fleet_drop_speed

    def update_fleet(self) -> None:
        self._check_fleet_edges()
        for alien in self.fleet:
            alien.update(self.fleet_direction)


    def draw(self) -> None:
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group) -> dict[any, list]:
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self) ->None:
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self) -> bool:
        return not self.fleet