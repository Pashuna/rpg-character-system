from character import Character


class Mage(Character):
    def __init__(self, name: str, health: int,
                 attack_power: int, mana: int) -> None:
        super().__init__(name, health, attack_power)
        self.mana = mana

    def fireball(self, other: "Character") -> None:
        if self.mana < 20:
            print("Not enough mana!")
            return

        special_attack = self.attack_power * 2
        attack_successful = super().attack(other, special_attack)
        if attack_successful:
            self.mana -= 20

    def attack_turn(self, other: "Character") -> None:
        self.fireball(other)
