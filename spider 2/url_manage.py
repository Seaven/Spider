# coding=utf-8

"""
url set
Author: Seaven
"""

import threading
import Queue


class UrlManage(object):
    def __init__(self):
        self.__url_set = set()
        self.__url_queue = Queue.Queue()
        self.__table_lock = threading.Lock()

    def url_put(self, url, depth=0):
        self.__table_lock.acquire()

        if url not in self.__url_set:
            self.__url_set.add(url)
            self.__url_queue.put({'url': url, 'depth': depth})

        self.__table_lock.release()

    def url_list_put(self, url_list, depth=0):
        if url_list is None or len(url_list) == 0:
            return

        self.__table_lock.acquire()

        for url in url_list:
            if url not in self.__url_set:
                self.__url_set.add(url)
                self.__url_queue.put({'url': url, 'depth': depth})

        self.__table_lock.release()

    def url_pop(self):
        url_dict = {'url': None, 'depth': 0}

        self.__table_lock.acquire()
        if self.__url_queue.not_empty:
            url_dict = self.__url_queue.get()
        self.__table_lock.release()

        return url_dict['url'], url_dict['depth']

    def url_empty(self):
        return self.__url_queue.empty()
