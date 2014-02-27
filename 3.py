from selenium import webdriver
import time

dr = webdriver.Ie()
#dr = webdriver.Chrome()
#dr = webdriver.Firefox()

time.sleep(2)
print "maximize browser"

dr.maximize_window()

time.sleep(2)
print 'close browser'

dr.quit()
