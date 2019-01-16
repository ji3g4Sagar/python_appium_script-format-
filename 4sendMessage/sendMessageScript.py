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
		self.sp.swipLeft(n=4)

	def login(self):
		self.basicMotion()
		self.ct.click("com.lavidatec.wacare:id/teachCloseLayout")
		self.ec.enter("0931540341","com.lavidatec.wacare:id/et_phone_num")
		self.ec.enter("ji3g4wj6", "com.lavidatec.wacare:id/et_login_pass")
		self.ct.click("com.lavidatec.wacare:id/tv_login")
		"""利用顯式等待等登入後的頁面(動態牆)出現"""
		self.wf.explicitWait("com.lavidatec.wacare:id/home_tab_icon")

	def sendMessage(self):
		self.login()
		self.ct.clickFromManyThings("com.lavidatec.wacare:id/home_tab_icon", 3)
		self.wf.explicitWait("com.lavidatec.wacare:id/iv_head")
		self.ct.click("com.lavidatec.wacare:id/iv_head")
		self.wf.explicitWait("com.lavidatec.wacare:id/familyChatRoomMessage")
		enterstring = ""
		self.ct.click("com.lavidatec.wacare:id/familyChatRoomMessage")
		self.ec.enter(enterstring , "com.lavidatec.wacare:id/familyChatRoomMessage")
		self.ct.click("com.lavidatec.wacare:id/familyChatRoomSend")
		target = self.driver.find_elements_by_id("com.lavidatec.wacare:id/myMessage")
		sleep(5)

