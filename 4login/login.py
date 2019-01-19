#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 

import os
import unittest
from appium import webdriver
from loginscript import script
from apkVersionAndCellConfig import Config

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WaCareTest(unittest.TestCase):
	def setUp(self):
		configFile = Config()
		self.driver = configFile.getDriver()
		self.driver.implicitly_wait(10)
		self.apkVersionIdName = configFile.getApkVersionIdName()
		
	def tearDown(self):
		self.driver.quit()

	def test(self):
		test = script(self.driver, self.apkVersionIdName)
		test.login()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest)  
    unittest.TextTestRunner(verbosity=0).run(suite)













