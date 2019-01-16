#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, clickAndTap, waittingFor, getToast
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class script():
	def __init__(self, driver):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ct = clickAndTap(driver)
		self.wf = waittingFor(driver)
		self.gt = getToast(driver)

	def basicMotion(self):
		sleep(4)
		self.sp.swipLeft(n=3)

	def loginWithWrongCountry(self):
		self.basicMotion()
		self.ct.click("com.lavidatec.wacare:id/teachCloseLayout")
		self.ct.click("com.lavidatec.wacare:id/image_flag")
		self.wf.explicitWait("com.lavidatec.wacare:id/image_flag")
		self.ct.click("com.lavidatec.wacare:id/image_flag")
		self.ec.enter("0931540341","com.lavidatec.wacare:id/et_phone_num")
		self.ec.enter("ji3g4wj6", "com.lavidatec.wacare:id/et_login_pass")
		self.ct.click("com.lavidatec.wacare:id/tv_login")
		self.gt.search4Toast("此帳號不存在")
		sleep(5)
		"""利用顯式等待等登入後的頁面(動態牆)出現"""
		#self.wf.explicitWait("com.lavidatec.wacare:id/home_tab_icon")
