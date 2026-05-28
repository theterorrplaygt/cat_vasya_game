# cat_vasya_game

## Модуль 1: `unit.py`

Абстрактный класс `Unit` — основа всех боевых единиц.

**Атрибуты**  
`strength`, `dexterity`, `constitution`, `wisdom`, `intelligence`, `charisma` – передаются в конструктор.

**Абстрактные методы**  
- `calculate_max_health() -> int`  
- `calculate_damage() -> int`  
- `calculate_defense() -> int`

**Магическая подсистема**  
- `spells: list` — хранит объекты заклинаний  
- `mana: int` — текущая мана  
- `add_spell(spell)` — добавляет заклинание  
- `cast_spell(index)` — применяет заклинание (тратит ману, возвращает урон)

## Модуль 2: `character.py`

Класс `Character` наследует `Unit`. При создании указывается `character_class`:

- `'warrior'` (воин)  
- `'mage'` (маг)  
- `'hunter'` (охотник)

Если класс неизвестен — `ValueError`.

**Формулы**  

| Класс     | Урон                                      | Защита                                      |
|-----------|-------------------------------------------|---------------------------------------------|
| Воин      | `strength * 2.2 + constitution // 3`      | `constitution * 1.8 + strength // 4`        |
| Маг       | `intelligence * 2.5 + wisdom // 2`        | `wisdom * 1.3 + intelligence // 6`          |
| Охотник   | `dexterity * 1.9 + strength // 3`         | `dexterity * 1.6 + constitution // 5`       |

**Здоровье** (единое для всех персонажей)  
`max_health = constitution * 10 + strength // 2`

**Максимальная мана**

| Класс     | Формула                                   |
|-----------|-------------------------------------------|
| Воин      | `intelligence + strength // 2`            |
| Маг       | `intelligence * 3 + wisdom`               |
| Охотник   | `int(dexterity * 1.5 + wisdom // 2)`      |

В конструкторе сразу вычисляются и сохраняются:
- `max_health` / `current_health`
- `damage`
- `defense`
- `mana` (устанавливается равной `max_mana`)

## Модуль 3: `monster.py`

Класс `Monster` наследует `Unit`. Не имеет классов, маны и заклинаний (мана всегда 0).

**Формулы**  
- Здоровье: `constitution * 8 + strength // 3`  
- Урон: `int(strength * 2 + constitution // 5)`  
- Защита: `int(constitution * 1.2 + strength // 5)`

В конструкторе аналогично сохраняются `max_health`, `current_health`, `damage`, `defense`.

## Модуль 4: `spell.py`

Абстрактный класс `Spell`:

- `name` — название  
- `damage` — базовый урон  
- `mana_cost` — стоимость маны  
- `cast()` — абстрактный метод, возвращает наносимый урон

**Реализованные заклинания**  
- `Fireball` — 35 урона, 15 маны  
- `IceLance` — 25 урона, 10 маны  
- `LightningBolt` — 40 урона, 20 маны

## Демонстрация: `main.py`

Создаются:
- воин (сила 18, телосложение 16, …),
- маг (интеллект 20),
- охотник (ловкость 18),
- дракон (монстр).

Персонажам добавляются заклинания, демонстрируется:

- применение заклинаний с расходом маны,
- проверка остатка маны,
- обработка ошибки при нехватке маны.

Выводятся все характеристики: HP, мана, урон, защита.

Запуск:

```bash
python main.py