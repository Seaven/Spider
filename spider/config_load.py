# coding=utf-8

"""
Author: Seaven
"""

import ConfigParser
import os
from common import log_util

config_log = log_util.get_logger('read_config')


def read_config(conf_path):
    """
    get spider config from config file
    will raise Exception when read config file error or config error
    :param conf_path: config file path
    :return: spider config object
    """
    if conf_path is None:
        raise Exception("conf_path can't be empty!")

    conf_parser = ConfigParser.ConfigParser()
    conf_parser.read(conf_path)

    spider_config = SpiderConfig()

    try:
        spider_config.url_list_file = conf_parser.get('spider', 'url_list_file')
        spider_config.output_directory = conf_parser.get('spider', 'output_directory')
        spider_config.target_url = conf_parser.get('spider', 'target_url')

        spider_config.max_depth = conf_parser.getint('spider', 'max_depth')
        spider_config.crawl_interval = conf_parser.getint('spider', 'crawl_interval')
        spider_config.crawl_timeout = conf_parser.getint('spider', 'crawl_timeout')
        spider_config.thread_count = conf_parser.getint('spider', 'thread_count')

        # check config is right
        spider_config.check_config()
    except Exception as e:
        config_log.error('read config from %s error! cause: %s' % (conf_path, e.message))
        raise e

    return spider_config


class SpiderConfig(object):
    """
    spider config
    """
    def __init__(self):
        self.url_list_file = ''
        self.output_directory = ''
        self.max_depth = 0
        self.crawl_interval = 1
        self.crawl_timeout = 10
        self.target_url = ''
        self.thread_count = 1

    def check_config(self):
        """
        check spider config is effect
        """
        if not os.path.isfile(self.url_list_file):
            raise Exception("spider url_list_file is't effect file")

        if self.max_depth < 0:
            raise Exception("spider max_depth can't less 0")

        if self.crawl_interval < 0:
            raise Exception("spider crawl_interval can't less 0")

        if self.crawl_timeout < 0:
            raise Exception("spider crawl_timeout can't less 0")

        if self.thread_count < 0:
            raise Exception("spider thread_count can't less 1")

