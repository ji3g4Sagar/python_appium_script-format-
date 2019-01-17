#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor, getToast
from time import sleep

class script():
	def __init__(self, driver):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.gt = getToast(driver)

	def basicMotion(self):
		sleep(4)
		self.sp.swipLeft(n=3)

	def login(self):
		self.basicMotion()
		self.ck.clickByResourceID("com.lavidatec.wacare:id/teachCloseLayout")
		self.ec.enter("0931540341","com.lavidatec.wacare:id/et_phone_num")
		self.ec.enter("ji3g4wj6", "com.lavidatec.wacare:id/et_login_pass")
		self.ck.clickByResourceID("com.lavidatec.wacare:id/tv_login")
		"""利用顯式等待等登入後的頁面(動態牆)出現"""
		self.wf.explicitWaitByResourceID("com.lavidatec.wacare:id/home_tab_icon")

	def addFriend(self):
		self.login()
		self.ck.clickFromManyThingsByResourceID("com.lavidatec.wacare:id/home_tab_icon", 1)
		self.wf.explicitWaitByResourceID("com.lavidatec.wacare:id/addFriend")
		self.ck.clickByResourceID("com.lavidatec.wacare:id/addFriend")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacare:id/tv_otherwayadd")
		self.ck.clickByResourceID("com.lavidatec.wacare:id/tv_otherwayadd")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacare:id/icon_picture")
		self.ck.clickByResourceID("com.lavidatec.wacare:id/icon_picture")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacare:id/et_familyAddFriendSearchFriend_cellphoneNumber")
		self.ec.enter("0999999999", "com.lavidatec.wacare:id/et_familyAddFriendSearchFriend_cellphoneNumber")
		self.ck.clickByResourceID("com.lavidatec.wacare:id/tv_familyAddFriendSearchFriend_nextStep")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacare:id/cb_check")
		self.sp.swipeUp()
		self.wf.explicitWaitByResourceID("com.lavidatec.wacare:id/tv_agree")
		self.ck.clickByResourceID("com.lavidatec.wacare:id/tv_agree")
		self.gt.search4Toast("此帳號已被邀請過")

		
		sleep(5)

