from abc import ABC, abstractmethod
from .products import (
    Chair,
    Sofa,
    ModernChair,
    ModernSofa,
    ClassicChair,
    ClassicSofa
)
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass
    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    def create_sofa(self) -> Sofa:
        return ModernSofa()
class ClassicFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ClassicChair()
    def create_sofa(self) -> Sofa:
        return ClassicSofa()