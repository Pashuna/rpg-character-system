from character import Character


class Enemy(Character):
    def __init__(
        self,
        name: str,
        health: int,
        attack_power: int,
        experience_reward: int
    ) -> None:
        super().__init__(name, health, attack_power)
        self.experience_reward = experience_reward
