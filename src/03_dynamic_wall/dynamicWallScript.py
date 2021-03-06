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

		self.testCountName ="" 
		self.albumName = ""
		self.message = ""
		self.emotionLevel = 0


	def starter(self):
		self.checkForDynamicWall()
		self.addEmotion()
		self.leftMessageInEmotion()
		self.editEmotion()
		self.deleteEmotion()
		"""
		self.createAlbum()
		self.leftMessageInMyselfAlbum()
		self.editAlbumName()
		self.deleteAlbum()"""
		self.clickSearch()
		#self.hiFiveCheck()
		
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
	def createAlbum(self):

		actionSuccessfully = False
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		sleep(3)
		self.ft.findTextInWholePage("親友")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("健康燈設定")
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
		self.ft.findTextInWholePage("選擇照片")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/file_thumbnail",1)
		self.ck.clickByString("傳送")
		self.ft.findTextInWholePage("分享")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("健康動態")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("親友")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",0)
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
		self.ft.findTextInWholePage("親友")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("健康燈設定")
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
		self.ft.findTextInWholePage("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("親友")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",0)
		self.sp.swipeDown()
		sleep(4)

		
		self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/homeAlmumLayout5")

		#self.ft.findTextInWholePage("在"+self.albumName+"新增了相片")
		targetXpath = '//*[@text=\'{}\']/parent::android.widget.LinearLayout\
									/parent::android.widget.LinearLayout\
									/parent::android.widget.LinearLayout\
									/following-sibling::android.widget.FrameLayout\
									/following-sibling::android.widget.FrameLayout\
									/following-sibling::android.widget.FrameLayout\
									/child::android.widget.LinearLayout\
									/child::android.widget.ImageView'.format("在"+self.albumName+"新增了相片")
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
		self.ft.findTextInWholePage("親友")
		#self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_name")
		self.ft.findTextInWholePage("健康燈設定")
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
		self.ft.findTextInWholePage("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("親友")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",0)
		sleep(5)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def deleteAlbum(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("健康燈設定")
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
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",0)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
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
	def addEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		sleep(3)
		self.ft.findTextInWholePage("親友")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("健康燈設定")
		self.ft.findTextInWholePage("心情")
		self.ck.clickByString("心情")
		self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/emotionCalender")
		self.ck.clickByResourceID(self.apkVersionIdName+"/addEmotion")
		self.ft.findTextInWholePage("說說您的健康狀況...")
		self.emotionLevel = str(random.randint(1,5))
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
	def leftMessageInEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		sleep(3)
		self.ft.findTextInWholePage("親友")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("健康燈設定")
		self.ft.findTextInWholePage("心情")
		self.ck.clickByString("心情")
		sleep(5)
		self.ck.clickByString("留言")
		self.ft.findTextInWholePage("回覆...")
		self.ck.clickByString("回覆...")
		message = "Testing message "+str(random.randint(1,1000))
		self.ec.enter(message, self.apkVersionIdName + "/emotionContentEdText")
		self.ck.clickByResourceID(self.apkVersionIdName+"/sendEmotionMsg")
		if(self.ft.findTextInWholePage(message, mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		sleep(5)
		self.driver.keyevent("4")
		sleep(5)
		self.driver.keyevent("4")
		sleep(5)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def editEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		sleep(3)
		self.ft.findTextInWholePage("親友")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findText("健康燈設定")
		CountNameObj = self.driver.find_element_by_id(self.apkVersionIdName+"/tv_name")
		self.testCountName = CountNameObj.text
		print(self.testCountName)
		self.ft.findTextInWholePage("心情")
		self.ck.clickByString("心情")
		sleep(5)
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/myEmotionSetting")
		self.ck.clickByResourceID(self.apkVersionIdName+"/myEmotionSetting")
		self.ft.findTextInWholePage("編輯")
		self.ck.clickByString("編輯")
		self.ft.findTextInWholePage("發佈")
		self.emotionLevel = str(random.randint(1,5))
		self.ck.clickByResourceID(self.apkVersionIdName+"/faceImage"+self.emotionLevel)
		self.ck.clickByString("發佈")
		sleep(3)
		emotionString = self.testCountName+self.emotionLeveltoString()
		if(self.ft.findTextInWholePage(emotionString, mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("親友")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",0)

		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def deleteEmotion(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		sleep(3)
		self.ft.findTextInWholePage("親友")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("健康燈設定")
		self.ft.findTextInWholePage("心情")
		self.ck.clickByString("心情")
		sleep(5)
		emotionContent = self.driver.find_element_by_id(self.apkVersionIdName+"/emotionContent").text
		self.ck.clickByResourceID(self.apkVersionIdName+"/myEmotionSetting")

		self.ft.findTextInWholePage("刪除")
		self.ck.clickByString("刪除")
		self.ft.findTextInWholePage("提醒")
		self.ck.clickByString("刪除")
		if(self.ft.findText(emotionContent, mode=1)):
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		else:
			print("[PASS]-"+sys._getframe().f_code.co_name)	
		sleep(5)
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("親友")

		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")	
	def emotionLeveltoString(self):
		if(self.emotionLevel == "1"):
			return "狀態很差！"
		elif(self.emotionLevel == "2"):
			return "狀態不太好！"
		elif(self.emotionLevel == "3"):
			return "狀態普通！"
		elif(self.emotionLevel == "4"):
			return "狀態不錯！"
		elif(self.emotionLevel == "5"):
			return "狀態棒透了！"
	def clickSearch(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.sp.swipeLeft()
		self.sp.swipeLeft()
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_homeHealthKeywords")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/iv_homeResultSearch")
		self.ck.clickByResourceID(self.apkVersionIdName+"/ll_homeResultArticleItem")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_homeRecommendType")
		self.ck.clickByString("查看出處")
		self.ft.findSpecificItemByResourceID("android:id/title")
		self.driver.keyevent("4")
		sleep(1)
		self.driver.keyevent("4")
		self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/youtube_playerView") #找尋有影片的文章
		self.ck.clickByResourceID(self.apkVersionIdName+"/youtube_playerView")
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




























