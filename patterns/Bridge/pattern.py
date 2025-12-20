from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def display(self, content):
        pass

class Monitor(Device):
    def display(self, content):
        print(f"Монитор отображает: {content}")

class Printer(Device):
    def display(self, content):
        print(f"Принтер печатает: {content}")

class Output(ABC):
    def __init__(self, device):
        self._device = device
    
    @abstractmethod
    def render(self, data):
        pass

class TextOutput(Output):
    def render(self, data):
        self._device.display(f"Текст: {data}")

class ImageOutput(Output):
    def render(self, data):
        self._device.display(f"Изображение: {data}")

class ChartOutput(Output):
    def render(self, data):
        self._device.display(f"График: {data}")