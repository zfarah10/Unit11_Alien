"""
Author: Zakarie Farah
Purpose: Custom alien invasion game
Date: July 17, 2025 
"""

from pathlib import Path
class Settings:
    def __init__(self) -> None:
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'space_background.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'cool_ship.png'
        self.ship_w = 60
        self.ship_h = 70
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'blue_laser.png'
        self.bullet_speed = 7
        self.bullet_w = 10
        self.bullet_h = 50
        self.bullet_amount = 5

        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'