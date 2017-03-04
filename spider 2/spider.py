# coding=utf-8

"""
Author: Seaven
"""

import collections
import time

import traceback
from common import file_util
from common import log_util
from common import webpage_util

spider_log = log_util.get_logger('Spider')


class Spider(object):
    """
    spider, craw url data
    """

    def __init__(self, spider_config, url_manage):
        """
        init
        :param spider_config: spider config
        :param url_manage: url manage class
        """
        self.url_queue = collections.deque()
        self.spider_config = spider_config
        self.url_manage = url_manage

    def add_url_list(self, url_list, depth=0):
        """
        add need craw url in spider target urls
        :param url_list: url which is need craw
        :param depth: url depth
        """
        if self.spider_config.max_depth < depth:
            return
       
        self.url_manage.url_list_put(url_list, depth)

    def is_finish(self):
        """
        decide spider craw data is finish
        :return: Boolean
        """
        return self.url_manage.url_empty()

    def craw(self):
        """
        spider craw data method
        :return:
        """

        def pop_url():
            return self.url_manage.url_pop()

        while not self.is_finish():
            next_depth_url_list = []

            # get next craw url
            url, depth = pop_url()

            # get url page content
            spider_log.info('spider to craw url[%s] data. ' % url)

            try:
                html = webpage_util.get_page_content(url, self.spider_config.crawl_timeout)

                spider_log.info('deal url[%s] page data.' % url)
                self.__craw_data_deal(url, html)

                spider_log.info('get next depth urls from url[%s] page.' % url)
                next_depth_url_list = webpage_util.get_page_urls(url, html)
            except Exception as e:
                spider_log.error('spider craw url[%s] error, cause : %s' % (url, traceback.format_exc(e)))

            self.add_url_list(next_depth_url_list, depth + 1)

            # craw sleep
            time.sleep(self.spider_config.crawl_interval)

    def __craw_data_deal(self, url, html):
        """
        url page deal method
        :param url: page url
        :param html: page html
        """
        if webpage_util.is_match_url(self.spider_config.target_url, url):
            file_name = webpage_util.url_escape(url)
            file_util.file_save(file_name, self.spider_config.output_directory, html)
            spider_log.info('spider match target url page, save file : %s to output directory.' % file_name)

