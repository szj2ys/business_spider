#-*-coding:utf-8-*-
import os
import time
from selenium import webdriver

URL = 'https://www.meitulu.com/t/1283/'
PIC_PATH = os.path.join(os.path.expanduser('~'), '/home/szj/spider/')
PIC_NAME = 'screenshot.png'


def screenshot_web(url=URL, path=PIC_PATH, name=PIC_NAME):
    '''capture the whole web page
    :param url: the website url
    :type url: str
    :param path: the path for saving picture
    :type str
    :param name: the name of picture
    :type name: str
    '''
    if not os.path.exists(path):
        os.makedirs(path)
    browser = webdriver.PhantomJS(executable_path='/usr/local/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
    browser.set_window_size(1200, 2800)
    browser.get(url)
    time.sleep(3)
    pic_path = os.path.join(os.path.join(path, name))
    print(pic_path)
    if browser.save_screenshot(pic_path):
        print('Done!')
    else:
        print('Failed!')
    browser.close()


if __name__ == '__main__':
    screenshot_web()