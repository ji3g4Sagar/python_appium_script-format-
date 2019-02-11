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

	def addMotion(self):
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 1)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_status_level")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/tv_status_level", 1)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_next")
		self.sp.swipeUp(n=1)
		self.ck.clickByString("心情")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/addEmotion")
		self.ck.clickByResourceID(self.apkVersionIdName + "/addEmotion")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/faceImage4")
		self.ck.clickByResourceID(self.apkVersionIdName + "/faceImage5")
		self.ec.enter("心情還不錯", self.apkVersionIdName + "/emotionContent")
		self.ck.clickByResourceID(self.apkVersionIdName + "/myEmotionPostText")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/addEmotion")
		self.driver.keyevent("4")
		sleep(5)

