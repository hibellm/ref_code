
import logging

logger = logging.getLogger('scope.name')

# LOG TO FILE
file_log_handler = logging.FileHandler('logfile.log')
logger.addHandler(file_log_handler)

# LOG TO STDERR
stderr_log_handler = logging.StreamHandler()
logger.addHandler(stderr_log_handler)

# FORMAT OUTPUT TO LOG
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_log_handler.setFormatter(formatter1)

formatter2 = logging.Formatter('%(message)s')
stderr_log_handler.setFormatter(formatter2)


logger.info('Info message')
logger.error('Error message')

