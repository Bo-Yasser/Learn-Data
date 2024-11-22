import logging

# print(dir(logging))

# logging.basicConfig(filename="my_app.log", filemode="a", 
#                     format="(%(asctime)s) => | %(name)s | %(levelname)s => '%(message)s'")
# logging.critical("This Is Critical Message")


logging.basicConfig(filename="my_app.log", 
                    filemode="a", 
                    format="(%(asctime)s) | %(name)s | %(levelname)s => '%(message)s'", 
                    datefmt="%d %B %Y, %H:%M:%S")

# logging.warning("This Is Warning Message")


my_logger = logging.getLogger("Elzero")
my_logger.warning("This Is Warning Message")