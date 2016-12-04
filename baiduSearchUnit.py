#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'apple'
__mtime__ = '2016/12/4'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import os
import unittest,time

from selenium import webdriver


class baiduSearchUnit(unittest.TestCase):
	def test_search(self):
		driver = webdriver.Safari()
		try:
			driver.get("http://www.baidu.com")
			print driver.title
			kw = driver.find_element_by_id('kw')
			kw.send_keys('hello')
			driver.find_element_by_id('su').click()
			time.sleep(3)
		except Exception,e:
			print e
		finally:
			driver.quit()
		#self.assertEqual(True, False)

if __name__ == '__main__':
	unittest.main()
