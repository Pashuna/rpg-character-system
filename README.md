# RPG Character System

A simple object-oriented RPG combat system built with Python.

The project demonstrates core OOP concepts such as inheritance, method overriding, encapsulation, and interaction between different character classes.

## Features

* Base `Character` class
* `Warrior` and `Mage` subclasses
* Health and maximum health
* Attack system
* Damage calculation
* Armor system
* Warrior power attack with random damage
* Mage fireball ability with mana consumption
* Healing
* Experience points
* Leveling system
* Character death checks
* Turn-based combat loop
* Type annotations
* Flake8 code quality checks

## Project Structure

```text
rpg-character-system/
├── character.py
├── warrior.py
├── mage.py
├── main.py
├── README.md
└── .gitignore
```

## Character Classes

### Character

The base class for all characters.

It provides:

* Health and maximum health
* Attack power
* Experience
* Level
* Basic attacks
* Damage handling
* Healing
* Leveling up
* Alive/dead state

### Warrior

The Warrior inherits from `Character` and adds:

* Armor
* `power_attack()`

The power attack has a 50% chance to deal double damage.

### Mage

The Mage inherits from `Character` and adds:

* Mana
* `fireball()`

Fireball deals double the Mage's attack power and costs 20 mana.

## Combat Example

A simple combat loop can be run from `main.py`.

```text
Warrior attacked Mage for 60 damage!
Mage attacked Warrior for 45 damage!
Warrior attacked Mage for 40 damage!
```

The battle continues until one of the characters dies.

## Leveling System

Characters gain experience by defeating enemies.

Every 100 experience points increases the character's level.

When a character levels up:

* Health increases by 20
* Maximum health increases by 20
* Attack power increases by 5

Extra experience is preserved after leveling up.

For example:

```text
160 XP
↓
Level up
↓
60 XP remaining
```

## Requirements

* Python 3.10+
* Flake8

## Running the Project

Clone the repository and run:

```bash
python main.py
```

To check the code with Flake8:

```bash
flake8 character.py warrior.py mage.py main.py
```

## Technologies

* Python
* Object-Oriented Programming
* Git
* GitHub
* Flake8

## Project Status

The basic RPG combat system is implemented and working.

Future improvements may include additional character classes, enemies, abilities, inventory, and a more advanced combat system.
