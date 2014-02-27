from selenium import webdriver
import time

dr = webdriver.Ie()
# dr = webdriver.Firefox()
# dr = webdriver.Chome()
time.sleep(2)

print 'browser will be closed'
dr.quit()# or dr.close()
print 'browser is closed'
