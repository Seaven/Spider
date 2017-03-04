# coding=utf-8

"""
 logger util.
 Author: Seaven
"""

import logging
import sys


def get_logger(log_name):
    """
    get a logger by logger name
    :param log_name: logger's name
    :return: logger object
    """

    logger = logging.getLogger(log_name)

    formatter = logging.Formatter('%(asctime)s | %(process)d | %(thread)d | %(name)s | '
                                  '%(levelname)s | %(filename)s | %(lineno)d | %(message)s ')

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger
