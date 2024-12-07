import logging

class GenericLogger:
    def __init__(self):
        """
        __init__ constructor for GenericLogger class
        
        Does nothing currently. Just a placeholder
        """
        pass

    def get_logger(self):
        """
        Gets a logger for the application with the level set to DEBUG
        
        The logger is configured to log to the console with the following format:
        %(asctime)s - %(name)s - %(levelname)s - %(message)s
        
        :return: A logger object
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)  

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)

        logger.propagate = False
        return logger
