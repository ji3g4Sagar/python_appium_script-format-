#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 
import os
import unittest
from appium import webdriver
from healthBulbICScript import script
from apkVersionAndCellConfig import Config


class WaCareTest(unittest.TestCase):
	def setUp(self):
		configfile = Config()
		self.driver = configfile.getDriver()
		self.driver.implicitly_wait(10)
		self.apkVersionIdName = configfile.getApkVersionIdName()

	def tearDown(self):
		self.driver.quit()

	def test(self):
		test = script(self.driver, self.apkVersionIdName)
		test.starter()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest)  
    unittest.TextTestRunner(verbosity=0).run(suite)
