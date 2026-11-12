from abc import ABC, abstractmethod
from enum import Enum

class RequestType(Enum):
    TYPE_A = "A"
    TYPE_B = "B"

class Request:
    def __init__(self, request_type):
        self.request_type = request_type
    def get_type(self):
        return self.request_type

class Handler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass
    @abstractmethod
    def set_next_handler(self, next_handler):
        pass

class ConcreteHandlerA(Handler):
    def __init__(self):
        self.next_handler = None
    def handle_request(self, request):
        if request.get_type() == RequestType.TYPE_A:
            print("ConcreteHandlerA handled the request.")
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)
    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

class ConcreteHandlerB(Handler):
    def __init__(self):
        self.next_handler = None
    def handle_request(self, request):
        if request.get_type() == RequestType.TYPE_B:
            print("ConcreteHandlerB handled the request.")
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)
    def set_next_handler(self, next_handler):
        self.next_handler = next_handler