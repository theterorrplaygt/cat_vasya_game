from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self, strength: int, dexterity: int, constitution: int,
                 wisdom: int, intelligence: int, charisma: int):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    @abstractmethod
    def calculate_max_health(self) -> int:
        pass

    @abstractmethod
    def calculate_damage(self) -> int:
        pass

    @abstractmethod
    def calculate_defense(self) -> int:
        pass