  #!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor
from time import sleep
from appium.webdriver import Remote #for keyevent

class script():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.apkVersionIdName = apkVersionIdName

	def recommendFriend(self):
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 3)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_head")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_head")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_function_list")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_function_list")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_function_close")
		self.ck.clickByString("推薦親友")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/inviteButton")
		self.ck.clickByString("推薦")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/intentButton")
		sleep(5)

