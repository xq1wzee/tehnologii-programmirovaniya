from unit import Unit
from attacker import Attacker
from moveable import Moveable

class Archer(Unit, Attacker, Moveable):
    def __init__(self, name, x, y, hp, damage):
        super().__init__(name, x, y, hp)
        self.__damage = damage

    def attack(self, unit):
        if self.isAlive():
            unit.receiveDamage(self.__damage)

    def move(self, x, y):
        if self.isAlive():
            self.setPosition(x, y)
