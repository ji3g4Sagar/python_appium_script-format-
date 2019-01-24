#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor, getToast
from time import sleep
from appium.webdriver import Remote #for keyevent

class script():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.gt = getToast(driver)
		self.apkVersionIdName = apkVersionIdName


	def addFriend(self):
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 1)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/addFriend")
		self.ck.clickByResourceID(self.apkVersionIdName + "/addFriend")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_otherwayadd")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_otherwayadd")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/icon_picture")
		self.ck.clickByString("手機/信箱")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/et_familyAddFriendSearchFriend_cellphoneNumber")
		self.ec.enter("0911110000", self.apkVersionIdName + "/et_familyAddFriendSearchFriend_cellphoneNumber")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_familyAddFriendSearchFriend_nextStep")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/cb_check")
		self.sp.swipeUp()
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_agree")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_agree")
		#self.gt.search4Toast("此帳號不存在")
		#Toast 訊息內容需再判斷
		sleep(5)

