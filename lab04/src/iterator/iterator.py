from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    @abstractmethod
    def next(self):
        pass

class ArrayIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.position = 0
    def has_next(self):
        return self.position < len(self.items)
    def next(self):
        if self.has_next():
            item = self.items[self.position]
            self.position += 1
            return item
        raise IndexError("No more elements")