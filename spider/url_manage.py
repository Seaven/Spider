# coding=utf-8

"""
url set
Author: Seaven
"""

import threading


class UrlManage(object):
    """
    support a url set, to filter repeat url
    """
    def __init__(self):
        self.__url_set = set()
        # lock
        self.__table_lock = threading.Lock()

    def url_put(self, url):
        self.__table_lock.acquire()

        self.__url_set.add(url)

        self.__table_lock.release()

    def url_is_contains(self, url):
        self.__table_lock.acquire()

        if url in self.__url_set:
            is_contain = True
        else:
            is_contain = False

        self.__table_lock.release()

        return is_contain
