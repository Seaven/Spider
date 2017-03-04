# coding=utf-8

"""
Author: Seaven
"""

import unittest

from common import log_util


class LogUtilCase(unittest.TestCase):
    def test_get_logger(self):
        test_logger = log_util.get_logger('log_test')

        self.assertIsNotNone(test_logger, 'log util get logger error')


if __name__ == '__main__':
    unittest.main()
