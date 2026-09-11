# RPG Character System

A small RPG character system written in Python.
The project demonstrates object-oriented programming, inheritance, polymorphism, and basic character progression.

## Features

* Character creation
* Health and attack power
* Taking damage
* Healing
* Health limit (`max_health`)
* Experience and leveling
* Warrior class with armor
* Mage class with mana and fireball attack
* Polymorphism through `take_damage()`
* Type annotations
* Code style checked with Flake8

## Classes

### `Character`

Base class for all characters.

Main attributes:

* `name`
* `health`
* `max_health`
* `attack_power`
* `level`
* `experience`

Main methods:

* `attack()`
* `take_damage()`
* `heal()`
* `is_alive()`
* `level_up()`

### `Warrior`

Inherits from `Character`.

Adds:

* `armor`

Armor reduces incoming damage.

### `Mage`

Inherits from `Character`.

Adds:

* `mana`
* `fireball()`

Fireball deals double the mage's attack power and costs 20 mana.

## Level System

Characters gain **50 XP** when they defeat an enemy.

Every **100 XP**:

* Level increases by 1
* Health increases by 20
* Attack power increases by 5

Extra XP is preserved, so a character can gain multiple levels if enough experience is available.

## Example

```python
from character import Character, Warrior, Mage

hero = Character("Hero", 100, 20)
warrior = Warrior("Warrior", 120, 15, 5)
mage = Mage("Mage", 80, 25, 40)

hero.attack(warrior)
mage.fireball(warrior)

print(hero)
print(warrior)
print(mage)
```

## Project Structure

```text
rpg-character-system/
├── character.py
├── main.py
├── README.md
├── .gitignore
└── .venv/
```

`.venv/`, `.idea/`, and `__pycache__/` are excluded from Git.

## Technologies

* Python
* Object-Oriented Programming
* Git
* GitHub
* Flake8

## Project Status

The basic character system is implemented.

Possible future improvements:

* Automatic tests with `pytest`
* More character classes
* Weapons and items
* Critical hits
* Skills and abilities
* More advanced combat system
* Separate test directory
