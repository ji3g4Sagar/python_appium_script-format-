#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor, findSpecificText
from time import sleep
from appium.webdriver import Remote #for keyevent
import random

class script():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.ft = findSpecificText(driver)
		self.apkVersionIdName = apkVersionIdName

	def sendMessage(self):
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 3)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_head")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_head")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/familyChatRoomMessage")
		enterstring = str(random.randint(1,1000)) + " Hey there"
		self.ck.clickByResourceID(self.apkVersionIdName + "/familyChatRoomMessage")
		self.ec.enter(enterstring , self.apkVersionIdName + "/familyChatRoomMessage")
		self.ck.clickByResourceID(self.apkVersionIdName + "/familyChatRoomSend")
		self.ft.findText(enterstring)
		sleep(5)

		#利用timestamp來檢查是否有把訊息丟出去
		#待修
