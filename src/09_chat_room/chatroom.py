#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 
import os
import unittest
from appium import webdriver
from chatroomScript import script
from apkVersionAndCellConfig import Config
from time import sleep

class WaCareTest(unittest.TestCase):
	def setUp(self):
		configfile = Config()
		self.driver = configfile.getDriver()
		sleep(5)
		self.apkVersionIdName = configfile.getApkVersionIdName()

	def tearDown(self):
		self.driver.quit()

	def test(self):
		testscript = script(self.driver, self.apkVersionIdName)
		testscript.sendMessage()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest)  
    unittest.TextTestRunner(verbosity=0).run(suite)






