from abc import ABC, abstractmethod
from enum import Enum

class RequestType(Enum):
    TYPE_A = "A"
    TYPE_B = "B"
    TYPE_C = "C"

class Request:
    def __init__(self, request_type, content):
        self.type = request_type
        self.content = content

class Handler(ABC):
    def __init__(self):
        self._next_handler = None
    
    def set_next(self, handler):
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request):
        pass
    
    def _pass_to_next(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request.type == RequestType.TYPE_A:
            print(f"Обработчик A обработал запрос: {request.content}")
            return True
        return self._pass_to_next(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request.type == RequestType.TYPE_B:
            print(f"Обработчик B обработал запрос: {request.content}")
            return True
        return self._pass_to_next(request)

class ConcreteHandlerC(Handler):
    def handle(self, request):
        if request.type == RequestType.TYPE_C:
            print(f"Обработчик C обработал запрос: {request.content}")
            return True
        print(f"Ни один обработчик не смог обработать запрос: {request.content}")
        return False