#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import unittest
from appium import webdriver
from testingScript import script
from apkVersionAndCellConfig import Config
from time import sleep
from appium.webdriver import Remote #for keyevent
import random



class WaCareTest(unittest.TestCase):
	def setUp(self):
		configfile = Config(apkName="qaExternalWaCare-v1.0.6.0.6.apk")
		self.driver = configfile.getDriver()
		self.driver.implicitly_wait(10)#隱式等待
		self.apkVersionIdName = configfile.getApkVersionIdName()

	def tearDown(self):
		self.driver.quit()

	def test(self):
		test = script(self.driver, self.apkVersionIdName)
		test.starter()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest)  
    unittest.TextTestRunner(verbosity=0).run(suite)