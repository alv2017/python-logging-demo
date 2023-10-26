# Time rotating log demo

import logging
import logging.handlers as handlers
import time
from random import randint

logger = logging.getLogger('ex03')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logHandler = handlers.TimedRotatingFileHandler('logs/ex03_app.log', when='M', interval=1, backupCount=2)
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)


def main():
    while True:
        time.sleep(1)
        logger.info("A Sample Log Statement")
        if randint(1, 10) == 9:
            logger.warning("Warning, the temperature reached 70°C.")


main()