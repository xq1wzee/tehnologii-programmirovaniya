from abc import ABC, abstractmethod
class Chair(ABC):
    @abstractmethod
    def sit(self) -> str:
        pass
class Sofa(ABC):
    @abstractmethod
    def lie_on(self) -> str:
        pass
class ModernChair(Chair):
    def sit(self) -> str:
        return "Сидим на современном стуле"
class ModernSofa(Sofa):
    def lie_on(self) -> str:
        return "Отдыхаем на современном диване"
class ClassicChair(Chair):
    def sit(self) -> str:
        return "Сидим на классическом стуле"
class ClassicSofa(Sofa):
    def lie_on(self) -> str:
        return "Отдыхаем на классическом диване"