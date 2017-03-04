# coding=utf-8

"""
Author: Seaven
"""

import unittest
from test.spider import config_load


class TestConfigLoad(unittest.TestCase):
    def test_read_config(self):
        config = config_load.read_config('..\spider.conf')

        self.assertIsNotNone(config, 'read config file error')
        self.assertEqual(config.max_depth, 1, 'int type data read error')
        self.assertEqual(config.output_directory, '../baidu/file', 'string type date read error')


if __name__ == '__main__':
    unittest.main()
