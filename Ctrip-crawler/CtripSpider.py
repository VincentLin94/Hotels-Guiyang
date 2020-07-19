# -*- coding:utf-8 -*-

from CtripDownloader import Downloader
from CtripParser import Parser
from CtripStorage import Storage


class Spider(object):

    def __init__(self):
        self.downloader = Downloader()
        self.parser = Parser()
        self.storage = Storage()

    def crawl(self, url):
        '''
        Main function to initialize the whole crawler
        :param url: Target url
        :return:
        '''
        try:
            content = self.downloader.download(url)
            datas = self.parser.parse(content)
            self.storage.write_head()
            self.storage.write_data(datas)
            self.storage.write_end()
        except Exception:
            print('Crawling failed!')
        print('Crawling finished!')


# Commence the crawling
if __name__ == '__main__':
    url = 'https://www.ctrip.com/'
    spider = Spider()
    spider.crawl(url)



