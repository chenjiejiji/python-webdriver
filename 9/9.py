# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html')
dr.get(file_path)

#ѡ�����е�checkbox��ȫ������
checkboxs = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxs:
    checkbox.click()

time.sleep(1)
dr.refresh()
time.sleep(2)

#��ӡ��ǰҳ�����ж��ٸ�checkbox
print len(dr.find_elements_by_css_selector('input[type=checkbox]'))

#ѡ��ҳ�������е�input��Ȼ����й��˳����е�checkbox����ѡ֮
inputs = dr.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()

time.sleep(1)

#��ҳ�������һ��checkbox�Ĺ�ȥ��
dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()

time.sleep(1)

dr.quit()
