#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor, findSpecificText, getXYLocation, homePage
#from logging import Log
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
		self.ft = findSpecificText(driver)
		self.testCountName ="test999" #想辦法改成自動去取得該次測試帳號的使用者名稱
		self.apkVersionIdName = apkVersionIdName
		self.hp = homePage(driver, apkVersionIdName)

	def starter(self):
		self.checkForDynamicWall()
		self.swipeAroundInDynamicWall()
		self.hiFiveCheck()
		self.leftMessageInAlbum()
		self.checkForEmotion()
		self.swipeAndClickSearch()
		self.leftApp()
	def checkForDynamicWall(self):
		#用以檢查動態牆是否存在以及當次動態牆上出現的文字
		"""
			1.利用self.hp.goBackToHomePage()返回動態牆
			2.印出動態牆上出現的文字
		"""
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_bankLoginRefresh")
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		print("Check for default announcement.....")
		defaultKeyWord = self.driver.find_element_by_id(self.apkVersionIdName + "/tv_homeHealthKeywords").text
		self.ft.findText(defaultKeyWord)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
		sleep(5)
	def swipeAroundInDynamicWall(self):
		#檢測動態牆的滑動是否正常
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.sp.swipeUp()
		self.sp.swipeDown()
		self.sp.swipeUp()
		self.sp.swipeDown()
		self.sp.swipeLeft()
		self.sp.swipeRight()
		self.sp.swipeUp(n=2)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
		sleep(5)
	def hiFiveCheck(self):
		#檢測在動態牆上是否有「為您擊掌」的互動訊息
		"""
			1.利用顯式(explicit)等待,尋找擊掌的sourceID(/likeTime)出現
				->findHiFive == True: 利用self.ft確認「為您擊掌」文字是否存在
				->findHiFive == False: 下向滑動繼續尋找
		"""
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		findHiFive = False
		while(findHiFive != True):
			#if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/likeTime", time=2, freuency=0.5)):
			if(self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/likeTime")):
				print(type(self))
				self.ft.findText("為您擊掌")
				findHiFive = True
			else:
				print("Keep serarching for the element %s !!!" % (self.apkVersionIdName+"/likeTime"))
				self.sp.swipeUp(n=2)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")			
		sleep(5)
	def deleteFriendOfHiFive(self):
		#找尋有擊掌互動的好友並將該位好友刪除
		"""
			1.self.hiFiveCheck()找尋「為您擊掌」訊息
			2.紀錄該名朋友的名字(nameOfFriendGoinToDelete),並點進好友頁面將該名好友刪除
			3.呼叫self.ft在好友頁面找尋該名好友是否還存在
			4.返回動態牆,刷新動態牆訊息
		"""
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.hiFiveCheck()
		targetXpath = '//*[@text=\'為您擊掌\']/parent::android.widget.LinearLayout/preceding-sibling::android.widget.LinearLayout'
		target = self.driver.find_element_by_xpath(targetXpath)
		T = target.find_element_by_id(self.apkVersionIdName + "/likeNickName")
		nameOfFriendGoingToDelete = T.text
		T.click()
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/tvDelete")
		self.ck.clickByString("刪除好友")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/alertTitle")
		self.ck.clickByString("刪除")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/addFriend")
		if(self.ft.findText(nameOfFriendGoingToDelete, mode=1) == False):
			print("Successuflly delete friend!! %s" % nameOfFriendGoingToDelete)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 0)
		self.sp.swipeDown(n=3, yStart=0.1)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")		
		sleep(5)
	def checkForAlbum(self):
		#檢測動態牆上是否有相簿訊息
		"""
			1.利用顯式等待,找尋相簿的sourceID(viewPageImageView)出現
				->findAlbum == True: 結束while loop
				->findAlbum == False: 向下滑動頁面繼續尋找
			2.進到相簿,並印出相簿名稱
		"""
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		findAlbum = False
		while(findAlbum != True):
			#if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/viewPagerImageView", time=2, freuency=0.5)):
			if(self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/viewPagerImageView")):
				findAlbum = True
			else:
				print("Keep serarching for the element %s !!!" % (self.apkVersionIdName+"/viewPagerImageView"))
				self.sp.swipeUp()		
		self.ck.clickByResourceID(self.apkVersionIdName + "/viewPagerImageView")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/titleNickName")
		self.driver.keyevent("4")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
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
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.checkForAlbum()
		nameOfFriendGoingToDelete = self.driver.find_element_by_id(self.apkVersionIdName + "/homeAlbumName").text
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/tvDelete")
		self.ck.clickByString("刪除好友")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/alertTitle")
		self.ck.clickByString("刪除")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/addFriend")
		if(self.ft.findText(nameOfFriendGoingToDelete, mode=1) == False):
			print("Successuflly delete friend!! %s" % nameOfFriendGoingToDelete)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 0)
		self.sp.swipeDown(n=3, yStart=0.1)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
		sleep(5)
	def leftMessageInAlbum(self):
		#在動態牆中出現的相簿動態下留言測試
		"""
			1.利用self.checkForAlbum()找尋是否有相簿動態
			2.進到相簿中留言,並利用self.ft確認留言是否成功
			3.返回動態牆
		"""
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.checkForAlbum()
		self.ck.clickByResourceID(self.apkVersionIdName + "/viewPagerImageView")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/messageBoardTitleLayout")
		self.ck.clickByResourceID(self.apkVersionIdName + "/messageBoardTitleLayout")
		message = str(random.randint(1,1000))+" test message!!!"
		self.ec.enter(message, self.apkVersionIdName + "/albumContentEdText")
		self.ck.clickByResourceID(self.apkVersionIdName+"/sendAlbumMsg")
		self.ft.findTextInWholePage(message)
		self.driver.keyevent("4")
		self.driver.keyevent("4")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
		sleep(3)
	def checkForEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		findEmotion = False
		emotionClickTarget =self.driver
		nameOfFriendGoingToDelete=""
		while(findEmotion != True):
			#if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/emotionFacePhoto", time=2, freuency=1)):
			if(self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/emotionFacePhoto")):
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
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")	
		self.driver.keyevent("4")	
		sleep(3)
	def deleteFriendOfEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.checkForEmotion()
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_ShareMainSetting")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/tvDelete")
		self.ck.clickByString("刪除好友")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/alertTitle")
		self.ck.clickByString("刪除")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/addFriend")
		if(self.ft.findText(nameOfFriendGoingToDelete, mode=1) == False):
			print("Successuflly delete friend!! %s" % nameOfFriendGoingToDelete)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")		
	def leftMessageInEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.checkForEmotion()
		self.driver.keyevent("4")
		self.ck.clickByResourceID(self.apkVersionIdName+"/emotionLayout4")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/emotionContentEdText")
		message = str(random.randint(1,1000)) + " message!!!"
		self.ec.enter(message, self.apkVersionIdName+"/emotionContentEdText")
		self.ck.clickByResourceID(self.apkVersionIdName+"/sendEmotionMsg")
		if( self.ft.findText(message, mode=1)==False):
			self.leftMessageInAlbum()
		self.driver.keyevent("4")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
		sleep(3)	
	def leftApp(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("離開")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")		
	def swipeAndClickSearch(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.sp.swipeLeft()
		self.sp.swipeLeft()
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_homeHealthKeywords")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/iv_homeResultSearch")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_homeResultSearch")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_homeResultSearch")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_homeResultSearch")
		self.ck.clickByResourceID(self.apkVersionIdName+"/ll_homeResultArticleItem")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_homeRecommendType")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_homeRecommendWeb")#點擊文章出處
		self.ft.findSpecificItemByResourceID("android:id/title")
		self.driver.keyevent("4")
		sleep(1)
		self.driver.keyevent("4")
		self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/youtube_playerView") #找尋有影片的文章
		self.ck.clickByResourceID(self.apkVersionIdName+"/youtube_playerView")
		self.ft.findTextInWholePage("查看出處")
		self.ck.clickByString("查看出處")
		#self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_homeRecommendWeb")
		#self.ck.clickByResourceID(self.apkVersionIdName+"/tv_homeRecommendWeb")#點擊影片來源「查看出處」
		sleep(3)
		self.ft.findTextInWholePage("訂閱")
		sleep(2)
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("查看出處")
		#self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_homeRecommendWeb")
		self.driver.keyevent("4")
		self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/iv_homeResultSearch")
		#self.ck.clickByResourceID(self.apkVersionIdName+"/home_recommendBack")
		self.driver.keyevent("4")
		#self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/iv_homeResultSearch")
		#self.ck.clickByResourceID(self.apkVersionIdName+"/iv_homeResultSearch")
		self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/home_tab_icon")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
		sleep(5)
	def todayMession(self):  # 3/24列入無法測試項目，因為需要人工每日由其他帳號操錯，今日進度才有項目出現
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickByResourceID(self.apkVersionIdName+"/linFollowedMission")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_toolbar")
		self.sp.swipeDown()
		self.sp.swipeUp()
		self.ck.clickByResourceID(self.apkVersionIdName+"/cb_mission")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tvMissionMemo")#等待任務頁面下方的memo出現
		self.driver.keyevent("4")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/deco_history_progress")
		self.ck.clickByResourceID(self.apkVersionIdName+"/deco_history_progress")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/fra_scroll_body")
		self.driver.keyevent("4")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_title")
		self.driver.keyevent("4")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")		



"""
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
"""




























