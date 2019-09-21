#-*-coding:utf-8-*-
from selenium import webdriver



def spider(url='http://bing.com'):
    option = webdriver.ChromeOptions()
    # 这个命令禁止沙箱模式，否则肯能会报错遇到chrome异常。
    option.add_argument('--no-sandbox')
    option.add_argument('--headless')
    # 注意path
    driver = webdriver.Chrome(executable_path='/home/szj/softwares/chromedriver', chrome_options=option)
    driver.get(url)
    print(driver.page_source)
spider()