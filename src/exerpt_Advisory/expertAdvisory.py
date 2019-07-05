#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 
import os
import unittest
from appium import webdriver
from expertAdvisoryScript import script
from apkVersionAndCellConfig import Config


class WaCareTest(unittest.TestCase):
	def setUp(self):
		configfile = Config()
		self.driver = configfile.getDriver()
		self.driver.implicitly_wait(10)
		self.apkVersionIdName = configfile.getApkVersionIdName()

	def tearDown(self):
		self.driver.quit()

	def test_Topic(self):
		testScript = script(self.driver, self.apkVersionIdName)
		testScript.starter()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest)  
    unittest.TextTestRunner(verbosity=0).run(suite)
