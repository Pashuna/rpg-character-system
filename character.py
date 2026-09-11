class Character:
    def __init__(self, name: str, health: int, attack_power: int) -> None:
        if health <= 0 or attack_power <= 0:
            raise ValueError("Health and attack power must be positive")
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.level = 1
        self.experience = 0

    def attack(self, other: "Character", damage: int | None = None) -> None:
        if not other.is_alive():
            print(f"{other.name} is dead!")
            return
        old_health = other.health
        if damage is None:
            damage = self.attack_power

        other.take_damage(damage)

        print(f"{self.name} attacked {other.name} for"
              f" {old_health - other.health} damage!")
        if other.health == 0:
            self.experience += 50
            self.level_up()

    def level_up(self) -> None:
        while self.experience >= 100:
            self.experience -= 100
            self.level += 1
            self.health += 20
            self.attack_power += 5
            print(f"{self.name} reached level {self.level}!")
            print(
                f"--------\n{self.name} health +20 -> {self.health}\n"
                f"attack_power +5 -> {self.attack_power}\n--------"
            )

    def take_damage(self, damage: int) -> None:
        self.health = max(0, self.health - damage)

    def __str__(self) -> str:
        return f"{self.name} | HP: {self.health} | Attack: {self.attack_power}"

    def is_alive(self) -> bool:
        return self.health > 0

    def heal(self, amount: int) -> None:
        if not self.is_alive():
            print(f"{self.name} is dead!")
            return
        self.health = min(self.max_health, self.health + amount)


class Warrior(Character):
    def __init__(self, name: str, health: int,
                 attack_power: int, armor: int) -> None:
        super().__init__(name, health, attack_power)
        self.armor = armor

    def take_damage(self, damage: int) -> None:
        actual_damage = max(0, damage - self.armor)
        super().take_damage(actual_damage)


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
        super().attack(other, special_attack)
        self.mana -= 20
