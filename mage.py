from character import Character


class Mage(Character):
    def __init__(
        self,
        name: str,
        health: int,
        attack_power: int,
        mana: int
    ) -> None:
        super().__init__(name, health, attack_power)
        self.mana = mana

    def fireball(self, other: "Character") -> None:
        if self.mana < 20:
            print("Not enough mana!")
            return

        damage = self.attack_power * 2
        attack_successful = super().attack(other, damage)

        if attack_successful:
            self.mana -= 20

    def attack_turn(self, other: "Character") -> None:
        self.attack(other)

    def special_attack(self, other: "Character") -> None:
        self.fireball(other)

    def level_up(self) -> None:
        levels_gained = super().level_up()
        self.mana += 20 * levels_gained

    def __str__(self) -> str:
        return (
            f"{self.name} | HP: {self.health}/{self.max_health} | "
            f"Attack: {self.attack_power} | Mana: {self.mana}"
        )
