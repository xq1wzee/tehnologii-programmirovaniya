from game_object import GameObject  # Импортируем базовый класс игровых объектов


class Building(GameObject):  # Создаём класс построек, наследующийся от GameObject
    def __init__(self, name, x, y, built):  # Конструктор принимает имя, координаты и состояние постройки
        super().__init__(name, x, y)  # Вызываем конструктор родительского класса
        self.__built = built  # Сохраняем информацию о том, построено ли здание

    def isBuilt(self):  # Метод проверяет состояние строительства
        return self.__built  # Возвращаем True или False