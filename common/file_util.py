# coding=utf-8

"""
file util, support spider file read/write method
Author: Seaven
"""
import os


def file_save(filename, path, content):
    """
    save file
    :param filename: save file name
    :param path: file path
    :param content: file content
    """
    if filename is None or path is None:
        return

    try:
        if not os.path.exists(path):
            os.makedirs(path)

        with open(path + filename, 'w') as save_file:
            save_file.write(content)

    except Exception as e:
        raise e


def read_file(file_path):
    """
    read file
    :param file_path: url seed file path
    :return: content list
    """
    list = []
    try:
        with open(file_path, 'r') as seed_file:
            # avoid null line and '\n'
            list = [line[:-1] for line in seed_file if line[:-1] != '']
    except Exception as e:
        raise e

    return list


