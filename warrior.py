import random

from character import Character


class Warrior(Character):
    def __init__(self, name: str, health: int,
                 attack_power: int, armor: int) -> None:
        super().__init__(name, health, attack_power)
        self.armor = armor

    def take_damage(self, damage: int) -> None:
        actual_damage = max(0, damage - self.armor)
        super().take_damage(actual_damage)

    def power_attack(self, other: "Character") -> None:
        if random.randint(0, 1) == 1:
            special_attack = self.attack_power * 2
            super().attack(other, special_attack)

        else:
            super().attack(other)
