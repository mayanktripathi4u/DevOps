import logging

logger = logging.getLogger() # This is an instance of Logger Class.

logging.basicConfig(filename="myLogs.log", format="%(asctime)s -- %(filename)s -- %(lineno)d -- %(message)s", level=logging.DEBUG)

logging.basicConfig(format="%(asctime)s -- %(filename)s -- %(lineno)d -- %(message)s", datefmt="%Y-%m-%d", level=logging.DEBUG)

logger.warning("This is a warning message") # Default
logger.info("This is a info message")   
logger.error("This is a error message")
logger.debug("This is a debug message")