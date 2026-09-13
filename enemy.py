from character import Character


class Enemy(Character):
    def __init__(self, name, health,
                 attack_power, experience_reward) -> None:
        super().__init__(name, health, attack_power)
        self.experience_reward = experience_reward
