import inspect
import logging


class LogGen:
    """Class for logging"""

    @staticmethod
    def log_gen():
        """Log generation will happen in this method"""
        # Set class/method name from where it is called
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        # create console handler or file handler and set the log level
        file_handler = logging.FileHandler(".//logs//automation.log", "w")
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s -%(name)s: %(message)s', datefmt='%m/%d%Y %I:%ML%S %p')
        # add formatter to console or file handler
        file_handler.setFormatter(formatter)
        # add console handler to logger
        logger.addHandler(file_handler)
        return logger