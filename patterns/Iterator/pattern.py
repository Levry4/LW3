from collections.abc import Iterator
from typing import Any, List

class CustomIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._position = 0
    
    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
            return value
        except IndexError:
            raise StopIteration()
    
    def has_next(self):
        return self._position < len(self._collection)

class Collection:
    def __init__(self):
        self._items = []
    
    def add_item(self, item):
        self._items.append(item)
    
    def __iter__(self):
        return CustomIterator(self._items)
    
    def reverse_iterator(self):
        return CustomIterator(list(reversed(self._items)))