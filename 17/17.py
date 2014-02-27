# -*- coding: utf-8 -*- 
from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']
dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('pagination.html')
dr.get(file_path)

#获得所有分页的数量
# -2 是因为要去掉上一个 和下一个
total_pags = len(dr.find_element_by_class_name('pagination').find_elements_by_tag_name('li')) -2

#获得当前的页面的url以及当前页面是第几页
current_page = dr.find_element_by_class_name('pagination').find_element_by_class_name('active')
print "current page is %s" %(current_page.text)
sleep(1)

dr.quit()
