# File log demo

import logging

logger = logging.getLogger('ex01')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('logs/ex01_app.log')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)


def main():
    logger.info("A Sample Log Statement")


main()