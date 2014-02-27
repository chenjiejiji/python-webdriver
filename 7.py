from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ:del os.environ['HTTP_PROXY']

dr = webdriver.Ie()

frist_url = 'http://www.baidu.com'
print "now access %s"%(frist_url)

dr.get(frist_url)
sleep(1)
second_url = 'http://www.news.baidu.com'
print "now access %s"%(second_url)
dr.get(second_url)
sleep(1)

print "back to %s"%(first_url)
dr.back()
sleep(1)
print "forward to %s"%(second_url)
dr.forward()
sleep(1)
dr.quit()
