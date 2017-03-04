# coding=utf-8

"""
Author: Seaven
"""

import unittest
from common import thread_task


class ThreadTaskTest(unittest.TestCase):
    def test_thread_task_run(self):
        target = []

        def func():
            target.append(1)

        func_list = []
        for i in xrange(5):
            func_list.append(func)

        task = thread_task.ThreadTask(func_list, lambda: target.append(10))
        task.task_start()

        self.assertEqual(len(task.thread_list), 5, 'task build thread count is error')
        self.assertEqual(len(target), 6, 'task run result is error')
        self.assertEqual(target[-1], 10, 'task end function is error')


if __name__ == '__main__':
    unittest.main()
