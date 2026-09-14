RPG Character System

A simple object-oriented RPG combat system built with Python.

This project demonstrates core Object-Oriented Programming (OOP) concepts such as inheritance, method overriding, encapsulation, polymorphism, and interaction between different character classes.

Features
Base Character class
Warrior and Mage subclasses
Enemy base class
Goblin and Dragon enemies
Health and maximum health
Attack system
Damage calculation
Warrior armor system
Warrior power attack with a 50% chance to deal double damage
Mage fireball ability with mana consumption
Healing system
Experience points
Leveling system
Character death checks
Random enemy selection
Turn-based combat
Multiple battles
Type annotations
Flake8 code quality checks
Project Structure
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
Character Classes
Character

Character is the base class for all characters.

It provides:

Health and maximum health
Attack power
Experience points
Level
Basic attacks
Damage handling
Healing
Leveling up
Alive/dead state
Warrior

Warrior inherits from Character and adds:

Armor
power_attack()

The power attack has a 50% chance to deal double damage.

When the Warrior levels up, armor increases by 2.

Mage

Mage inherits from Character and adds:

Mana
fireball()

Fireball deals double the Mage's attack power and costs 20 mana.

When the Mage levels up, mana increases by 20.

Enemies
Goblin

A basic enemy with:

40 HP
10 attack power
50 experience points
Dragon

A stronger enemy with:

60 HP
15 attack power
90 experience points

At the beginning of each battle, a random enemy is selected.

Combat System

The game uses a turn-based combat system.

During the player's turn, they can choose:

1 - Attack
2 - Heal
3 - Special attack

After a successful player action, the enemy attacks if it is still alive.

The battle continues until either the player or the enemy dies.

After winning a battle, the player can start another random battle.

Leveling System

Characters gain experience points by defeating enemies.

Every 100 experience points increases the character's level.

When a character levels up:

Health increases by 20
Maximum health increases by 20
Attack power increases by 5

Extra experience points are preserved after leveling up.

For example:

160 XP
   ↓
Level up
   ↓
60 XP remaining

Multiple levels can be gained if enough experience points are earned.

Requirements
Python 3.10+
Flake8
Installation

Clone the repository:

git clone https://github.com/Pashuna/rpg-character-system.git

Open the project directory:

cd rpg-character-system

Create and activate a virtual environment.

Windows
python -m venv .venv
.venv\Scripts\activate
macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

Install Flake8:

pip install flake8
Running the Project

Run the game with:

python main.py
Code Quality

The project was checked with Flake8.

Run:

flake8 --exclude=.venv .

The project should pass the Flake8 code quality check without errors.

Technologies
Python
Object-Oriented Programming (OOP)
Inheritance
Polymorphism
Encapsulation
Type Annotations
Git
GitHub
Flake8
Project Status

The basic RPG combat system is implemented and working.

Possible future improvements:

Additional character classes
Additional enemies
More special abilities
Inventory system
Items and equipment
More advanced combat mechanics
Critical hits and status effects
Save/load system