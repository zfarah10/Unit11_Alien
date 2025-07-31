"""
Author: Zakarie Farah
Purpose: Stores all configuration and asset paths for the custom Alien Invasion game.
Date: July 17, 2025
"""

from pathlib import Path

class Settings:
    def __init__(self) -> None:
        # Game window
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        # Background
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'space_background.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        # Ship settings
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'cool_ship.png'
        self.ship_w = 60
        self.ship_h = 70

        # Bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'blue_laser.png'

        # Sound settings
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'alien_hit_boom.mp3'

        # Alien settings
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemyBlue3.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1  # 1 = right, -1 = left

        # Button settings
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,50)
        self.button_image = Path.cwd() / 'Assets' / 'images' / 'PlayButton.png'

        # Text and font
        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'fonts' / 'Silkscreen' / 'Roman-Regular.ttf'

    def initialize_dynamic_settings(self) -> None:
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 10
        self.bullet_h = 50
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 5
        self.fleet_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self) -> None:
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
