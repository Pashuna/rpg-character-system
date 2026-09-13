from enemy import Enemy


class Goblin(Enemy):
    def __init__(self) -> None:
        super().__init__("Goblin", 40, 10, 50)
