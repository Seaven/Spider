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

import docopt
import spider

"""
Author: Seaven
"""
if __name__ == '__main__':
    args = docopt.docopt(__doc__, version='spider_main_1.0.0.0')
    spider.spider_run(args['-c'])
