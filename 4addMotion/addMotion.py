#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 

import os
import unittest
from appium import webdriver
from addMotionScript import script

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WaCareTest(unittest.TestCase):
	def setUp(self):
		desired_caps = {} # Appium收到http Request後會解析這個key-value pair
		app = ('http://35.194.192.102:5000/getfile?filename=proWaCare-v1.0.1.4.apk')
		desired_caps['app'] = app
		desired_caps['platformName'] = 'Android' #定義測試的系統環境
		desired_caps['platformVersion'] = '5.1.1' #定義版本
		desired_caps['deviceName'] = 'Android Emulator' #定義裝置名稱
		desired_caps['automationName'] = 'uiautomator2'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(10)#隱式等待

	def tearDown(self):
		self.driver.quit()

	def test(self):
		test = script(self.driver)
		test.addMotion()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest)  
    unittest.TextTestRunner(verbosity=0).run(suite)













