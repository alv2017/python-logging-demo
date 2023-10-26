# Using multiple log levels

import logging
import logging.handlers as handlers
import time

logger = logging.getLogger('ex04')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logHandler = handlers.TimedRotatingFileHandler('logs/ex04_app.log', when='M', interval=1, backupCount=2)
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)

errorLogHandler = handlers.RotatingFileHandler('logs/ex04_error.log', maxBytes=5000, backupCount=2)
errorLogHandler.setLevel(logging.ERROR)
errorLogHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.addHandler(errorLogHandler)


def main():
    while True:
        time.sleep(1)
        logger.info("A Sample Log Statement")
        logger.error("An error log statement")


main()
