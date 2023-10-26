# Rotating log demo

import logging
import logging.handlers as handlers
import time

logger = logging.getLogger('ex02')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logHandler = handlers.RotatingFileHandler('logs/ex02_app.log', maxBytes=500, backupCount=2)
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)


def main():
    while True:
        time.sleep(1)
        logger.info("A Sample Log Statement")


main()
