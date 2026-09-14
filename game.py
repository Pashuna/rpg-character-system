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
            turn_completed = self.player_turn(enemy)

            if turn_completed and enemy.is_alive():
                enemy.attack(self.player)

        if self.player.is_alive():
            print("You won!")
            print(f"Experience: {self.player.experience}")
            print(f"Level: {self.player.level}")
        else:
            print("You lost!")

    def run(self) -> None:
        while self.player.is_alive():
            self.battle()

            if not self.player.is_alive():
                break

            player_choice = input(
                "Next battle press 'Y', if you want to stop, "
                "press another key:\n"
            )
            if player_choice.strip().lower() != "y":
                break

    def player_turn(self, enemy: Enemy) -> bool:
        print(f"\n{self.player}")
        print(f"{enemy}")

        choice = input(
            "1-Attack\n"
            "2-Heal\n"
            "3-Special attack:\n"
        )

        if choice == "1":
            self.player.attack_turn(enemy)
            return True
        elif choice == "2":
            print(f"HP before heal: {self.player.health}")
            self.player.heal(20)
            print(f"HP after heal: {self.player.health}")
            return True
        elif choice == "3":
            self.player.special_attack(enemy)
            return True
        else:
            print("Invalid choice!")
            return False
