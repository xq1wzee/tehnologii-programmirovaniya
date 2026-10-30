from lab02.src.game_object import GameObject

class Unit(GameObject):
    def __init__(self, name, x, y, hp):
        super().__init__(name, x, y)
        self.__hp = hp

    def isAlive(self):
        return self.__hp > 0

    def getHp(self):
        return self.__hp

    def receiveDamage(self, damage):
        self.__hp -= damage

        if self.__hp < 0:
            self.__hp = 0
