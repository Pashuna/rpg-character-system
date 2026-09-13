import random

from character import Character
from enemy import Enemy
from goblin import Goblin
from dragon import Dragon


class Game:
    def __init__(self, player: Character) -> None:
        self.player = player

    @staticmethod
    def create_random_enemy() -> Enemy:
        enemy_class = random.choice([Goblin, Dragon])
        return enemy_class()


    def battle(self) -> None:
        enemy = self.create_random_enemy()
        while enemy.is_alive() and self.player.is_alive():
            self.player.attack_turn(enemy)
            if enemy.is_alive():
                enemy.attack(self.player)