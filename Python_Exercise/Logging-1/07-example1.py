import logging

logger = logging.getLogger() # This is an instance of Logger Class.

logging.basicConfig(filename="myLogs.log", format="%(asctime)s -- %(filename)s -- %(levelname)s -- %(lineno)d -- %(message)s", level=logging.DEBUG)


def return_sum_of_two_nums(a,b):
    logger.info(f"Inside function to add [a = {a} & b = {b}]")

    try:
        logger.warning("There are no checks if the inputs are integer")
        return a + b
    except Exception as e:
        logger.error("%s", e)

print(return_sum_of_two_nums(10, 20))

print(return_sum_of_two_nums(10, 'n'))

print(return_sum_of_two_nums(40, 60))