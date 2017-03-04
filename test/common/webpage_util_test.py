# coding=utf-8

"""
Author: Seaven
"""

import unittest
from common import webpage_util


class WebPageUtilTest(unittest.TestCase):
    def test_get_page_content(self):
        html = webpage_util.get_page_content('http://www.baidu.com')

        self.assertIsNotNone(html, 'get page content error')

    def test_get_page_urls(self):
        html = """
            <html>
                <body>
                    <a href='/helloworld.html' />
                    <div><a href='http://weibo.com'></div>
                </body>
            </html>
        """

        base_url = 'http://www.baidu.com'

        urls = webpage_util.get_page_urls(base_url, html)

        self.assertEqual(len(urls), 2, 'get urls from html error')
        self.assertEqual('http://www.baidu.com/helloworld.html' in urls, True, 'package urls error')

    def test_url_escape(self):
        url = "http://www.baidu.com/test.jpg"
        escape_url = webpage_util.url_escape(url)

        self.assertEqual('/' in escape_url, False, 'escape url error')

    def test_is_match_url(self):
        regex = ur'www\.baidu\.com'

        result = webpage_util.is_match_url(regex, 'https://www.baidu.com/test.jpg')
        self.assertEqual(result, True, 'url match error')

        result = webpage_util.is_match_url(regex, 'https://www.sina.com/test.html')
        self.assertEqual(result, False, 'url match error')


if __name__ == '__main__':
    unittest.main()
