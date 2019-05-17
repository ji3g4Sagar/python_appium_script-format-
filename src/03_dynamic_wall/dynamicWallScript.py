#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import *
#from logging import Log
from time import sleep
from appium.webdriver import Remote #for keyevent
import random, string


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
		self.apkVersionIdName = apkVersionIdName
		self.hp = homePage(driver, apkVersionIdName)
		self.gt = getToast(driver)

		self.testCountName ="0011" #想辦法改成自動去取得該次測試帳號的使用者名稱
		self.albumName = ""
		self.message = ""
		self.emotionLevel = 0


	def starter(self):
		self.addEmotion()
		#self.checkForEmotion()
		#self.leftMessageInEmotion()
		self.checkForDynamicWall()
		self.createAlbum()
		self.leftMessageInMyselfAlbum()
		self.editAlbumName()
		self.deleteAlbum()
		self.swipeAroundInDynamicWall()
		self.hiFiveCheck()
		self.leftMessageInAlbum()
		self.checkForEmotion()
		self.swipeAndClickSearch()
		self.leftApp()

	def createAlbum(self):

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
		self.albumName = str(random.randint(1,1000))+" testing album"
		self.ec.enter(self.albumName, self.apkVersionIdName + "/albumName")
		self.ck.clickByString("完成")
		self.ft.findTextInWholePage("健康動態")
		self.ck.clickByString(self.albumName)
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
		if(self.ft.findTextInWholePage("在"+self.albumName+"新增了相片", mode=1)):
			actionSuccessfully = True
		if(actionSuccessfully):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		sleep(5)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def leftMessageInMyselfAlbum(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		""""""
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("新增健康燈")
		self.ck.clickByString("相簿")
		self.ft.findTextInWholePage("健康動態")
		self.ck.clickByString(self.albumName)
		self.ft.findTextInWholePage("分享")
		self.ck.clickByResourceID(self.apkVersionIdName+"/leaveMessageCount")
		sleep(5)
		self.message = "Testing message "+str(random.randint(1,1000))
		self.ec.enter(self.message, self.apkVersionIdName + "/albumContentEdText")
		self.ft.findTextInWholePage(self.message)
		self.ck.clickByResourceID(self.apkVersionIdName+"/sendAlbumMsg")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("分享")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("健康動態")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("新增健康燈")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("親友健康")
		self.driver.keyevent("4")
		self.sp.swipeDown(n=3)
		#self.ft.findTextInWholePage("在"+self.albumName+"新增了相片")
		#self.ft.findTextInWholePage("在01新增了相片")
		#xpath = "//android.widget.TextView[@resource-id='"+ self.apkVersionIdName + "/order" + "']/parent::android.widget.FrameLayout/preceding-sibling::android.widget.ImageView"
		#message = '//*[@text=\'{}\']/parent::android.widget.LinearLayout/parent::android.widget.LinearLayout/following-sibing::android.widget.FrameLayout/following-sibing::android.widget.FrameLayout/following-sibing::android.widget.FrameLayout/child::android.widget.LinearLayout/child::android.widget.TextView'.format("在01新增了相片")
		self.ft.findTextInWholePage("在"+self.albumName+"新增了相片")
		targetXpath = '//*[@text=\'{}\']/parent::android.widget.LinearLayout/\
									parent::android.widget.LinearLayout\
									/parent::android.widget.LinearLayout\
									/following-sibling::android.widget.FrameLayout\
									/following-sibling::android.widget.FrameLayout\
									/following-sibling::android.widget.FrameLayout\
									/child::android.widget.LinearLayout\
									/child::android.widget.TextView'.format("在"+self.albumName+"新增了相片")
		target = self.driver.find_element_by_xpath(targetXpath)
		print(target.text)
		target.click()
		self.ck.clickByResourceID(self.apkVersionIdName+"/leaveMessageCount")
		if(self.ft.findTextInWholePage(self.message, mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		sleep(3)
		self.driver.keyevent("4")
		sleep(3)
	
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def editAlbumName(self):

		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("新增健康燈")
		self.ck.clickByString("相簿")
		self.ft.findTextInWholePage("健康動態")
		self.ck.clickByString(self.albumName)
		self.ft.findTextInWholePage("分享")
		self.ck.clickByResourceID(self.apkVersionIdName+"/familyPhotoAlbumHistorySetting")
		self.ck.clickByString("編輯")
		self.ft.findTextInWholePage("設定相簿")
		self.ck.clickByResourceID(self.apkVersionIdName+"/albumName")
		for i in range(len(self.albumName)):
			self.driver.keyevent("67")
		self.albumName = "New "+str(random.randint(1,1000))+" name"
		self.ec.enter(self.albumName, self.apkVersionIdName + "/albumName")
		self.ck.clickByString("完成")
		self.ft.findTextInWholePage("分享")
		if(self.ft.findTextInWholePage(self.albumName, mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("健康動態")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("新增健康燈")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("親友健康")
		self.driver.keyevent("4")
		sleep(5)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def deleteAlbum(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("新增健康燈")
		self.ck.clickByString("相簿")
		self.ft.findTextInWholePage("健康動態")
		self.ck.clickByString(self.albumName)
		self.ft.findTextInWholePage("分享")
		self.ck.clickByResourceID(self.apkVersionIdName+"/familyPhotoAlbumHistorySetting")
		self.ck.clickByString("刪除")
		self.ft.findTextInWholePage("提醒")
		self.ck.clickByString("刪除")
		if(self.gt.search4Toast("刪除完成", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		sleep(5)
		self.driver.keyevent("4")
		sleep(5)
		self.driver.keyevent("4")
		sleep(3)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def checkForDynamicWall(self):
		#用以檢查動態牆是否存在以及當次動態牆上出現的文字
		"""
			1.利用self.hp.goBackToHomePage()返回動態牆
			2.印出動態牆上出現的文字
		"""
		#self.ck.clickByResourceID(self.apkVersionIdName+"/iv_bankLoginRefresh")
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		print("Check for default announcement.....")  
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
	def addEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		sleep(3)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("新增健康燈")
		self.ft.findTextInWholePage("心情")
		self.ck.clickByString("心情")
		self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/emotionCalender")
		self.ck.clickByResourceID(self.apkVersionIdName+"/addEmotion")
		self.ft.findTextInWholePage("選擇您的心情")
		self.emotionLevel = str(random.randint(1,5))
		print(self.emotionLevel)
		self.ck.clickByResourceID(self.apkVersionIdName+"/faceImage"+self.emotionLevel)
		emotionMessage = ''.join(random.choice(string.ascii_letters) for x in range(256))
		self.ec.enter(emotionMessage, self.apkVersionIdName + "/emotionContent")
		sleep(1)
		self.ck.clickByString("發佈")
		self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/emotionCalender")
		self.driver.keyevent("4")
		sleep(3)
		self.driver.keyevent("4")
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")

	def checkForEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.sp.swipeDown(n=2)
		self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/emotionFaceContent")
		self.ck.clickByResourceID("/emotionFaceContent")
		if(self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/emotionContent", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		sleep(2)
		self.driver.keyevent("4")	
		sleep(1)		
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")

	def leftMessageInEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		targetText = self.testCountName + self.emotionLeveltoString()
		self.ft.findTextInWholePage(targetText)
		self.ck.clickByString(targetText)

		sleep(5)

		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")



	def emotionLeveltoString(self):
		if(self.emotionLevel == "1"):
			return "心情很差！"
		elif(self.emotionLevel == "2"):
			return "心情不太好！"
		elif(self.emotionLevel == "3"):
			return "心情普通！"
		elif(self.emotionLevel == "4"):
			return "心情不錯！"
		elif(self.emotionLevel == "5"):
			return "心情棒透了！"
"""
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
"""




























