from selenium import webdriver
import time

dr = webdriver.Ie()
#dr = webdriver.Firefox()
#dr = webdriver.Chrome()

dr.set_window_size(500,320)
dr.get('http://www.3g.qq.com')
time.sleep(5)
dr.quit()
