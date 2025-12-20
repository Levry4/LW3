from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message, level="INFO"):
        pass

class ExternalLogger:
    def log_message(self, msg, msg_type):
        print(f"[{msg_type}] {msg}")

class LoggerAdapter(Logger):
    def __init__(self, external_logger):
        self._external_logger = external_logger
        self._level_mapping = {
            "INFO": "INFO",
            "WARNING": "WARN",
            "ERROR": "ERROR",
            "DEBUG": "DEBUG"
        }
    
    def log(self, message, level="INFO"):
        external_level = self._level_mapping.get(level, "INFO")
        self._external_logger.log_message(message, external_level)

class NewSystemLogger(Logger):
    def log(self, message, level="INFO"):
        print(f"Новая система: [{level}] {message}")