from building import Building  # Импортируем класс построек
from moveable import Moveable  # Импортируем способность перемещаться


class MobileHouse(Building, Moveable):  # Мобильный дом является постройкой и умеет перемещаться
    def move(self, x, y):  # Реализуем обязательный метод перемещения
        self.setPosition(x, y)  # Меняем координаты дома на новые