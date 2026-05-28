from abc import ABC, abstractmethod


class Spell(ABC):
    def __init__(self, name: str, damage: int, mana_cost: int) -> None:
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self) -> int:
        pass


class Fireball(Spell):
    def __init__(self) -> None:
        super().__init__("Огненный шар", 35, 15)

    def cast(self) -> int:
        return self.damage


class IceLance(Spell):
    def __init__(self) -> None:
        super().__init__("Ледяное копьё", 25, 10)

    def cast(self) -> int:
        return self.damage


class LightningBolt(Spell):
    def __init__(self) -> None:
        super().__init__("Удар молнии", 40, 20)

    def cast(self) -> int:
        return self.damage