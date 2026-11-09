from building import Building  # Импортируем класс построек
from attacker import Attacker  # Импортируем абстрактный класс способности атаковать


class Fort(Building, Attacker):  # Крепость наследуется от постройки и способности атаковать
    def __init__(self, name, x, y, built, damage):  # Конструктор принимает данные крепости и её урон
        super().__init__(name, x, y, built)  # Передаём общие параметры конструктору Building
        self.__damage = damage  # Сохраняем силу атаки крепости

    def attack(self, unit):  # Реализуем метод атаки
        if self.isBuilt():  # Проверяем, построена ли крепость
            unit.receiveDamage(self.__damage)  # Если построена, наносим цели урон