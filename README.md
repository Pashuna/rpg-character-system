# RPG Character System

A simple object-oriented RPG combat system built with Python.

The project demonstrates core OOP concepts such as inheritance, method overriding, encapsulation, polymorphism, and interaction between different character classes.

## Features

* Base `Character` class
* `Warrior` and `Mage` subclasses
* `Enemy` base class
* `Goblin` and `Dragon` enemies
* Health and maximum health
* Attack system
* Damage calculation
* Warrior armor system
* Warrior power attack with a 50% chance to deal double damage
* Mage fireball ability with mana consumption
* Healing system
* Experience points
* Leveling system
* Character death checks
* Random enemy selection
* Turn-based combat
* Multiple battles
* Type annotations
* Flake8 code quality checks

## Project Structure

```text
rpg-character-system/
├── character.py
├── warrior.py
├── mage.py
├── enemy.py
├── goblin.py
├── dragon.py
├── game.py
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

The `Warrior` inherits from `Character` and adds:

* Armor
* `power_attack()`

The power attack has a 50% chance to deal double damage.

When the Warrior levels up, armor also increases by 2.

### Mage

The `Mage` inherits from `Character` and adds:

* Mana
* `fireball()`

Fireball deals double the Mage's attack power and costs 20 mana.

When the Mage levels up, mana increases by 20.

## Enemies

### Goblin

A basic enemy with:

* 40 HP
* 10 attack power
* 50 experience reward

### Dragon

A stronger enemy with:

* 60 HP
* 15 attack power
* 90 experience reward

At the beginning of each battle, a random enemy is selected.

## Combat System

The game uses a turn-based combat system.

During the player's turn, they can:

```text
1 - Attack
2 - Heal
3 - Special attack
```

After a successful player action, the enemy attacks if it is still alive.

The battle continues until either the player or the enemy dies.

The player can start another random battle after winning.

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

Multiple levels can be gained if enough experience is earned.

## Requirements

* Python 3.10+
* Flake8

## Running the Project

Run the game with:

```bash
python main.py
```

## Code Quality

To check the entire project with Flake8:

```bash
flake8 --exclude=.venv .
```

## Technologies

* Python
* Object-Oriented Programming
* Git
* GitHub
* Flake8

## Project Status

The basic RPG combat system is implemented and working.

Possible future improvements:

* Additional character classes
* Additional enemies
* More special abilities
* Inventory system
* Items and equipment
* More advanced combat mechanics
* Critical hits and status effects
* Save/load system
