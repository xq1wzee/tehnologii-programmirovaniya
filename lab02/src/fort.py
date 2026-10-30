from lab02.src.building import Building
from lab02.src.attacker import Attacker

class Fort(Building, Attacker):
    def __init__(self, name, x, y, built, damage):
        super().__init__(name, x, y, built)
        self.__damage = damage

    def attack(self, unit):
        if self.isBuilt():
            unit.receiveDamage(self.__damage)
