# strategy.py
from abc import ABC, abstractmethod

# Интерфейс стратегии
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Сортировка пузырьком:")
        arr = data.copy()
        n = len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Быстрая сортировка:")
        return self._quick_sort(data.copy())
    
    def _quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self._quick_sort(left) + middle + self._quick_sort(right)

class Sorter:
    def __init__(self, strategy=None):
        self._strategy = strategy
    
    def set_strategy(self, strategy):
        self._strategy = strategy
    
    def sort_data(self, data):
        if self._strategy:
            result = self._strategy.sort(data)
            print(f"Результат: {result}")
        else:
            raise ValueError("Стратегия не установлена")