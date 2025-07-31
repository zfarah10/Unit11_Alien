from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats():

    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self) -> None:
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions) -> None:
        # update score
        self._update_score(collisions)

        # update max_score
        self._update_max_score()
        # update hi_score

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f'Max:  {self.max_score}')
    
    
    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += self.settings.alien_points
        # print(f'Basic:  {self.score}')

    def update_level(self) -> None:
        self.level += 1
        print (self.level)