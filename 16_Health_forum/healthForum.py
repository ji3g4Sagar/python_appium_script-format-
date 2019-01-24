#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 

import os
import unittest
from appium import webdriver
from healthForumScript import *
from apkVersionAndCellConfig import Config


class WaCareTest(unittest.TestCase):
	def setUp(self):
		configfile = Config()
		self.driver = configfile.getDriver()
		sleep(3)
		self.apkVersionIdName = configfile.getApkVersionIdName()

	def tearDown(self):
		self.driver.quit()

	def test1_Topic(self):
		testScript = scriptForHelthForum_1_1(self.driver, self.apkVersionIdName)
		testScript.starter()
		testScript = scriptForHelthForum_1_2(self.driver, self.apkVersionIdName)
		testScript.starter()
	#def test2_ReplayPostSelf(self):
		


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest)  
    unittest.TextTestRunner(verbosity=0).run(suite)
