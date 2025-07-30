"""
Lab12_zfarah_2.py
Author: Zakarie Farah
Date: July 21, 2025
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from time import sleep
from game_stats import GameStats
from button import Button

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_custom_fleet()

        self.running = True
        self.game_active = False
        self.play_button = Button(self, 'Play')
        self.clock = pygame.time.Clock()

    def run_game(self):
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.ship.arsenal.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        if self.ship.check_collisions(self.alien_fleet.fleet) or self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
        if self.alien_fleet.check_collisions(self.ship.arsenal.arsenal):
            self.impact_sound.play()
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()

    def _check_game_status(self):
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_custom_fleet()

    def restart_game(self):
        # setting up dynamic Settings
        # reset Game stats
        # update HUD scores
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.arsenal.draw()
        self.ship.draw()
        self.alien_fleet.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
        elif event.key == pygame.K_q:
            self._quit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _quit(self):
        self.running = False
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
