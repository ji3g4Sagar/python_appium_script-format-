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
		self.addNewAlbum()
		self.checkForDynamicWall()
		self.swipeAroundInDynamicWall()
		self.hiFiveCheck()
		self.leftMessageInAlbum()
		self.checkForEmotion()
		self.swipeAndClickSearch()
		self.leftApp()

	def addNewAlbum(self):
		actionSuccessfully = False
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		sleep(3)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("新增健康燈")
		self.ck.clickByString("相簿")
		self.ft.findTextInWholePage("健康動態")
		self.ck.clickByString("＋新增相簿")
		self.ft.findTextInWholePage("設定相簿")
		albumName = str(random.randint(1,1000))+" testing album"
		self.ec.enter(albumName, self.apkVersionIdName + "/albumName")
		self.ck.clickByString("完成")
		self.ft.findTextInWholePage("健康動態")
		self.ck.clickByString(albumName)
		self.ft.findTextInWholePage("分享")
		self.ck.clickByResourceID(self.apkVersionIdName+"/familyPhotoAlbumHistoryAdd")
		self.ft.findTextInWholePage("相簿")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/order",0)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/order",1)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/order",2)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/order",3)
		self.ck.clickByString("確認")
		self.ft.findTextInWholePage("分享")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("健康動態")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("新增健康燈")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("親友健康")
		self.driver.keyevent("4")
		self.sp.swipeDown(n=2)
		if(self.ft.findTextInWholePage("在"+albumName+"新增了相片", mode=1)):
			actionSuccessfully = True
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("新增健康燈")
		self.ck.clickByString("相簿")
		self.ft.findTextInWholePage("健康動態")
		self.ck.clickByString(albumName)
		self.ft.findTextInWholePage("分享")
		self.ck.clickByResourceID(self.apkVersionIdName+"/familyPhotoAlbumHistorySetting")
		self.ck.clickByString("刪除")
		self.ft.findTextInWholePage("提醒")
		self.ck.clickByString("刪除")
		if(actionSuccessfully):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		sleep(5)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")


	def checkForDynamicWall(self):
		#用以檢查動態牆是否存在以及當次動態牆上出現的文字
		"""
			1.利用self.hp.goBackToHomePage()返回動態牆
			2.印出動態牆上出現的文字
		"""
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_bankLoginRefresh")
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		print("Check for default announcement.....")  #待修
		defaultKeyWord = self.driver.find_element_by_id(self.apkVersionIdName + "/tv_homeHealthKeywords").text
		if(self.ft.findText(defaultKeyWord, mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
		sleep(5)
	def swipeAroundInDynamicWall(self):
		#檢測動態牆的滑動是否正常
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.sp.swipeUp()
		self.sp.swipeDown()
		self.sp.swipeUp()
		self.sp.swipeDown()
		self.sp.swipeLeft()
		self.sp.swipeRight()
		self.sp.swipeUp(n=2)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
		sleep(5)
	def hiFiveCheck(self):
		#檢測在動態牆上是否有「為您擊掌」的互動訊息
		"""
			1.利用顯式(explicit)等待,尋找擊掌的sourceID(/likeTime)出現
				->findHiFive == True: 利用self.ft確認「為您擊掌」文字是否存在
				->findHiFive == False: 下向滑動繼續尋找
		"""
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		findHiFive = False
		while(findHiFive != True):
			#if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/likeTime", time=2, freuency=0.5)):
			if(self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/likeTime")):
				print(type(self))
				if(self.ft.findText("為您擊掌", mode=1)):
					findHiFive = True		
					print("[PASS]-"+sys._getframe().f_code.co_name)
				else:
					print("[FAIL]-"+sys._getframe().f_code.co_name)
			else:
				print("Keep serarching for the element %s !!!" % (self.apkVersionIdName+"/likeTime"))
				self.sp.swipeUp(n=2)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")			
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
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		findAlbum = False
		while(findAlbum != True):
			#if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/viewPagerImageView", time=2, freuency=0.5)):
			if(self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/viewPagerImageView")):
				findAlbum = True
				print("[PASS]-"+sys._getframe().f_code.co_name)
			else:
				print("Keep serarching for the element %s !!!" % (self.apkVersionIdName+"/viewPagerImageView"))
				self.sp.swipeUp()		
		self.ck.clickByResourceID(self.apkVersionIdName + "/viewPagerImageView")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/titleNickName")
		self.driver.keyevent("4")
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
		sleep(5)
	def leftMessageInAlbum(self):
		#在動態牆中出現的相簿動態下留言測試
		"""
			1.利用self.checkForAlbum()找尋是否有相簿動態
			2.進到相簿中留言,並利用self.ft確認留言是否成功
			3.返回動態牆
		"""
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.checkForAlbum()
		self.ck.clickByResourceID(self.apkVersionIdName + "/viewPagerImageView")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/messageBoardTitleLayout")
		self.ck.clickByResourceID(self.apkVersionIdName + "/messageBoardTitleLayout")
		message = str(random.randint(1,1000))+" test message!!!"
		self.ec.enter(message, self.apkVersionIdName + "/albumContentEdText")
		self.ck.clickByResourceID(self.apkVersionIdName+"/sendAlbumMsg")
		if(self.ft.findTextInWholePage(message, mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.driver.keyevent("4")
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
		sleep(3)
	def checkForEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		findEmotion = False
		emotionClickTarget = self.driver
		while(findEmotion != True):
			if(self.ft.findSpecificItemByResourceID(self.apkVersionIdName + "/emotionFacePhoto")):
				targets = self.driver.find_elements_by_id(self.apkVersionIdName+"/emotionNickName")
				for t in targets:
					print(t.text)
					if (t.text != self.testCountName):
						continue
					else:
						print("[PASS]-"+sys._getframe().f_code.co_name)
						t.click()
						findEmotion = True
						break
			else:
				print("Keep serarching for the element %s !!!" % (self.apkVersionIdName+"/emotionFacePhoto"))
			if(findEmotion==False):
				self.sp.swipeUp()
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")	
		self.driver.keyevent("4")	
		sleep(3)		
	def leftMessageInEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.checkForEmotion()
		self.driver.keyevent("4")
		self.ck.clickByResourceID(self.apkVersionIdName+"/emotionLayout4")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/emotionContentEdText")
		message = str(random.randint(1,1000)) + " message!!!"
		self.ec.enter(message, self.apkVersionIdName+"/emotionContentEdText")
		self.ck.clickByResourceID(self.apkVersionIdName+"/sendEmotionMsg")
		if( self.ft.findText(message, mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)

		self.driver.keyevent("4")
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
		sleep(3)	
	def leftApp(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("離開")
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")		
	def swipeAndClickSearch(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
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
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
		sleep(5)

"""
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
"""




























