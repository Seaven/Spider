# coding=utf-8

"""
Thread Task
Author: Seaven
"""

import threading
import log_util
import traceback

task_log = log_util.get_logger('ThreadTask')

TASK_STATUS_READY = 1
TASK_STATUS_RUNNING = 2
TASK_STATUS_FINISH = 3
TASK_STATUS_ERROR = 4


class ThreadTask(object):
    """
    build a task, run a group function by multi thread
    """
    def __init__(self, run_func_list, end_func=lambda: "Task End!"):
        self.end_func = end_func
        self.thread_list = list()
        self.__init_threads(run_func_list)

    def __init_threads(self, run_func_list):
        for i in xrange(len(run_func_list)):
            self.thread_list.append(ExecuteThread(i, run_func_list[i]))

    def task_start(self):
        task_log.info('Thread Task start run.')

        for i in xrange(len(self.thread_list)):
            try:
                self.thread_list[i].start()
            except Exception as e:
                task_log.warn(
                    "Thread Task run warn, Thread %d : %s"
                    % (self.thread_list[i].thread_id, traceback.format_exc(e)))

        while not self.task_is_finish():
            pass

        self.task_finish()
        task_log.info('Thread Task finish run.')

    def task_is_finish(self):
        for i in self.thread_list:
            status = i.is_finish()
            if status == TASK_STATUS_READY or status == TASK_STATUS_RUNNING:
                return False

        return True

    def task_finish(self):
        task_log.info('Thread Task start end method.')
        try:
            self.end_func()
        except Exception as e:
            task_log.error('Thread Task end error, cause : ' % traceback.format_exc(e))
        finally:
            task_log.info('Thread Task finish end method.')


execute_log = log_util.get_logger('ExecuteThread')


class ExecuteThread(threading.Thread):
    def __init__(self, thread_id, run_func):
        super(ExecuteThread, self).__init__()
        self.thread_id = thread_id
        self.run_func = run_func
        self.__status = TASK_STATUS_READY
        self.__status_message = ''

    def run(self):
        execute_log.info('Execute Thread %d, start run.' % self.thread_id)
        self.__pre_run()
        try:
            self.run_func()
            self.__aft_run()
        except Exception as e:
            execute_log.warn('Execute Thread %d error, cause : %s' % (self.thread_id, e.message))
            self.__error(e.message)
        finally:
            execute_log.info('Execute Thread %d, run end.' % self.thread_id)

    def is_finish(self):
        return self.__status

    def get_finish_message(self):
        return self.__status_message

    def __error(self, error_info):
        self.__status = TASK_STATUS_ERROR
        self.__status_message = 'Thread %d Error, cause : %s' % (self.thread_id, error_info)

    def __aft_run(self):
        self.__status = TASK_STATUS_FINISH
        self.__status_message = 'Success'

    def __pre_run(self):
        self.__status = TASK_STATUS_RUNNING
        self.__status_message = 'Running'
