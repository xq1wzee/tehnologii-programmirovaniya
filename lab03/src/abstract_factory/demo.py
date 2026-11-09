from .factories import (
    ModernFurnitureFactory,
    ClassicFurnitureFactory
)
from .room import Room
def run():
    modern_room = Room(ModernFurnitureFactory())
    classic_room = Room(ClassicFurnitureFactory())
    print("Современная мебель:")
    for item in modern_room.describe():
        print("-", item)
    print("Классическая мебель:")
    for item in classic_room.describe():
        print("-", item)
if __name__ == "__main__":
            run()