from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array):
        pass

class BubbleSortStrategy(SortingStrategy):
    def sort(self, array):
        n = len(array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

class QuickSortStrategy(SortingStrategy):
    def sort(self, array):
        def quick_sort(items):
            if len(items) <= 1:
                return items
            pivot = items[len(items) // 2]
            less = [x for x in items if x < pivot]
            equal = [x for x in items if x == pivot]
            greater = [x for x in items if x > pivot]
            return quick_sort(less) + equal + quick_sort(greater)
        array[:] = quick_sort(array)

class Sorter:
    def __init__(self):
        self.strategy = None
    def set_strategy(self, strategy):
        self.strategy = strategy
    def sort_array(self, array):
        if self.strategy is None:
            raise ValueError("Strategy is not set")
        self.strategy.sort(array)