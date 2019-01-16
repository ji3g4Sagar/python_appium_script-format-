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

	def addMotion(self):
		self.login()
		self.ct.clickFromManyThings("com.lavidatec.wacare:id/home_tab_icon", 1)
		self.wf.explicitWait("com.lavidatec.wacare:id/tv_status_level")
		self.ct.clickFromManyThings("com.lavidatec.wacare:id/tv_status_level", 1)
		self.wf.explicitWait("com.lavidatec.wacare:id/iv_next")
		self.ct.clickFromManyThings("com.lavidatec.wacare:id/iv_next", 1)
		self.wf.explicitWait("com.lavidatec.wacare:id/addEmotion")
		self.ct.click("com.lavidatec.wacare:id/addEmotion")
		self.wf.explicitWait("com.lavidatec.wacare:id/faceImage4")
		self.ct.click("com.lavidatec.wacare:id/faceImage4")
		self.ec.enter("心情還不錯", "com.lavidatec.wacare:id/emotionContent")
		self.ct.click("com.lavidatec.wacare:id/myEmotionPostText")
		self.wf.explicitWait("com.lavidatec.wacare:id/addEmotion")
		sleep(5)

