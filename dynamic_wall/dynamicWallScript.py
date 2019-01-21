#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor, findSpecificText
from time import sleep
from appium.webdriver import Remote #for keyevent
import random

class script():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.ft = findSpecificText(driver)
		self.apkVersionIdName = apkVersionIdName
	def checkForDynamicWall(self):
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/fl_homeHealthVideoTitle")
		print("Check for default announcement.....")
		defaultKeyWord = self.driver.find_element_by_id(self.apkVersionIdName + "/tv_homeHealthKeywords").text
		self.ft.findText(defaultKeyWord)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def swipeAroundInDynamicWall(self):
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/fl_homeHealthVideoTitle")
		self.sp.swipeUp(n=2)
		self.sp.swipeDown(n=4)
		self.sp.swipeUp(n=2)
		self.sp.swipeDown(n=4)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def hiFiveCheck(self):
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/home_tab_icon")
		findHiFive = False
		while(findHiFive != True):
			if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/likeTime", time=2, freuency=0.5)):
				print(type(self))
				self.ft.findText("為您擊掌")
				findHiFive = True
			else:
				print("Keep serarching for the element %s !!!" % (self.apkVersionIdName+"/likeTime"))
				self.sp.swipeUp()
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")			
		sleep(5)
	def deleteFriendOfHiFive(self):
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/fl_homeHealthVideoTitle")
		self.hiFiveCheck()
		targetXpath = '//*[@text=\'為您擊掌\']/parent::android.widget.LinearLayout/preceding-sibling::android.widget.LinearLayout'
		target = self.driver.find_element_by_xpath(targetXpath)
		T = target.find_element_by_id(self.apkVersionIdName + "/likeNickName")
		nameOfFriendGoingToDelete = T.text
		T.click()
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tvDelete")
		self.ck.clickByString("刪除好友")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/alertTitle")
		self.ck.clickByString("刪除")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/addFriend")
		if(self.ft.findText(nameOfFriendGoingToDelete, mode=1) == False):
			print("Successuflly delete friend!! %s" % nameOfFriendGoingToDelete)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 0)
		self.sp.swipeDown(n=3, yStart=0.1)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")		
		sleep(5)
	def checkForAlbum(self):
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/home_tab_icon")
		findAlbum = False
		while(findAlbum != True):
			if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/viewPagerImageView", time=2, freuency=0.5)):
				findAlbum = True
			else:
				print("Keep serarching for the element %s !!!" % (self.apkVersionIdName+"/likeTime"))
				self.sp.swipeUp()		
		self.ck.clickByResourceID(self.apkVersionIdName + "/viewPagerImageView")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/titleNickName")
		self.driver.keyevent("4")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def deleteFriendOfAlbum(self):
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")	
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 0)
		self.checkForAlbum()
		nameOfFriendGoingToDelete = self.driver.find_element_by_id(self.apkVersionIdName + "/homeAlbumName").text
		self.ck.clickByResourceID(self.apkVersionIdName + "/homeAlbumName")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tvDelete")
		self.ck.clickByString("刪除好友")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/alertTitle")
		self.ck.clickByString("刪除")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/addFriend")
		if(self.ft.findText(nameOfFriendGoingToDelete, mode=1) == False):
			print("Successuflly delete friend!! %s" % nameOfFriendGoingToDelete)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 0)
		self.sp.swipeDown(n=3, yStart=0.1)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)




	

		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
	