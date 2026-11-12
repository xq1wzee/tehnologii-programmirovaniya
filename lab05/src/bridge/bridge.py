from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def print(self, data):
        pass

class Monitor(Device):
    def print(self, data):
        print("Displaying on monitor:", data)

class Printer(Device):
    def print(self, data):
        print("Printing to paper:", data)

class Output(ABC):
    def __init__(self, device):
        self.device = device
    @abstractmethod
    def render(self, data):
        pass

class TextOutput(Output):
    def render(self, data):
        self.device.print("Text: " + data)

class ImageOutput(Output):
    def render(self, data):
        self.device.print("Image: [Binary data: " + data + "]")