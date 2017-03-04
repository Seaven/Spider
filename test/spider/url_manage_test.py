# coding=utf-8

"""
Author: Seaven
"""

import unittest
import threading

from spider import url_manage


class UrlManageCase(unittest.TestCase):
    def test(self):
        manage = url_manage.UrlManage()

        threading.Thread(target=lambda: manage.url_put('www.baidu.com')).start()
        self.assertEqual(manage.url_is_contains('www.baidu.com'), True, 'url manage is not contains url')
        threading.Thread(target=lambda: manage.url_put('www.weibo.com')).start()
        self.assertEqual(manage.url_is_contains('www.baidu.com'), True, 'url manage is not contains url')
        self.assertEqual(manage.url_is_contains('www.weibo.com'), True, 'url manage is not contains url')


if __name__ == '__main__':
    unittest.main()
