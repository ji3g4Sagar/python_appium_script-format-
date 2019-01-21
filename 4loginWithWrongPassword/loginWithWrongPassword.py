#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 

import os
import unittest
from appium import webdriver
from loginWithWrongPasswordScript import script
from apkVersionAndCellConfig import Config
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WaCareTest(unittest.TestCase):
	def setUp(self):
		#configfile = Config(apkName = "proWaCare-v1.0.1.4.apk")# For 正式站
		configfile = Config(apkName = "qaExternalWaCare-v1.0.3.1.3.apk")
		self.driver = configfile.getDriver()
		self.apkVersionIdName = configfile.getApkVersionIdName()
		sleep(5)

	def tearDown(self):
		self.driver.quit()

	def test(self):
		test = script(self.driver, self.apkVersionIdName)
		test.loginWithWrongPassword()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest)  
    unittest.TextTestRunner(verbosity=0).run(suite)