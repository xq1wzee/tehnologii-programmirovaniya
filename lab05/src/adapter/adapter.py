from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ExternalLogger:
    def log_message(self, msg):
        print("External log:", msg)

class LoggerAdapter(Logger):
    def __init__(self, external_logger):
        self.external_logger = external_logger
    def log(self, message):
        self.external_logger.log_message(message)