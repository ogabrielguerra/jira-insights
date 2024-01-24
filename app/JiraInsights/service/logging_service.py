import logging

class LoggingService:

    logger = logging.getLogger(__name__)
    stack_level = 4

    def __init__(self, level: str, message: str):
        self.switch(level, message)           

    def switch(self, level, message):
        default = self.info_event(message)
        return getattr(self, str(level) + '_event', lambda message: default)(message)
    
    def debug_event(self, message):
        self.logger.debug(message, stacklevel=self.stack_level)
    
    def info_event(self, message):
        self.logger.info(message, stacklevel=self.stack_level)
    
    def warning_event(self, message):
        self.logger.warning(message, stacklevel=self.stack_level)

    def error_event(self, message):
        self.logger.error(message, stacklevel=self.stack_level)

    def critical_event(self, message):
        self.logger.critical(message, stacklevel=self.stack_level)
