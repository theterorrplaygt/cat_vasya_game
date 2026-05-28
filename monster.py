from unit import Unit


class Monster(Unit):
    def __init__(self, strength: int, dexterity: int, constitution: int,
                 wisdom: int, intelligence: int, charisma: int) -> None:
        super().__init__(strength, dexterity, constitution,
                         wisdom, intelligence, charisma)
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self) -> int:
        return self.constitution * 8 + self.strength // 3

    def calculate_damage(self) -> int:
        return int(self.strength * 2 + self.constitution // 5)

    def calculate_defense(self) -> int:
        return int(self.constitution * 1.2 + self.strength // 5)