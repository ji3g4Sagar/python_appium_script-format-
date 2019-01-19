#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor, getToast
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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


	def basicMotion(self):
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/animationJson")
		self.sp.swipLeft(n=3)

	def loginWithWrongCountry(self):
		self.basicMotion()
		self.ck.clickByResourceID(self.apkVersionIdName + "/teachCloseLayout")
		self.ck.clickByResourceID(self.apkVersionIdName + "/image_flag")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/image_flag")
		self.ck.clickByResourceID(self.apkVersionIdName + "/image_flag")
		self.ec.enter("0931540341",self.apkVersionIdName + "/et_phone_num")
		self.ec.enter("ji3g4wj6", self.apkVersionIdName + "/et_login_pass")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_login")
		self.gt.search4Toast("此帳號不存在")
		self.wf.implicitWait()
		