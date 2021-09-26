# exception_decor.py

import functools
import logging

def create_logger():
    """
    Creates a logging object and returns it
    """
    logger = logging.getLogger("example_logger")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("e:/projects/ref_code/mjhtest.log")

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)
    return logger


def exception(function):
    """
    A decorator that wraps the passed in function and logs 
    exceptions should one occur
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logger = create_logger()
        try:
            logger.INFO()
            return function(*args, **kwargs)
        except:
            # log the exception
            err = "There was an exception in  "
            err += function.__name__
            logger.exception(err)

            # re-raise the exception
            raise
    return wrapper



@exception
def zero_divide():
    1 / 1



def LOG(fn):
    import inspect
    varList, _, _, default = inspect.getargspec(fn)
    d = {}
    if default is not None:
        d = dict((varList[-len(default):][i], v) for i, v in enumerate(default))

    def f(*argt, **argd):
        print ('Enter %s' % fn).center(100, '=')
        d.update(dict((varList[i], v) for i, v in enumerate(argt)))
        d.update(argd)
        for c in d.iteritems():
            print(f'{c} = {c}')

        ret = fn(*argt, **argd)
        
        print(f'return: {ret}')

        print('Exit %s' % fn).center(100, '=')
        return ret
    return f

@LOG
def f(a, b=2, *c, **d):
    pass
