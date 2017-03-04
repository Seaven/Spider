# coding=utf-8

"""
Author: Seaven
"""

import unittest
import os
from common import file_util


class FileUtilTest(unittest.TestCase):
    def test_file_save(self):
        file_name = 'file_save_test.txt'
        path = '../output/'
        content = 'file_save_test'

        file_util.file_save(file_name, path, content)

        self.assertEqual(os.path.exists(path + file_name), True, 'file save error')

    def test_file_read(self):
        file_path = '../output/file_read_test.txt'

        lines = file_util.read_file(file_path)

        self.assertEqual(len(lines), 2, 'read file error')
        self.assertEqual(lines[1], 'test file line2', 'read content error')


if __name__ == '__main__':
    unittest.main()
