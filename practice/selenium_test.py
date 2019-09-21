#-*-coding:utf-8-*-
from selenium import webdriver
import time


def spider(url='https://www.baidu.com/'):
    option = webdriver.ChromeOptions()
    # 这个命令禁止沙箱模式，否则肯能会报错遇到chrome异常。
    option.add_argument('--no-sandbox')
    # 设置启动无界面化
    # option.add_argument('--headless')
    # 注意path
    browser = webdriver.Chrome(executable_path='/home/szj/softwares/chromedriver', options=option)
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="kw"]').clear()
    img_src = browser.find_element_by_xpath('//*[@id="kw"]').send_keys("美女")
    browser.find_element_by_xpath('//*[@id="su"]').click()

    time.sleep(3)
    print(img_src)
    browser.quit()
    # 将网页保存为图片
    # browser.get_screenshot_as_file("./bing.png")
    # print(driver.page_source)
spider()