#-*-coding:utf-8-*-
import os
import requests
from lxml import etree
import random
import time
import json
from selenium import webdriver
import re


url='https://www.lsmpx.com/forum.php?mod=viewthread&tid=19741&extra=&highlight=%E5%BF%83%E5%A6%8D&page=5'
option = webdriver.ChromeOptions()
# 这个命令禁止沙箱模式，否则肯能会报错遇到chrome异常。
option.add_argument('--no-sandbox')
# 设置启动无界面化
# option.add_argument('--headless')
# 注意path
browser = webdriver.Chrome(executable_path='/home/szj/softwares/chromedriver', options=option)
browser.get(url)
# browser.find_element_by_xpath('/html/body/div[2]/div[4]/ul/li[1]/a/img').click()
print(browser.current_url)
# 取出网页源码
# page_source = browser.page_source

print(browser.find_element_by_class_name("adw").text)
# print(browser.find_element_by_id("thread-title"))
img=browser.find_elements_by_xpath('//ul[@class]/node()/img')
# img=browser.find_elements_by_xpath('//*[@id="thread-pic"]/ul/li[2]/img')

print(img)

# nextpage=re.compile('</a> <a class="a1" href="(.*?)">下一页</a>',re.S).findall(page_source)
# nextpage=re.findall('<a class="a1" href="(.*?)">下一页</a>',page_source)

# print(page_source)
time.sleep(2)
browser.close()
browser.quit()

