import logging
import logging.handlers
from filelock import FileLock

log_base = "/home/aerotract/microservice_logs/"

class AeroLogger:

    def __init__(self, name, log_file, maxBytes=20480, backup_count=5):
        self.name = name
        self.log_file = log_base + log_file
        self.maxBytes = maxBytes
        self.backup_count = backup_count
        self.lock_file = self.log_file + ".lock"

    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)
        log_format = f'[%(levelname)s] %(asctime)s {self.name} - %(message)s'
        date_format = '%Y-%m-%d %H:%M:%S'
        file_handler = logging.handlers.RotatingFileHandler(self.log_file, maxBytes=10240, backupCount=5)
        formatter = logging.Formatter(log_format, datefmt=date_format)
        file_handler.setFormatter(formatter)
        if not logger.handlers:
            logger.addHandler(file_handler)
        return logger
    
    def info(self, msg):
        with FileLock(self.lock_file):
            l = self.get_logger()
            l.info(msg)
            del l

    def error(self, msg):
        with FileLock(self.lock_file):
            l = self.get_logger()
            l.error(msg)
            del l