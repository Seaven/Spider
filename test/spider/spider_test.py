# coding=utf-8

"""
Author: Seaven
"""

import unittest
import os
from spider import spider
from spider import url_manage
from spider import config_load


class SpiderTest(unittest.TestCase):
    def test_spider_craw(self):
        conf = config_load.SpiderConfig()
        conf.output_directory = '../output/'
        conf.crawl_timeout = 5
        conf.crawl_interval = 0
        conf.target_url = 'home\.baidu\.com$'

        sp = spider.Spider(conf, url_manage.UrlManage())
        sp.add_url_list(['http://www.baidu.com'])
        sp.craw()

        self.assertEqual(os.path.isfile('../outputhttp%3A%2F%2Fhome.baidu.com'), True, 'spider craw error')


if __name__ == '__main__':
    unittest.main()
