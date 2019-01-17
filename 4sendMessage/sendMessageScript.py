#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor
from time import sleep

class script():
	def __init__(self, driver):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)

	def basicMotion(self):
		self.wf.explicitWaitByResourceID("com.lavidatec.wacare:id/animationJson")
		self.sp.swipLeft(n=3)

	def login(self):
		self.basicMotion()
		self.ck.clickByResourceID("com.lavidatec.wacare:id/teachCloseLayout")
		self.ec.enter("0931540341","com.lavidatec.wacare:id/et_phone_num")
		self.ec.enter("ji3g4wj6", "com.lavidatec.wacare:id/et_login_pass")
		self.ck.clickByResourceID("com.lavidatec.wacare:id/tv_login")
		"""利用顯式等待等登入後的頁面(動態牆)出現"""
		self.wf.explicitWaitByResourceID("com.lavidatec.wacare:id/fl_homeHealthVideoTitle")

	def sendMessage(self):
		self.login()
		self.ck.clickFromManyThingsByResourceID("com.lavidatec.wacare:id/home_tab_icon", 3)
		self.wf.explicitWaitByResourceID("com.lavidatec.wacare:id/iv_head")
		self.ck.clickByResourceID("com.lavidatec.wacare:id/iv_head")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacare:id/familyChatRoomMessage")
		enterstring = "Hey there"
		self.ck.clickByResourceID("com.lavidatec.wacare:id/familyChatRoomMessage")
		self.ec.enter(enterstring , "com.lavidatec.wacare:id/familyChatRoomMessage")
		self.ck.clickByResourceID("com.lavidatec.wacare:id/familyChatRoomSend")
		self.wf.implicitWait()
		#利用timestamp來檢查是否有把訊息丟出去
		#待修
