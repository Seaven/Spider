# coding=utf-8

"""spider_main.
Usage:
    spider_main.py -c <config_file>
    spider_main.py (-h | --help)
    spider_main.py (-v | --version)

Options:
-c file        Run spider use the config file
-h --help      Show this screen.
-v --version   Show version.

"""

import config_load
import spider
import docopt
import url_manage
from common import thread_task
from common import file_util

"""
Author: Seaven
"""


# spider run method
def spider_run(config_file):
    # read config
    spider_config = config_load.read_config(config_file)
    urls = file_util.read_file(spider_config.url_list_file)

    # set urls, build task
    url_center = url_manage.UrlManage()
    url_center.url_list_put(urls)

    # set spider
    spider_func_list = []
    for i in xrange(spider_config.thread_count):
        sp = spider.Spider(spider_config, url_center)
        spider_func_list.append(sp.craw)

    task = thread_task.ThreadTask(spider_func_list)

    # craw start
    task.task_start()


if __name__ == '__main__':
    args = docopt.docopt(__doc__, version='spider_main_1.0.0.0')
    spider_run(args['-c'])
