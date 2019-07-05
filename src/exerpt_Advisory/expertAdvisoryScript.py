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



class script():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.gt = getToast(driver)
		self.xy = getXYLocation(driver)
		self.hp = homePage(driver, apkVersionIdName)
		self.ft = findSpecificText(driver)
		self.apkVersionIdName = apkVersionIdName
	def starter(self):
		""""""
		self.bookExpert()
		self.quickSearch()
		
	def bookExpert(self):
		self.hp.goBackToHomePage()
		actionSuccess = True
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",2)
		self.ft.findText("找專家")
		self.ck.clickByString("找專家")
		self.ft.findText(" 快速搜尋 ")
		expertNameXpath = '//*[@text=\'{}\']/parent::android.widget.LinearLayout\
										/parent::android.widget.LinearLayout\
										/following-sibling::android.widget.FrameLayout\
										/child::androidx.recyclerview.widget.RecyclerView\
										/child::android.widget.LinearLayout\
										/child::android.widget.LinearLayout\
										/child::android.widget.LinearLayout\
										/following-sibling::android.widget.LinearLayout\
										/child::android.widget.LinearLayout\
										/child::android.widget.LinearLayout\
										/child::android.widget.TextView'.format(" 快速搜尋 ")
		expertNameObj = self.driver.find_element_by_xpath(expertNameXpath)
		Name = expertNameObj.text

		starXpath = '//*[@text=\'{}\']/parent::android.widget.LinearLayout\
										/parent::android.widget.LinearLayout\
										/following-sibling::android.widget.FrameLayout\
										/child::androidx.recyclerview.widget.RecyclerView\
										/child::android.widget.LinearLayout\
										/child::android.widget.LinearLayout\
										/child::android.widget.LinearLayout\
										/following-sibling::android.widget.LinearLayout\
										/child::android.widget.LinearLayout\
										/child::android.widget.LinearLayout\
										/following-sibling::android.widget.ImageView'.format(" 快速搜尋 ")

		starObj = self.driver.find_element_by_xpath(starXpath)
		starObj.click()
		if(self.gt.search4Toast("已訂閱", mode=1)):
			actionSuccess = actionSuccess and True
		else:
			actionSuccess = actionSuccess and False

		self.driver.keyevent("4")
		self.ft.findText("找專家")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findText("專家")
		self.ck.clickByString("專家")
		self.ft.findText("我的最愛")
		bookExpertName = self.driver.find_element_by_id(self.apkVersionIdName+"/tv_expert_name").text
		if(Name == bookExpertName):
			actionSuccess = actionSuccess and True
		else:
			actionSuccess = actionSuccess and False

		self.ck.clickByResourceID(self.apkVersionIdName+"/lav_favorite")

		if(self.gt.search4Toast("取消訂閱", mode=1)):
			actionSuccess = actionSuccess and True
		else:
			actionSuccess = actionSuccess and False


		if(actionSuccess):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)

		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
	def quickSearch(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",2)
		self.ft.findText("找專家")
		self.ck.clickByString("找專家")
		self.ft.findText(" 快速搜尋 ")
		self.ck.clickByString(" 快速搜尋 ")
		self.ft.findText("選擇問答類別")
		self.ft.findTextInWholePage("婦科")
		self.ck.clickByString("婦科")
		self.ck.clickByString("下一步")
		self.ft.findText("選擇專家條件")
		self.ck.clickByString("女")
		self.ck.clickByString("完成")
		if(self.ft.findText("張家蓓", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("找專家")
		sleep(5)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")

	
"""
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
"""


























