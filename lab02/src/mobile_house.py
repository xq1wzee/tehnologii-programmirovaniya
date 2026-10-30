from lab02.src.building import Building
from moveable import Moveable

class MobileHouse(Building, Moveable):
    def move(self, x, y):
        self.setPosition(x, y)
