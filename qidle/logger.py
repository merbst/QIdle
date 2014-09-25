"""
This module contains functions for easily setup the application logger
"""
import logging
import os
from qidle import system


def get_path():
    """
    Returns the log file path
    :return: str
    """
    return os.path.join(system.get_cache_directory(), 'QIdle.log')


def setup(verbose=False):
    """
    Configures the logger, adds a stream handler and a file handler.

    :param version: version of the application
    :param debug: True to enable debug log level, otherwise the info log
        level is used.
    """
    level = logging.DEBUG if verbose else logging.INFO
    logger = logging.getLogger()
    formatter = logging.Formatter(
        '%(asctime)s::%(levelname)s::%(name)s::%(message)s',
        '%Y-%m-%d %H:%M:%S')
    handlers = [
        logging.FileHandler(get_path(), mode='w')
    ]
    logger.setLevel(level)
    for handler in handlers:
        logger.addHandler(handler)
    for handler in logger.handlers:
        handler.setFormatter(formatter)
