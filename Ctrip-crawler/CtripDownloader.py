# -*- coding:UTF-8 -*-

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json


class Downloader(object):

    def download(self, url):
        '''
        Download target page source using Selenium
        :param url: Target url
        :return:
        '''
        # Preset parameters for browser
        chrome_set = Options()
        chrome_set.add_argument('--headless')
        chrome_set.add_argument('disable-gpu')
        chrome_set.add_argument('--window-size=1600,900')
        browser = webdriver.Chrome(chrome_options=chrome_set)
        browser.get(url=url)

        # Get cookies to bypass the login process
        f = open('cookie.txt')
        cookies = f.read()
        cookies = json.loads(cookies)
        for c in cookies:
            browser.add_cookie(c)
        browser.refresh()

        # Search by city name and date
        location = browser.find_element_by_xpath('//*[@id="HD_CityName"]')
        location.clear()
        location.send_keys('贵阳')
        date_in = browser.find_element_by_xpath('//*[@id="HD_CheckIn"]')
        date_in.clear()
        date_in.send_keys('2020-07-26')
        data_out = browser.find_element_by_xpath('//*[@id="HD_CheckOut"]')
        data_out.clear()
        data_out.send_keys('2020-07-27')
        data_out.send_keys(Keys.RETURN)
        time.sleep(5)

        # Get the source of the first ten pages

        js = 'arguments[0].scrollIntoView();'
        contents = []
        for i in range(10):
            # browser.execute_script(js, next_page)
            contents.append(browser.page_source)
            next_page = browser.find_element_by_xpath('//*[@id="downHerf"]')
            next_page.click()
            time.sleep(5)

        # Return page source for parsing
        browser.close()
        print('Page content successfully downloaded! Waiting for parsing...')
        return contents


# Troubleshoot for this section
'''
if __name__ == '__main__':
    d = Downloader()
    res = d.download('https://www.ctrip.com/')
    print(res)
'''
