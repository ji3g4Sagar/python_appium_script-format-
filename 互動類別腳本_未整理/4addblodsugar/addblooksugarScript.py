#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor
from time import sleep
import random
from appium.webdriver import Remote #for keyevent


class script():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.apkVersionIdName = apkVersionIdName

	def addbloodsugar(self):
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/fl_homeHealthVideoTitle")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 1)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_status_level")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/tv_status_level", 1)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_next")
		self.sp.swipeUp(n=1)
		#self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/healthLeveltx", 3)
		self.ck.clickByString("血糖")
		print(self.apkVersionIdName + "/iv_mybloodSugar_Plus")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_mybloodSugar_Plus")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_mybloodSugar_Plus")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_measure_time")
		self.ck.clickByString("午餐前")
		sugarNumber = random.randint(70,99)
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_next_step")
		self.ec.enter(str(sugarNumber), self.apkVersionIdName + "/et_blood_sugar")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_submit")
		self.driver.keyevent("4")
		sleep(5)

