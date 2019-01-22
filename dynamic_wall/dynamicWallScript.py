#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor, findSpecificText, getXYLocation
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
		self.xy = getXYLocation(driver)
		self.testCountName ="test999"
		self.apkVersionIdName = apkVersionIdName
	def goBackToDynamicWall(self):
		# 呼叫於每次操作前，返回動態牆畫面使用
		"""
			1.檢查畫面最下方的home tab是否存在
			2.利用tap進到動態牆頁面
			3.檢查畫面中是否出現Notification元件,用以確認是否返回動態牆最上方
		"""
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/home_tab_icon")
		target = self.driver.find_elements_by_id(self.apkVersionIdName+ "/home_tab_icon")
		self.ck.tap(target[0])
		findNotification = False
		while (findNotification == False):
			if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/home_notification", time=2, freuency=1)):
				findNotification = True
			else:
				self.sp.swipeDown()
		print("Successuflly go back to dynaamic wall!!\n")
	def checkForDynamicWall(self):
		#用以檢查動態牆是否存在以及當次動態牆上出現的文字
		"""
			1.利用self.goBackToDynamicWall()返回動態牆
			2.印出動態牆上出現的文字
		"""
		self.goBackToDynamicWall()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		print("Check for default announcement.....")
		defaultKeyWord = self.driver.find_element_by_id(self.apkVersionIdName + "/tv_homeHealthKeywords").text
		self.ft.findText(defaultKeyWord)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def swipeAroundInDynamicWall(self):
		#檢測動態牆的滑動是否正常
		self.goBackToDynamicWall()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.sp.swipeUp()
		self.sp.swipeDown()
		self.sp.swipeUp()
		self.sp.swipeDown()
		self.sp.swipLeft()
		self.sp.swipRight()
		self.sp.swipeUp(n=2)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def hiFiveCheck(self):
		#檢測在動態牆上是否有「為您擊掌」的互動訊息
		"""
			1.利用顯式(explicit)等待,尋找擊掌的sourceID(/likeTime)出現
				->findHiFive == True: 利用self.ft確認「為您擊掌」文字是否存在
				->findHiFive == False: 下向滑動繼續尋找
		"""
		self.goBackToDynamicWall()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		findHiFive = False
		while(findHiFive != True):
			if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/likeTime", time=2, freuency=0.5)):
				print(type(self))
				self.ft.findText("為您擊掌")
				findHiFive = True
			else:
				print("Keep serarching for the element %s !!!" % (self.apkVersionIdName+"/likeTime"))
				self.sp.swipeUp(n=2)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")			
		sleep(5)
	def deleteFriendOfHiFive(self):
		#找尋有擊掌互動的好友並將該位好友刪除
		"""
			1.self.hiFiveCheck()找尋「為您擊掌」訊息
			2.紀錄該名朋友的名字(nameOfFriendGoinToDelete),並點進好友頁面將該名好友刪除
			3.呼叫self.ft在好友頁面找尋該名好友是否還存在
			4.返回動態牆,刷新動態牆訊息
		"""
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
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
		#檢測動態牆上是否有相簿訊息
		"""
			1.利用顯式等待,找尋相簿的sourceID(viewPageImageView)出現
				->findAlbum == True: 結束while loop
				->findAlbum == False: 向下滑動頁面繼續尋找
			2.進到相簿,並印出相簿名稱
		"""
		self.goBackToDynamicWall()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		findAlbum = False
		while(findAlbum != True):
			if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/viewPagerImageView", time=2, freuency=0.5)):
				findAlbum = True
			else:
				print("Keep serarching for the element %s !!!" % (self.apkVersionIdName+"/viewPagerImageView"))
				self.sp.swipeUp()		
		self.ck.clickByResourceID(self.apkVersionIdName + "/viewPagerImageView")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/titleNickName")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def deleteFriendOfAlbum(self):
		#找尋動態牆上是否有相簿動態消息,並將發布相簿的好友刪除
		"""
			1.利用self.checkForAlbum()檢測是否有相簿出現
			2.紀錄(nameOfFriendGoingToDelete)並點擊該名好友進入好友頁面並將之刪除
			3.在好友頁面找尋該名好友是否存在
			4.返回動態牆,刷新動態牆訊息
		"""
		self.goBackToDynamicWall
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.checkForAlbum()
		nameOfFriendGoingToDelete = self.driver.find_element_by_id(self.apkVersionIdName + "/homeAlbumName").text
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
	def leftMessageInAlbum(self):
		#在動態牆中出現的相簿動態下留言測試
		"""
			1.利用self.checkForAlbum()找尋是否有相簿動態
			2.進到相簿中留言,並利用self.ft確認留言是否成功
			3.返回動態牆
		"""
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.checkForAlbum()
		self.ck.clickByResourceID(self.apkVersionIdName + "/viewPagerImageView")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/titleNickName")
		self.ck.clickByResourceID(self.apkVersionIdName + "/messageBoardTitleLayout")
		message = str(random.randint(1,1000))+" message!!!"
		self.ec.enter(message, self.apkVersionIdName + "/albumContentEdText")
		self.ck.clickByResourceID(self.apkVersionIdName+"/sendAlbumMsg")
		if( self.ft.findText(message, mode=1)==False):
			self.leftMessageInAlbum()
		self.driver.keyevent("4")
		self.driver.keyevent("4")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(3)

	def checkForEmotion(self):
		self.goBackToDynamicWall()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		findEmotion = False
		emotionClickTarget =self.driver
		nameOfFriendGoingToDelete=""
		while(findEmotion != True):
			if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/emotionFacePhoto", time=2, freuency=1)):
				targets = self.driver.find_elements_by_id(self.apkVersionIdName+"/emotionNickName")
				for t in targets:
					print(t.text)
					if (t.text==self.testCountName):
						continue
					else:
						nameOfFriendGoingToDelete=t.text
						t.click()
						#emotionClickTarget = t
						findEmotion = True
						break
			else:
				print("Keep serarching for the element %s !!!" % (self.apkVersionIdName+"/emotionFacePhoto"))
			if(findEmotion==False):
				self.sp.swipeUp()
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tvDelete")
		self.ck.clickByString("刪除好友")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/alertTitle")
		self.ck.clickByString("刪除")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/addFriend")
		if(self.ft.findText(nameOfFriendGoingToDelete, mode=1) == False):
			print("Successuflly delete friend!! %s" % nameOfFriendGoingToDelete)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")		
		sleep(3)
	


"""
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
"""
