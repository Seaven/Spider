# coding=utf-8

"""
html page util
Author: Seaven
"""

import urllib2
import urlparse
import re
import bs4
import contextlib


def get_page_content(url, time_out=10):
    """
    get web page html
    :param url: target url
    :param time_out: connection url timeout
    :return: page html
    """
    if url is None or url is '':
        return

    html = ''
    try:
        with contextlib.closing(urllib2.urlopen(url, timeout=time_out)) as response:
            if response is not None and response.getcode() == 200:
                html = response.read()
    except Exception as e:
        raise e

    return html


def get_page_urls(page_url, html):
    """
    get urls where is in the page html
    :param page_url: page base url
    :param html: page content html
    :return: urls where is in page
    """
    soup = bs4.BeautifulSoup(html, 'html.parser', from_encoding='uft-8')
    urls = set()

    try:
        links = soup.find_all('a', href=True)

        for link in links:
            href_url = link['href']
            new_url = urlparse.urljoin(page_url, href_url)

            # avoid some script url which is like <a href='javascript:void(0)'>
            if new_url.startswith(r'http'):
                urls.add(new_url)
    except Exception as e:
        raise e

    return list(urls)


def url_escape(url):
    """
    escape url to safe
    :param url: target url
    :return: escape url string
    """
    # urllib2.quote default safe = '/', but file name can't contains '/'
    return urllib2.quote(url, safe='')


def is_match_url(regex, url):
    """
    match url use regex, if match return True
    :param regex: url regex
    :param url: target url
    :return: Boolean
    """
    pattern = re.compile(regex, re.S)

    url_list = pattern.findall(url)

    if any(url_list):
        return True

    return False
