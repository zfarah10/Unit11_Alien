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

        # Ship settings
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'cool_ship.png'
        self.ship_w = 60
        self.ship_h = 70
        self.ship_speed = 5
        self.starting_ship_count = 3

        # Bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'blue_laser.png'
        self.bullet_speed = 7
        self.bullet_w = 10
        self.bullet_h = 50
        self.bullet_amount = 5

        # Sound settings
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'alien_hit_boom.mp3'

        # Alien settings
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemyBlue3.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2
        self.fleet_direction = 1  # 1 = right, -1 = left
        self.fleet_drop_speed = 40
