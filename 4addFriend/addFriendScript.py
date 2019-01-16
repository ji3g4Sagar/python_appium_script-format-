#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, clickAndTap, waittingFor
from time import sleep

class script():
	def __init__(self, driver):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ct = clickAndTap(driver)
		self.wf = waittingFor(driver)

	def basicMotion(self):
		sleep(4)
		self.sp.swipLeft(n=3)

	def login(self):
		self.basicMotion()
		self.ct.click("com.lavidatec.wacare:id/teachCloseLayout")
		self.ec.enter("0931540341","com.lavidatec.wacare:id/et_phone_num")
		self.ec.enter("ji3g4wj6", "com.lavidatec.wacare:id/et_login_pass")
		self.ct.click("com.lavidatec.wacare:id/tv_login")
		"""利用顯式等待等登入後的頁面(動態牆)出現"""
		self.wf.explicitWait("com.lavidatec.wacare:id/home_tab_icon")

	def addFriend(self):
		self.login()
		self.ct.clickFromManyThings("com.lavidatec.wacare:id/home_tab_icon", 1)
		self.wf.explicitWait("com.lavidatec.wacare:id/addFriend")
		self.ct.click("com.lavidatec.wacare:id/addFriend")
		self.wf.explicitWait("com.lavidatec.wacare:id/tv_otherwayadd")
		self.ct.click("com.lavidatec.wacare:id/tv_otherwayadd")
		self.wf.explicitWait("com.lavidatec.wacare:id/icon_picture")
		self.ct.click("com.lavidatec.wacare:id/icon_picture")
		self.wf.explicitWait("com.lavidatec.wacare:id/et_familyAddFriendSearchFriend_cellphoneNumber")
		self.ec.enter("0911110000", "com.lavidatec.wacare:id/et_familyAddFriendSearchFriend_cellphoneNumber")
		self.ct.click("com.lavidatec.wacare:id/tv_familyAddFriendSearchFriend_nextStep")
		self.wf.explicitWait("com.lavidatec.wacare:id/cb_check")
		self.sp.swipeUp()
		self.wf.explicitWait("com.lavidatec.wacare:id/tv_agree")
		self.ct.click("com.lavidatec.wacare:id/tv_agree")


		
		sleep(5)

