from enemy import Enemy


class Dragon(Enemy):
    def __init__(self) -> None:
        super().__init__("Dragon", 60, 15, 90)
