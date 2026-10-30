from lab02.src.archer import Archer
from lab02.src.fort import Fort
from mobile_house import MobileHouse

archer = Archer("Лучник", 2, 3, 100, 20)
enemy = Archer("Противник", 5, 5, 100, 10)
fort = Fort("Крепость", 1, 1, True, 30)
house = MobileHouse("Дом на колесах", 4, 4, True)

print("Игровые объекты:")
print(archer.getName(), "ID:", archer.getId())
print("Координаты:", archer.getX(), archer.getY())
print("Здоровье:", archer.getHp())

print("\nАтака лучника:")
archer.attack(enemy)
print("Здоровье противника:", enemy.getHp())

print("\nАтака крепости:")
fort.attack(enemy)
print("Здоровье противника:", enemy.getHp())

print("\nПроверка состояния юнита:")
print("Жив ли противник:", enemy.isAlive())

print("\nПеремещение:")
archer.move(6, 7)
house.move(8, 9)

print("Новые координаты лучника:",
      archer.getX(), archer.getY())

print("Новые координаты дома:",
      house.getX(), house.getY())

print("\nПроверка постройки:")
print("Крепость построена:", fort.isBuilt())
print("Дом построен:", house.isBuilt())
