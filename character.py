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
        self.experience_reward = 0

    def attack(self, other: "Character", damage: int | None = None) -> bool:
        if not self.is_alive():
            print(f"{self.name} is dead!")
            return False
        if not other.is_alive():
            print(f"{other.name} is dead!")
            return False
        old_health = other.health
        if damage is None:
            damage = self.attack_power

        other.take_damage(damage)

        print(f"{self.name} attacked {other.name} for"
              f" {old_health - other.health} damage!")
        if other.health == 0:
            print(f"{other.name} is dead!")
            self.experience += other.experience_reward
            self.level_up()
        return True

    def attack_turn(self, other: "Character") -> None:
        self.attack(other)

    def special_attack(self, other: "Character") -> None:
        self.attack(other)

    def level_up(self) -> int:
        levels_gained = 0
        while self.experience >= 100:
            self.experience -= 100
            self.level += 1
            self.health += 20
            self.max_health += 20
            self.attack_power += 5
            levels_gained += 1
            print(f"{self.name} reached level {self.level}!")
            print(
                f"--------\n{self.name} health +20 -> {self.health}\n"
                f"attack_power +5 -> {self.attack_power}\n--------"
            )
        return levels_gained

    def take_damage(self, damage: int) -> None:
        self.health = max(0, self.health - damage)

    def __str__(self) -> str:
        return (
            f"{self.name} | HP: {self.health}/{self.max_health} | "
            f"Attack: {self.attack_power}"
        )

    def is_alive(self) -> bool:
        return self.health > 0

    def heal(self, amount: int) -> None:
        if not self.is_alive():
            print(f"{self.name} is dead!")
            return
        if amount <= 0:
            raise ValueError("Heal amount must be positive")
        self.health = min(self.max_health, self.health + amount)
