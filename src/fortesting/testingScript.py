#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import *
#from logging import Log
from time import sleep
from appium.webdriver import Remote #for keyevent
import random


class script():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.ct = getContext(driver)
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.ft = findSpecificText(driver)
		self.xy = getXYLocation(driver)
		self.ft = findSpecificText(driver)
		self.apkVersionIdName = apkVersionIdName
		self.hp = homePage(driver, apkVersionIdName)

	def starter(self):
		self.getContextTesting()

	def getContextTesting(self):
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		print("Check for default announcement.....")
		self.hp.goBackToHomePage()
		print(self.ct.context())
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
		sleep(5)