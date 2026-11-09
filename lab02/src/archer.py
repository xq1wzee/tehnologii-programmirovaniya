from unit import Unit  # Импортируем класс юнита
from attacker import Attacker  # Импортируем способность атаковать
from moveable import Moveable  # Импортируем способность перемещаться


class Archer(Unit, Attacker, Moveable):  # Лучник наследуется от юнита и двух классов способностей
    def __init__(self, name, x, y, hp, damage):  # Конструктор принимает данные лучника
        super().__init__(name, x, y, hp)  # Передаём общие данные и здоровье родительскому классу Unit
        self.__damage = damage  # Сохраняем силу атаки лучника

    def attack(self, unit):  # Реализуем метод атаки, обязательный для Attacker
        if self.isAlive():  # Проверяем, жив ли сам лучник
            unit.receiveDamage(self.__damage)  # Наносим цели урон, равный силе атаки лучника

    def move(self, x, y):  # Реализуем метод перемещения, обязательный для Moveable
        if self.isAlive():  # Проверяем, жив ли лучник
            self.setPosition(x, y)  # Изменяем координаты лучника