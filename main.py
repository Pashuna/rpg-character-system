from warrior import Warrior
from mage import Mage


warrior = Warrior('Warrior', 120, 30, 5)
mage = Mage('Mage', 100, 25, 60)
while warrior.is_alive() and mage.is_alive():
    warrior.power_attack(mage)
    if mage.is_alive():
        mage.fireball(warrior)
