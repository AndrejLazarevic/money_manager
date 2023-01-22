import logging

LOG = logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')


def log(message):
    LOG.info('\n' + message)
