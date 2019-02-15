#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import *
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver import Remote #for keyevent
import random



class scriptExpertAnswer():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.gt = getToast(driver)
		self.xy = getXYLocation(driver)
		self.hp = homePage(driver, apkVersionIdName)
		self.apkVersionIdName = apkVersionIdName
	def starter(self):
		self.clickExpert()

	def clickExpert(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/et_search_keyword")
		self.ck.clickByString("醫護人員")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/tv_quick_search")
		self.ck.clickByString(" 快速搜尋 ")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/tv_select_all")
		self.ck.clickByResourceID(self.apkVersionIdName+"tv_select_all")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_submit")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/tv_sex")
		

		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
		sleep(5)



"""
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
"""


























