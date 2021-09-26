# # exception_decor.py

# import functools
# import logging


# mylogs = logging.getLogger(__name__)
# mylogs.setLevel(logging.DEBUG)

# file = logging.FileHandler("e:/projects/ref_code/logging_example.log")
# file.setLevel(logging.INFO)
# fileformat = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s",datefmt="%H:%M:%S")
# file.setFormatter(fileformat)
# mylogs.addHandler(file)

# # The demo test code
# mylogs.debug("The debug")
# mylogs.info("The info")
# mylogs.warning("The warn")
# mylogs.error("The error")
# mylogs.critical("The critical")





# # WRITE TO LOG AND CONSOLE

# import logging

# stream = logging.StreamHandler()
# stream.setLevel(logging.INFO)
# streamformat = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
# stream.setFormatter(streamformat)

# mylogs.addHandler(stream)


# # The demo test code
# mylogs.debug("The debug")
# mylogs.info("The info")
# mylogs.warning("The warn")
# mylogs.error("The error")
# mylogs.critical("The critical")


"""
Now we are going to create 3 handlers namely file , cric_file , stream .
file will be storing all the logs of level warning and above in the file sample.log
cric_file will be storing all the logs of critical level in the file Critical.log
stream will be showing all the logs in the console.
So, as I said about handlers they can be configured differently as you want; like having different levels and all other configs. Dont worry everything is explained below.
"""

import logging
import os


log_root = os.path.join(os.getcwd(), 'ref_code')

# Creating logger
mylogs = logging.getLogger(__name__)
mylogs.setLevel(logging.DEBUG)

# Handler - 1
file = logging.FileHandler(os.path.join(log_root, "logging_example.log"))
fileformat = logging.Formatter("%(asctime)s - [%(levelname)s] - [%(filename)s > %(funcName)s() > %(lineno)d %(lineno)s] %(message)s",
datefmt="%Y-%m-%d %H:%M:%S")
file.setLevel(logging.WARNING)
file.setFormatter(fileformat)

# Handler - 2
cric_file = logging.FileHandler(os.path.join(log_root, "logging_example_critical.log"))
cric_file.setLevel(logging.CRITICAL)
cric_file.setFormatter(fileformat)
# format we can use it anywhere.

# Handler - 3
stream = logging.StreamHandler()
streamformat = logging.Formatter("%(levelname)s:%(module)s:%(message)s")
stream.setLevel(logging.DEBUG)
stream.setFormatter(streamformat)

# Adding all handlers to the logs
mylogs.addHandler(file)
mylogs.addHandler(stream)
mylogs.addHandler(cric_file)
















# def create_logger():
#     """
#     Creates a logging object and returns it
#     """
#     logger = logging.getLogger("example_logger")
#     logger.setLevel(logging.INFO)

#     # create the logging file handler
#     fh = logging.FileHandler("e:/projects/ref_code/mjhtest.log")

#     fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#     formatter = logging.Formatter(fmt)
#     fh.setFormatter(formatter)

#     # add handler to logger object
#     logger.addHandler(fh)
#     return logger


# def exception(function):
#     """
#     A decorator that wraps the passed in function and logs 
#     exceptions should one occur
#     """
#     @functools.wraps(function)
#     def wrapper(*args, **kwargs):
#         logger = create_logger()
#         try:
#             logger.INFO()
#             return function(*args, **kwargs)
#         except:
#             # log the exception
#             err = "There was an exception in  "
#             err += function.__name__
#             logger.exception(err)

#             # re-raise the exception
#             raise
#     return wrapper



# @exception
# def zero_divide():
#     1 / 1



# def LOG(fn):
#     import inspect
#     varList, _, _, default = inspect.getargspec(fn)
#     d = {}
#     if default is not None:
#         d = dict((varList[-len(default):][i], v) for i, v in enumerate(default))

#     def f(*argt, **argd):
#         print ('Enter %s' % fn).center(100, '=')
#         d.update(dict((varList[i], v) for i, v in enumerate(argt)))
#         d.update(argd)
#         for c in d.iteritems():
#             print(f'{c} = {c}')

#         ret = fn(*argt, **argd)
        
#         print(f'return: {ret}')

#         print('Exit %s' % fn).center(100, '=')
#         return ret
#     return f

# @LOG
# def f(a, b=2, *c, **d):
#     pass
