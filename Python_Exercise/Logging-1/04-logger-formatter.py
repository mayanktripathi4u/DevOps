import logging

logger = logging.getLogger() # This is an instance of Logger Class.

logging.basicConfig(format="()", level=logging.DEBUG)

# logger.warning("This is a warning message") # Default
# logger.info("This is a info message")
# logger.error("This is a error message")
logger.debug("This is a debug message")