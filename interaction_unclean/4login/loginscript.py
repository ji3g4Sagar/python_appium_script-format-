#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")
from Motion import swipePage, enterContext, click, waittingFor, getToast
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class script():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.gt = getToast(driver)
		self.apkVersionIdName = apkVersionIdName

	def basicMotion(self):
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/animationJson")
		self.sp.swipLeft(n=3)

	def login(self):
		self.basicMotion()
		self.ck.clickByString("立即改變生活")
		self.ec.enter("0999999999",self.apkVersionIdName + "/et_phone_num")
		self.ck.clickByResourceID(self.apkVersionIdName + "/et_login_pass")
		self.ec.enter("111111", self.apkVersionIdName + "/et_login_pass")
		self.ck.clickByString("登入")
		sleep(5)
		"""利用顯式等待等登入後的頁面(動態牆)出現"""
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/fl_homeHealthVideoTitle")
