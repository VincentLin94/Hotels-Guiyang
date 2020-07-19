# -*-coding:UTF-8 -*-

from CtripDownloader import Downloader
from bs4 import BeautifulSoup


class Parser(object):

    def parse(self, content):
        '''
        Parse the html content using BeautifulSoup
        :param content: Content downloaded by Downloader
        :return:
        '''
        hotel_list = []

        # Find all the key tags
        for a, c in enumerate(content):
            soup = BeautifulSoup(c, 'html.parser')
            hotels = soup.find_all('div', class_='hotel_new_list J_HotelListBaseCell')

            # Separate the tags to get right info
            for n, i in enumerate(hotels):
                hotel = i.find('a', href=True)
                name = hotel['title']
                url = 'https://hotels.ctrip.com' + hotel['href']
                url = url.replace('?isFull=F', '')
                addrs = i.find('p', class_='hotel_item_htladdress').text
                tags = i.find('span', class_='special_label').text
                icons = i.find('div', class_='icon_list').find_all('i')
                facilities = str()
                for f in icons:
                    text = f['title']
                    facilities = facilities + text
                price = i.find('span', class_='J_price_lowList').text
                score = i.find('a', class_='hotel_judge')['title']
                comments = i.find('span', class_='hotel_judgement').text
                briefs = i.find('span', class_='recommend')
                if briefs is None:
                    briefs = 'None'
                else:
                    briefs = briefs.text
                data = (name, url, addrs, tags, facilities, price, score, comments, briefs)
                hotel_list.append(data)
                print(str('Page number: %s has been parsed.' % (a+1)))

        print('All pages have been successfully parsed! Waiting for storage...')
        return hotel_list


# Troubleshoot for this section
'''
if __name__ == '__main__':
    url = 'https://www.ctrip.com/'
    d = Downloader()
    p = Parser()
    content = d.download(url)
    datas = p.parse(content)
    print(datas)
'''


