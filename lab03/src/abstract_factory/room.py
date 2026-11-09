from .factories import FurnitureFactory
class Room:
    def __init__(self, factory: FurnitureFactory):
        self.chair = factory.create_chair()
        self.sofa = factory.create_sofa()
    def describe(self):
        return (
            self.chair.sit(),
            self.sofa.lie_on()
        )