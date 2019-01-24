#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor
from time import sleep

class script():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.apkVersionIdName = apkVersionIdName

	def addBloodPressure(self):
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/fl_homeHealthVideoTitle")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 1)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_status_level")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/tv_status_level", 1)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_next")
		self.sp.swipeUp(n=1)
		self.ck.clickByString("血壓")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/ivAdd")
		"""無法新增血壓"""
		self.wf.implicitWait()

