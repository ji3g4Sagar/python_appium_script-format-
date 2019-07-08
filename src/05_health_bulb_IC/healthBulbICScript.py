#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import *
#from logging import Log
from time import sleep
import time
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
		self.apkVersionIdName = apkVersionIdName
		self.hp = homePage(driver, apkVersionIdName)
		self.gt = getToast(driver)


	def starter(self):
		""""""
		self.addICData()
		self.addICNodata()
		self.icLevels()
		
		self.addReVisit()
		self.checkReVisitData()
		self.addReVisitEmpty()


	def addICData(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("IC")
		self.ck.clickByString("IC")
		self.ft.findText("IC_TICA")
		self.ft.findText("疼痛程度")
		painBarXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
										/child::android.view.View\
										/child::android.view.View'.format("疼痛程度")

		painBarObj = self.driver.find_element_by_xpath(painBarXpath)
		painBarX = painBarObj.location['x']
		painBarY = painBarObj.location['y']
		self.driver.tap([(painBarX+float(380), painBarY)])
		self.ft.findText("尿急程度")
		urgencyBarXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
											/child::android.view.View\
											/child::android.view.View'.format("尿急程度")
		urgencyBarObj = self.driver.find_element_by_xpath(urgencyBarXpath)
		urgencyBarX = urgencyBarObj.location['x']
		urgencyBarY = urgencyBarObj.location['y']
		self.driver.tap([(urgencyBarX+float(380), urgencyBarY)])
		self.ft.findTextInWholePage("查看月曆")
		urinaryVolume = str(random.randint(1,70))
		self.ft.findText("紀錄您現在的排尿量(單位:c.c.)")
		urinaryVolumeXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
												  /child::android.widget.EditText'.format("紀錄您現在的排尿量(單位:c.c.)")
		urinaryVolumeFiled = self.driver.find_element_by_xpath(urinaryVolumeXpath)
		urinaryVolumeFiled.click()
		urinaryVolumeFiled.set_text(urinaryVolume)
		self.ck.clickByString("上傳")
		self.gt.search4Toast("新增成功")
		sleep(5)
		if(self.ft.findText(urinaryVolume+"c.c", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		sleep(5)
		self.driver.keyevent("4")
		self.ft.findText("IC_TICA")
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		sleep(3)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def addICNodata(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("IC")
		self.ck.clickByString("IC")
		self.ft.findText("IC_TICA")
		self.ft.findText("疼痛程度")
		self.ck.clickByString("上傳")
		if(self.gt.search4Toast("疼痛、尿急程度為必填", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		sleep(3)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def icLevels(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("IC")
		self.ck.clickByString("IC")
		actionSuccess = True
		for i in range(5):
			icLevelNum = random.randint(0,11)
			self.ft.findText("IC_TICA")
			painBarX, painBarY, urgencyBarX, urgencyBarY, levelText, urinaryVolume = self._icLevelToLocation(icLevelNum)
			print(painBarX, painBarY, urgencyBarX, urgencyBarY, levelText, urinaryVolume)
			self.ft.findText("疼痛程度")
			sleep(2)
			self.driver.tap([(painBarX, painBarY)])
			sleep(2)
			self.driver.tap([(urgencyBarX, urgencyBarY)])
			sleep(2)
			self.ft.findTextInWholePage("查看月曆")
			urinaryVolumeXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
												  /child::android.widget.EditText'.format("紀錄您現在的排尿量(單位:c.c.)")
			urinaryVolumeFiled = self.driver.find_element_by_xpath(urinaryVolumeXpath)
			urinaryVolumeFiled.click()
			sleep(5)
			urinaryVolumeFiled.set_text(urinaryVolume)
			sleep(5)
			self.ck.clickByString("上傳")
			sleep(10)
			self.ft.findText("日常紀錄")
			self.ft.findText(urinaryVolume+"c.c")
			painXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/child::android.view.View\
											/following-sibling::android.view.View\
											/following-sibling::android.view.View\
											/following-sibling::android.view.View'.format(urinaryVolume+"c.c")
			urgencyXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/child::android.view.View\
											/following-sibling::android.view.View\
											/following-sibling::android.view.View\
											/following-sibling::android.view.View\
											/following-sibling::android.view.View\
											/following-sibling::android.view.View'.format(urinaryVolume+"c.c")
			painTextObj = self.driver.find_element_by_xpath(painXpath)
			urgencyTextObj = self.driver.find_element_by_xpath(urgencyXpath)
			if(painTextObj.text == levelText and urgencyTextObj.text == levelText):
				print("find")
				actionSuccess = True and actionSuccess
			else:
				print("not found")
				actionSuccess = False and actionSuccess
			sleep(4)
			self.driver.keyevent("4")

		self.ft.findText("IC_TICA")
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		sleep(3)	

		if(actionSuccess):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)

		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def _icLevelToLocation(self, icLevel):
		urinaryVolume = str(random.randint(1,9999)) #利用尿量作為唯一代碼，找尋輸入的等級
		if(icLevel == 0):
			return 229, 788, 229, 1287, "正常", urinaryVolume
		elif(icLevel == 1):
			return 298, 788, 298, 1287, "正常", urinaryVolume
		elif(icLevel == 2):
			return 367, 788, 367, 1287, "輕微", urinaryVolume
		elif(icLevel == 3):
			return 436, 788, 436, 1287, "輕微", urinaryVolume
		elif(icLevel == 4):
			return 505, 788, 505, 1287, "中度", urinaryVolume
		elif(icLevel == 5):
			return 574, 788, 574, 1287, "中度", urinaryVolume
		elif(icLevel == 6):
			return 643, 788, 643, 1287, "高度", urinaryVolume
		elif(icLevel == 7):
			return 712, 788, 712, 1287, "高度", urinaryVolume
		elif(icLevel == 8):
			return 781, 788, 781, 1287, "劇烈", urinaryVolume
		elif(icLevel == 9):
			return 850, 788, 850, 1287, "劇烈", urinaryVolume
		elif(icLevel == 10):
			return 919, 788, 919, 1287, "劇烈", urinaryVolume
	def addReVisit(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 1)
		self.ft.findText("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic", 0)
		self.ft.findTextInWholePage("回診")
		self.ck.clickByString("回診")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/iv_addReVisitData")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_addReVisitData")  #點選介面上的「+」
		self.ft.findText("新增回診單照片")
		self.ck.clickByString("新增回診單照片")
		self.ft.findText("選擇照片")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/file_thumbnail", 1)
		self.ck.clickByString("傳送")
		self.ft.findText("編輯圖片")
		revisitTimeXpath = '//*[@text=\'{}\']/following-sibling::android.view.View'.format("選擇回診時間")
		revisitTimeObj = self.driver.find_element_by_xpath(revisitTimeXpath)
		revisitTimeObj.click() #確認回診時間
		self.ft.findText("確定")
		self.ck.clickByString("確定")
		self.ft.findText("確定")
		self.ck.clickByString("確定")
		revisitName = "No." + str(random.randint(1,999))
		revisitNameXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
											 /child::android.widget.EditText'.format("提醒時間")
		revisitNameObj = self.driver.find_element_by_xpath(revisitNameXpath)
		revisitNameObj.click()
		revisitNameObj.set_text(revisitName)
		self.ft.findText(revisitName)
		self.ck.clickByString("完成")
		timeStampXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
										   /child::android.view.View\
										   /following-sibling::android.view.View'.format("今天")
		nameXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
									  /child::android.view.View\
									  /parent::android.view.View\
									  /following-sibling::android.view.View\
									  /child::android.view.View'.format("今天")   #找不到原因，會選到錯的元件，已修正。
		timeStampObj = self.driver.find_element_by_xpath(timeStampXpath)
		nameObj = self.driver.find_element_by_xpath(nameXpath)
		currentTimeStamp = time.strftime("%Y/%m/%d %H:", time.localtime())
		print(currentTimeStamp)
		print(timeStampObj.text)
		print(revisitName)
		print(nameObj.text)
		if(currentTimeStamp in timeStampObj.text and revisitName == nameObj.text):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)


		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findText("親友健康")
		sleep(5)	
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def checkReVisitData(self):
		self.hp.goBackToHomePage()
		actionSuccess = True
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 1)
		self.ft.findText("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic", 0)
		self.ft.findTextInWholePage("回診")
		self.ck.clickByString("回診")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/iv_addReVisitData")
		self.ft.findText("今天")
		checkBoxXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
										   /child::android.view.View'.format("今天")
		checkBoxObj = self.driver.find_element_by_xpath(checkBoxXpath)
		checkBoxObj.click()
		if(self.ft.findText("完成", mode=1)):
			actionSuccess = True and actionSuccess
		else:
			actionSuccess = False and actionSuccess
		checkBoxObj.click()
		if(self.ft.findText("今天", mode=1)):
			actionSuccess = True and actionSuccess
		else:
			actionSuccess = False and actionSuccess

		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findText("親友健康")
		if(actionSuccess):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		sleep(5)	

		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def addReVisitEmpty(self):
		self.hp.goBackToHomePage()
		actionSuccess = True
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 1)
		self.ft.findText("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic", 0)
		self.ft.findTextInWholePage("回診")
		self.ck.clickByString("回診")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/iv_addReVisitData")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_addReVisitData")  #點選介面上的「+」
		self.ft.findText("新增回診單照片")
		self.ck.clickByString("完成")
		if(self.gt.search4Toast("必填項目不可為空", mode=1)):
			actionSuccess = True and actionSuccess
		else:
			actionSuccess = False and actionSuccess

		# --------------新增回診時間，重新上傳------------------
		revisitTimeXpath = '//*[@text=\'{}\']/following-sibling::android.view.View'.format("選擇回診時間")
		revisitTimeObj = self.driver.find_element_by_xpath(revisitTimeXpath)
		revisitTimeObj.click() #確認回診時間
		self.ft.findText("確定")
		self.ck.clickByString("確定")
		self.ft.findText("確定")
		self.ck.clickByString("確定")
		self.ck.clickByString("完成")		
		if(self.gt.search4Toast("必填項目不可為空", mode=1)):
			actionSuccess = True and actionSuccess
		else:
			actionSuccess = False and actionSuccess

		# --------------返回上頁，重新新增回診名稱，預期跳出toast顯示「必填項目不可為空」-----------------
		self.ck.clickByString("取消")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/iv_addReVisitData")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_addReVisitData")  #點選介面上的「+」
		self.ft.findText("新增回診單照片")

		revisitName = "No." + str(random.randint(1,999))
		revisitNameXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
											 /child::android.widget.EditText'.format("提醒時間")
		revisitNameObj = self.driver.find_element_by_xpath(revisitNameXpath)
		revisitNameObj.click()
		revisitNameObj.set_text(revisitName)
		self.ft.findText(revisitName)
		self.ck.clickByString("完成")
		if(self.gt.search4Toast("必填項目不可為空", mode=1)):
			actionSuccess = True and actionSuccess
		else:
			actionSuccess = False and actionSuccess

		#--------------------最後測試沒有照片，預期可以成功上傳-----------------------
		revisitTimeXpath = '//*[@text=\'{}\']/following-sibling::android.view.View'.format("選擇回診時間")
		revisitTimeObj = self.driver.find_element_by_xpath(revisitTimeXpath)
		revisitTimeObj.click() #確認回診時間
		self.ft.findText("確定")
		self.ck.clickByString("確定")
		self.ft.findText("確定")
		self.ck.clickByString("確定")
		self.ck.clickByString("完成")
		timeStampXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
										   /child::android.view.View\
										   /following-sibling::android.view.View'.format("今天")
		nameXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
									  /child::android.view.View\
									  /parent::android.view.View\
									  /following-sibling::android.view.View\
									  /child::android.view.View'.format("今天")   #找不到原因，會選到錯的元件，已修正。
		timeStampObj = self.driver.find_element_by_xpath(timeStampXpath)
		nameObj = self.driver.find_element_by_xpath(nameXpath)
		currentTimeStamp = time.strftime("%Y/%m/%d %H:", time.localtime())

		if(currentTimeStamp in timeStampObj.text and revisitName == nameObj.text and actionSuccess):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)	
		sleep(5)	
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
		#----------------刪除-----------------
		self.ck.clickByString(timeStampObj.text)
		self.ft.findText("回診詳情")
		self.ck.clickByString("編輯")
		self.ft.findTextInWholePage("刪除")
		self.ck.clickByString("刪除")
		#----------------刪除-----------------

		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findText("親友健康")












