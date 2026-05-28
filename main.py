from character import Character
from monster import Monster
from spell import Fireball, IceLance, LightningBolt


def print_separator() -> None:
    print("-" * 60)


def print_unit_stats(unit, name: str) -> None:
    if hasattr(unit, 'max_mana'):
        print(f"{name}: HP={unit.current_health}/{unit.max_health}, "
              f"Мана={unit.mana}/{unit.max_mana}, Урон={unit.damage}, Защита={unit.defense}")
    else:
        print(f"{name}: HP={unit.current_health}/{unit.max_health}, "
              f"Урон={unit.damage}, Защита={unit.defense}")


def main() -> None:
    warrior = Character(18, 12, 16, 8, 10, 12, 'warrior')
    mage = Character(10, 14, 12, 18, 20, 16, 'mage')
    hunter = Character(14, 18, 14, 12, 12, 14, 'hunter')
    dragon = Monster(12, 10, 12, 6, 6, 6)

    fireball = Fireball()          
    ice_lance = IceLance()        
    lightning = LightningBolt()    
    warrior.add_spell(fireball)
    warrior.add_spell(ice_lance)
    mage.add_spell(fireball)
    mage.add_spell(lightning)

    print_separator()
    print_unit_stats(warrior, "Воин")
    print_unit_stats(mage, "Маг")
    print_unit_stats(hunter, "Охотник")
    print_unit_stats(dragon, "Дракон")
    print_separator()

    print("\n--- Воин колдует ---")
    try:
        dmg = warrior.cast_spell(0)
        print(f"Воин применил {warrior.spells[0].name}, урон {dmg}. Осталось маны: {warrior.mana}")
        print(f"Попытка второго заклинания: {warrior.cast_spell(1)} урона. Остаток маны: {warrior.mana}")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- Маг колдует ---")
    try:
        dmg = mage.cast_spell(1)
        print(f"Маг применил {mage.spells[1].name}, урон {dmg}. Осталось маны: {mage.mana}")
        print(f"Маг пробует то же заклинание снова: {mage.cast_spell(1)} урона. Остаток маны: {mage.mana}")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n--- Испытание нехватки маны ---")
    try:
        warrior.cast_spell(0)
    except Exception as e:
        print(f"Воин: {e}")

    try:
        mage.cast_spell(0)
    except Exception as e:
        print(f"Маг: {e}")

    print_separator()
    print("Финальные характеристики:")
    print_unit_stats(warrior, "Воин")
    print_unit_stats(mage, "Маг")
    print_separator()


if __name__ == "__main__":
    main()