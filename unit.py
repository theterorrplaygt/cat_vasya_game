from abc import ABC, abstractmethod
from typing import List


class Unit(ABC):
    def __init__(self, strength: int, dexterity: int, constitution: int,
                 wisdom: int, intelligence: int, charisma: int) -> None:
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.spells: List['Spell'] = []
        self.mana: int = 0

    @abstractmethod
    def calculate_max_health(self) -> int:
        pass

    @abstractmethod
    def calculate_damage(self) -> int:
        pass

    @abstractmethod
    def calculate_defense(self) -> int:
        pass

    def add_spell(self, spell: 'Spell') -> None:
        self.spells.append(spell)

    def cast_spell(self, index: int) -> int:
        if index < 0 or index >= len(self.spells):
            raise IndexError("Неверный индекс заклинания")
        spell = self.spells[index]
        if self.mana < spell.mana_cost:
            raise ValueError(f"Недостаточно маны. Нужно {spell.mana_cost}, доступно {self.mana}")
        self.mana -= spell.mana_cost
        return spell.cast()