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
		self.addBP_TW()
		self.addBP_US()
		self.addBP_EU()
		self.editBP()
		self.failBP()
		self.deleteBP()
		self.addBG()
		self.addICDatda()
		self.addICNodata()
		self.icLevels()
		self.takeMedicine()
		self.addRankintable()
		self.addCigarette()
		self.addNewSituationEmergency()
		self.addNewSituationNotice()
		self.addReVisit()
		self.checkReVisitData()
		self.addReVisitEmpty()

		self.addMedicalExamination()

	def _setBPStandard(self, standardCode):
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("血壓")
		self.ck.clickByString("血壓")
		self.ft.findTextInWholePage(" 設定標準 ")
		self.ck.clickByString(" 設定標準 ")
		self.ft.findText("設定個人化標準")
		self.ck.clickByResourceID(self.apkVersionIdName+"/spn_bp_standard")
		if(standardCode == 1):
			self.ft.findText("2017 中華民國心臟學會標準")
			self.ck.clickByString("2017 中華民國心臟學會標準")
		elif (standardCode == 2):
			self.ft.findText("2017 美國心臟醫學會標準")
			self.ck.clickByString("2017 美國心臟醫學會標準")
		elif (standardCode == 3):
			self.ft.findText("2018 歐洲心臟/高血壓學會標準")
			self.ck.clickByString("2018 歐洲心臟/高血壓學會標準")
		self.ck.clickByString("確認")
	def addBP_TW(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self._setBPStandard(1)
		for i in range (4):
			self.ck.clickByResourceID(self.apkVersionIdName+"/ivAdd")
			self.ft.findText("如何量血壓")
			systolic, diastolic, bpLevelText = self._bpStandard_TW(i)
			print(systolic, diastolic, bpLevelText)
			self.ft.findText("晚上")
			systolicXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/following-sibling::android.widget.EditText'.format("晚上")
			systolicFiled = self.driver.find_element_by_xpath(systolicXpath)
			systolicFiled.set_text(systolic)

			diastolicXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/following-sibling::android.widget.EditText\
											/following-sibling::android.view.View\
											/following-sibling::android.widget.EditText'.format("晚上")
			diastolicFiled = self.driver.find_element_by_xpath(diastolicXpath)
			diastolicFiled.set_text(diastolic)
			self.ck.clickByString("完成")
			targetXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
											/preceding-sibling::android.view.View\
											/following-sibling::android.view.View'.format(bpLevelText)
			target = self.driver.find_element_by_xpath(targetXpath)
			bpTime =  time.strftime("%H", time.localtime())
			print(target.text)
			print(bpTime)
			if(bpTime in target.text):
				print("[PASS]-"+sys._getframe().f_code.co_name)
			else:
				print("[FAIL]-"+sys._getframe().f_code.co_name)
			sleep(2)

		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")

		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def addBP_EU(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self._setBPStandard(3)
		for i in range (4):
			self.ck.clickByResourceID(self.apkVersionIdName+"/ivAdd")
			self.ft.findText("如何量血壓")
			systolic, diastolic, bpLevelText = self._bpStandard_EU(i)
			systolicXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/following-sibling::android.widget.EditText'.format("晚上")
			systolicFiled = self.driver.find_element_by_xpath(systolicXpath)
			systolicFiled.set_text(systolic)

			diastolicXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/following-sibling::android.widget.EditText\
											/following-sibling::android.view.View\
											/following-sibling::android.widget.EditText'.format("晚上")
			diastolicFiled = self.driver.find_element_by_xpath(diastolicXpath)
			diastolicFiled.set_text(diastolic)
			self.ck.clickByString("完成")
			targetXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
											/preceding-sibling::android.view.View\
											/following-sibling::android.view.View'.format(bpLevelText)
			target = self.driver.find_element_by_xpath(targetXpath)
			bpTime =  time.strftime("%H", time.localtime())
			print(target.text)
			print(bpTime)
			if(bpTime in target.text):
				print("[PASS]-"+sys._getframe().f_code.co_name)
			else:
				print("[FAIL]-"+sys._getframe().f_code.co_name)
			sleep(2)
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")

		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def addBP_US(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self._setBPStandard(2)
		for i in range (3):
			self.ck.clickByResourceID(self.apkVersionIdName+"/ivAdd")
			self.ft.findText("如何量血壓")
			systolic, diastolic, bpLevelText = self._bpStandard_US(i)
			print(systolic, diastolic, bpLevelText)
			systolicXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/following-sibling::android.widget.EditText'.format("晚上")
			systolicFiled = self.driver.find_element_by_xpath(systolicXpath)
			systolicFiled.set_text(systolic)

			diastolicXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/following-sibling::android.widget.EditText\
											/following-sibling::android.view.View\
											/following-sibling::android.widget.EditText'.format("晚上")
			diastolicFiled = self.driver.find_element_by_xpath(diastolicXpath)
			diastolicFiled.set_text(diastolic)
			self.ck.clickByString("完成")
			targetXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
											/preceding-sibling::android.view.View\
											/following-sibling::android.view.View'.format(bpLevelText)
			target = self.driver.find_element_by_xpath(targetXpath)
			bpTime =  time.strftime("%H", time.localtime())
			print(target.text)
			print(bpTime)
			if(bpTime in target.text):
				print("[PASS]-"+sys._getframe().f_code.co_name)
			else:
				print("[FAIL]-"+sys._getframe().f_code.co_name)
			sleep(2)
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")

		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def _bpStandard_TW(self, bpLevel):
		if(bpLevel == 0): #緊急
			return "180", "110", "緊急"
		elif(bpLevel == 1):#正常
			return "111", "79", "正常"
		elif(bpLevel == 2):#留意
			return "131", "89", "留意"
		elif(bpLevel == 3):#注意
			return "131", "90", "注意"
	def _bpStandard_EU(self, bpLevel):
		if(bpLevel == 0):
			return "181", "110", "緊急"
		elif(bpLevel == 1):
			return "178", "109", "注意"
		elif(bpLevel == 2):
			return "139", "89", "留意"
		elif(bpLevel == 3):
			return "111", "79", "正常"
	def _bpStandard_US(self, bpLevel):
		if(bpLevel == 0):
			return "130", "80", "注意"
		elif(bpLevel == 1):
			return "129", "79", "留意"
		elif(bpLevel == 2):
			return "119", "79", "正常"
	def editBP(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("血壓")
		self.ck.clickByString("血壓")
		self.ft.findText("今日")
		self.ck.clickByString("今日")
		sleep(1)
		self.ft.findText("今日")
		self.ck.clickByString("今日")
		self.ft.findText("編輯")
		self.ck.clickByString("編輯")
		self.ft.findText("儲存")
		editSystolic = str(random.randint(1,299))
		editDiastolic = str(random.randint(1,299))
		print(editDiastolic, editSystolic)
		systolicXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/following-sibling::android.widget.EditText'.format("晚上")
		systolicFiled = self.driver.find_element_by_xpath(systolicXpath)
		systolicFiled.click()
		for i in range(len(systolicFiled.text)):
			self.driver.keyevent("67")
		systolicFiled.set_text(editSystolic)
		diastolicXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/following-sibling::android.widget.EditText\
											/following-sibling::android.view.View\
											/following-sibling::android.widget.EditText'.format("晚上")
		diastolicFiled = self.driver.find_element_by_xpath(diastolicXpath)
		diastolicFiled.click()
		for i in range(len(diastolicFiled.text)):
			self.driver.keyevent("67")
		diastolicFiled.set_text(editDiastolic)
		self.ck.clickByString("儲存")
		if(self.ft.findText(editSystolic, mode=1) and self.ft.findText(editDiastolic, mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		sleep(3)
		self.driver.keyevent("4")
		self.ft.findText("今日")
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")

		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def deleteBP(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("血壓")
		self.ck.clickByString("血壓")
		self.ft.findText("今日")
		self.ck.clickByString("今日")
		sleep(1)
		self.ft.findText("今日")
		self.ck.clickByString("今日")
		self.ft.findText("編輯")
		self.ck.clickByString("編輯")
		systolicXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/following-sibling::android.widget.EditText'.format("晚上")
		systolicFiled = self.driver.find_element_by_xpath(systolicXpath)
		systolic = systolicFiled.text
		diastolicXpath = '//*[@text=\'{}\']/parent::android.view.View\
											/following-sibling::android.widget.EditText\
											/following-sibling::android.view.View\
											/following-sibling::android.widget.EditText'.format("晚上")
		diastolicFiled = self.driver.find_element_by_xpath(diastolicXpath)
		diastolic = diastolicFiled.text
		self.ft.findText("刪除")
		self.ck.clickByString("刪除")
		
		self.ft.findText("確認")
		self.ck.clickByString("確認")
		if(self.ft.findText(systolic, mode=1) and self.ft.findText(diastolic, mode=1)):
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		else:
			print("[PASS]-"+sys._getframe().f_code.co_name)

		sleep(3)
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def failBP(self):
		actionSuccess = False
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("血壓")
		self.ck.clickByString("血壓")
		self.ft.findText("今日")
		self.ck.clickByString("今日")
		sleep(1)
		self.ft.findText("作廢")
		self.ck.clickByString("作廢")
		self.ck.clickByString("今日")
		self.ft.findText("編輯")
		if(self.ft.findText("此筆資料作廢", mode=1)):
			actionSuccess = True
		else:
			actionSuccess = False
		self.driver.keyevent("4")
		self.ft.findText("恢復")
		self.ck.clickByString("恢復")
		self.ck.clickByString("今日")
		self.ft.findText("編輯")
		if(self.ft.findText("此筆資料作廢", mode=1)):
			actionSuccess = False
		else:
			actionSuccess = True
		sleep(3)
		if(actionSuccess):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)

		self.driver.keyevent("4")
		self.ft.findText("今日")
		self.driver.keyevent("4")
		self.ft.findText("今日")
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def addBG(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("血糖")
		self.ck.clickByString("血糖")
		self.ft.findText("WHO標準")
		for i in range(4):
			self.ck.clickByResourceID(self.apkVersionIdName+"/iv_mybloodSugar_Plus")
			self.ft.findText("早餐前")
			self.ck.clickByString("早餐前")
			self.ck.clickByString("下一步")
			self.ft.findText("請輸入血糖值")
			bloodGlucose, bloodGlucoseLevel = self._bloodGlucoseValueAndLevel(i)
			self.ck.clickByString("請輸入血糖值")
			self.ec.enter(bloodGlucose, self.apkVersionIdName+"/et_blood_sugar")
			self.ck.clickByString("確認")
			sleep(3)
			bloodGlucoseDateXpath = '//*[@text=\'{}\']/parent::android.widget.LinearLayout\
												  /preceding-sibling::android.widget.LinearLayout\
												  /preceding-sibling::android.widget.FrameLayout\
												  /child::android.widget.TextView'.format(bloodGlucose+" 	mg/dL")
			bloodGlucoseDateObj = self.driver.find_element_by_xpath(bloodGlucoseDateXpath)
			print(bloodGlucoseDateObj.text)

			bloodGlucoseLevelXpath = '//*[@text=\'{}\']/parent::android.widget.LinearLayout\
												  /following-sibling::android.widget.FrameLayout\
												  /child::android.widget.TextView'.format(bloodGlucose+" 	mg/dL")
			bloodGlucoseLevelObj = self.driver.find_element_by_xpath(bloodGlucoseLevelXpath)
			print(bloodGlucoseLevelObj.text)

			if(bloodGlucoseDateObj.text == "今日" and bloodGlucoseLevelObj.text == bloodGlucoseLevel):
				print("[PASS]-"+sys._getframe().f_code.co_name)
			else:
				print("[FAIL]-"+sys._getframe().f_code.co_name)
		sleep(3)		
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		sleep(5)

		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def _bloodGlucoseValueAndLevel(self, bGLevel):
		if(bGLevel == 0):		
			return str(random.randint(70,99)), "正常"
		elif(bGLevel == 1):
			return str(random.randint(100,125)), "留意"
		elif(bGLevel == 2):
			return str(random.randint(126,200)), "注意"
		elif(bGLevel == 3):
			return str(random.randint(600,999)), "緊急"
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
		urgencyBarXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
											/child::android.view.View\
											/child::android.view.View'.format("尿急程度")
		urgencyBarObj = self.driver.find_element_by_xpath(urgencyBarXpath)
		urgencyBarX = urgencyBarObj.location['x']
		urgencyBarY = urgencyBarObj.location['y']
		self.driver.tap([(urgencyBarX+float(380), urgencyBarY)])
		self.ft.findTextInWholePage("查看月曆")
		urinaryVolume = str(random.randint(1,70))
		urinaryVolumeXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
												  /child::android.widget.EditText'.format("紀錄您現在的排尿量(單位:c.c.)")
		urinaryVolumeFiled = self.driver.find_element_by_xpath(urinaryVolumeXpath)
		urinaryVolumeFiled.click()
		urinaryVolumeFiled.set_text(urinaryVolume)
		self.ck.clickByString("上傳")
		self.gt.search4Toast("新增成功")
		if(self.ft.findText(urinaryVolume+"c.c", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
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
		actionSuccess = False
		for i in range(11):
			self.ft.findText("IC_TICA")
			painBarX, painBarY, urgencyBarX, urgencyBarY, levelText, urinaryVolume = self._icLevelToLocation(i)
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
			urinaryVolumeFiled.set_text(urinaryVolume)
			self.ck.clickByString("上傳")
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
				actionSuccess = True
			else:
				print("not found")
				actionSuccess = False
			sleep(4)
			self.driver.keyevent("4")

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
			return 298, 788, 298, 1287, "輕微", urinaryVolume
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
	def takeMedicine(self): #無法測試，因為web view 的XML跑版，選擇不到元件
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("用藥")
		self.ck.clickByString("用藥")
		self.ft.findText("今日藥物")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_MedicineListAdd")
		self.ft.findText("*新增藥物照片")
		self.ck.clickByString("*新增藥物照片")
		self.ft.findText("選擇照片")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/file_thumbnail",1)
		self.ck.clickByString("傳送")
		self.ft.findText("新增用藥")
		self.ck.clickByString("新增用藥")

		medicineNameXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
											/child::android.widget.EditText'.format("*用藥時間")
		medicineNameObj = self.driver.find_element_by_xpath(medicineNameXpath)
		medicineNameObj.click()
		medicienceNmae = time.strftime("%m/%d", time.localtime()) + " No." + str(random.randint(1,1000))
		medicineNameObj.set_text(medicienceNmae)

		takeMedicineTimeXpath = '//*[@text=\'{}\']/preceding-sibling::android.view.View\
												  /preceding-sibling::android.view.View\
												  /child::android.view.View\
												  /child::android.view.View'.format("早上")
		takeMedicineTimeObj = self.driver.find_element_by_xpath(takeMedicineTimeXpath)
		takeMedicineTimeObj.click()
		self.sp.swipeUp()
		startDateXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
										   /following-sibling::android.view.View'.format("*用藥時間")

 		endDateXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
										   /following-sibling::android.view.View\
										   /following-sibling::android.view.View\
 										   /child::android.widget.EditText\
 										   /following-sibling::android.widget.EditText'.format("*用藥時間")
 		startDateObj = self.driver.find_element_by_xpath(startDateXpath)  # 抓不到 物件
 		print(startDateObj.text)
 		endDateObj = self.driver.find_element_by_xpath(endDateXpath)

 		startDateObj.click()
 		self.ft.findText("確定")
 		self.ck.clickByString("確定")
 		endDateObj.click()
 		self.ft.findText("確定")
 		self.ck.clickByString("確定")
 		self.ft.findText("新增")
 		self.ck.clickByString("新增")
 		if(self.ft.findText(medicienceNmae, mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
 		self.driver.keyevent("4")
 		self.ft.findText("健康燈設定")
 		self.driver.keyevent("4")

		sleep(5)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def addRankintable(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findText("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("中風")
		self.ck.clickByString("中風")
		self.ft.findText("請選擇欲新增項目")
		self.ck.clickByString("Rankin量表")
		levels = random.randint(0,5)
		self.ft.findText("下一頁")
		self.ck.clickByString("下一頁")
		targetText = self._rankinLevels(levels)
		self.ck.clickByString(targetText)
		self.ck.clickByString("送出")
		self.ft.findText("中風")
		timeStampXpath = '//*[@text=\'{}\']/following-sibling::android.view.View'.format("今日")
		timeStampObj = self.driver.find_element_by_xpath(timeStampXpath)
		levelXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
									   /following-sibling::android.view.View'.format("今日")
		levelObj = self.driver.find_element_by_xpath(levelXpath)
		print(timeStampObj.text, ": ", levelObj.text)
		nowTime = time.strftime("%H", time.localtime())
		if(nowTime in timeStampObj.text and str(levels) == levelObj.text):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findText("親友健康")

		sleep(5)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def _rankinLevels(self, innerLevels):
		if(innerLevels == 0):
			return "完全無症狀"
		elif(innerLevels == 1):
			return "儘管有症狀，但無明顯功能障礙，能完成所有日常工作和生活"
		elif(innerLevels == 2):
			return "輕度殘疾，不能完成病前所有活動，但不需幫助能照料自己的日常事務"
		elif(innerLevels == 3):
			return "中度殘疾，需部分説明，但能獨立行走"
		elif(innerLevels == 4):
			return "中重度殘疾，不能獨立行走，日常生活需別人幫助"
		elif(innerLevels == 5):
			return "重度殘疾，臥床，二便失禁，日常生活完全依賴他人"
	def addCigarette(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findText("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("中風")
		self.ck.clickByString("中風")
		self.ft.findText("請選擇欲新增項目")
		self.ck.clickByString("抽菸數量")
		self.ft.findText("新增抽菸紀錄")
		cigaretteNum = str(random.randint(1, 99))
		cigaretteNumEditTextXpath = '//*[@text=\'{}\']/preceding-sibling::android.widget.EditText'.format("根")
		cigaretteNumEditTextObj = self.driver.find_element_by_xpath(cigaretteNumEditTextXpath)
		cigaretteNumEditTextObj.click()
		cigaretteNumEditTextObj.set_text(cigaretteNum)
		self.ck.clickByString("上傳")
		self.ft.findText("中風")
		if(self.ft.findText(cigaretteNum, mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		sleep(5)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def addNewSituationEmergency(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findText("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("中風")
		self.ck.clickByString("中風")
		self.ft.findText("請選擇欲新增項目")
		self.ck.clickByString("新發現狀況")
		emergencyStatement = self._newSituationLevel(random.randint(0, 2))
		self.ft.findText(emergencyStatement)
		emergencyCheckBoxXpath = '//*[@text=\'{}\']'.format(emergencyStatement)
		emergencyCheckBoxObj = self.driver.find_element_by_xpath(emergencyCheckBoxXpath)

		checkBoxX = emergencyCheckBoxObj.location['x']
		checkBoxY = emergencyCheckBoxObj.location['y']
		print(checkBoxX, checkBoxY)
		self.driver.tap([(checkBoxX-float(55), checkBoxY+float(30))])
		emergencyCheckBoxObj.click()
		self.ck.clickByString("上傳")
		self.ft.findText("建議撥打119電話或儘速就醫！")
		self.ck.clickByString("關閉")
		nowTime = time.strftime("%H", time.localtime())
		emergencyTimeXpath = '//*[@text=\'{}\']/following-sibling::android.view.View'.format("今日")
		emergencyStatementXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
													/following-sibling::android.view.View'.format("今日")
		emergencyTimeObj = self.driver.find_element_by_xpath(emergencyTimeXpath)
		emergencyStatementObj = self.driver.find_element_by_xpath(emergencyStatementXpath)
		print(emergencyStatementObj.text)
		print("\n")
		print(emergencyStatement)

		if (nowTime in emergencyTimeObj.text and emergencyStatement == emergencyStatementObj.text):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findText("親友健康")

		sleep(5)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def addNewSituationNotice(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findText("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("中風")
		self.ck.clickByString("中風")
		self.ft.findText("請選擇欲新增項目")
		self.ck.clickByString("新發現狀況")
		emergencyStatement = self._newSituationLevel(random.randint(3, 7))
		self.ft.findText(emergencyStatement)
		emergencyCheckBoxXpath = '//*[@text=\'{}\']'.format(emergencyStatement)
		emergencyCheckBoxObj = self.driver.find_element_by_xpath(emergencyCheckBoxXpath)

		checkBoxX = emergencyCheckBoxObj.location['x']
		checkBoxY = emergencyCheckBoxObj.location['y']
		print(checkBoxX, checkBoxY)
		self.driver.tap([(checkBoxX-float(55), checkBoxY+float(30))])
		emergencyCheckBoxObj.click()
		self.ck.clickByString("上傳")
		self.ft.findText("建議您提早回診")
		self.ck.clickByString("確認")
		nowTime = time.strftime("%H", time.localtime())
		emergencyTimeXpath = '//*[@text=\'{}\']/following-sibling::android.view.View'.format("今日")
		emergencyStatementXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
													/following-sibling::android.view.View'.format("今日")
		emergencyTimeObj = self.driver.find_element_by_xpath(emergencyTimeXpath)
		emergencyStatementObj = self.driver.find_element_by_xpath(emergencyStatementXpath)
		

		if (nowTime in emergencyTimeObj.text and emergencyStatement == emergencyStatementObj.text):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findText("親友健康")

		sleep(5)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def _newSituationLevel(self, innerLevels):
		if(innerLevels == 0):
			return "新發現臉部表情不對稱"
		elif(innerLevels == 1):
			return "新發現一隻手臂無力下垂"
		elif(innerLevels == 2):
			return "新發現說話含糊不清"
		elif(innerLevels == 3):
			return "流鼻血"
		elif(innerLevels == 4):
			return "牙齦出血"
		elif(innerLevels == 5):
			return "血尿"
		elif(innerLevels == 6):
			return "血便"
		elif(innerLevels == 7):
			return "身上不明血點/瘀青"
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
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findText("親友健康")
		if(currentTimeStamp in timeStampObj.text and revisitName == nameObj.text):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		sleep(5)	
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
	def checkReVisitData(self):
		self.hp.goBackToHomePage()
		actionSuccess = False
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
			actionSuccess = True
		else:
			actionSuccess = False
		checkBoxObj.click()
		if(self.ft.findText("今天", mode=1)):
			actionSuccess = True
		else:
			actionSuccess = False

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
		actionSuccess = False
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
			actionSuccess = True
		else:
			actionSuccess = False

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
			actionSuccess = True
		else:
			actionSuccess = False

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
			actionSuccess = True
		else:
			actionSuccess = False

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
		if(currentTimeStamp in timeStampObj.text and revisitName == nameObj.text and actionSuccess):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)	
		sleep(5)	
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")

	def addMedicalExamination(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 1)
		self.ft.findText("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic", 0)
		self.ft.findTextInWholePage("檢驗")
		self.ck.clickByString("檢驗")
		sleep(10)
		examinationIndex = 12
		examinationCurrentLevel = 0
		actionSuccess = False
		while(examinationIndex < 21):
			examinationItem, examinationValue, examinationLevelNumber, examinationResult = self._medicalExamination(examinationIndex, examinationCurrentLevel)			
				
			if(examinationCurrentLevel < examinationLevelNumber):

				self.ft.findText("檢驗")
				self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/ivAdd")
				self.ck.clickByResourceID(self.apkVersionIdName+"/ivAdd")
				self.ft.findText("生化檢查")
				self.ck.clickByString("生化檢查")
				self.ft.findTextInWholePage(examinationItem)
				itemValueFiledXpath = '//*[@text=\'{}\']/following-sibling::android.view.View\
										   /child::android.widget.EditText'.format(examinationItem)
				itemValueFiledObj = self.driver.find_element_by_xpath(itemValueFiledXpath)
				itemValueFiledObj.click()
				itemValueFiledObj.set_text(examinationValue)
				self.ck.clickByString("上傳")
				self.ft.findText("檢驗")
				examinationItemNameXapth = '//*[@text=\'{}\']/following-sibling::android.view.View'.format("項目名稱")
				examinationVlaueXpath = '//*[@text=\'{}\']/following-sibling::android.view.View'.format("檢查結果")
				resultXpath = '//*[@text=\'{}\']/following-sibling::android.view.View'.format("狀態")
				examinationItemNameObj = self.driver.find_element_by_xpath(examinationItemNameXapth)
				examinationVlaueObj = self.driver.find_element_by_xpath(examinationVlaueXpath)
				resultObj = self.driver.find_element_by_xpath(resultXpath)
				print("Return: ")
				print(examinationItem)
				print(examinationValue)
				print(examinationResult)
				print("Current: ")
				print(examinationItemNameObj.text)
				print(examinationVlaueObj.text)
				print(resultObj.text)
				if(examinationItemNameObj.text in examinationItem and examinationVlaueObj.text == str(examinationValue) and examinationResult == resultObj.text):
					actionSuccess = True and actionSuccess
				else:
					actionSuccess = False and actionSuccess
				examinationCurrentLevel = examinationCurrentLevel + 1
				#-----------刪除該筆檢測資料---------------
				examinationItemNameObj.click()
				self.ft.findText(str(examinationValue))
				examinationResultXpath = '//*[@text=\'{}\']/following-sibling::android.widget.Image'.format(examinationResult)
				examinationResultObj = self.driver.find_element_by_xpath(examinationResultXpath)
				examinationResultObj.click()
				self.ft.findText("刪除")
				self.ck.clickByString("刪除")
				self.ft.findText("提醒")
				self.ck.clickByString("刪除")
				sleep(5)
				#-----------刪除該筆檢測資料---------------
				self.driver.keyevent("4")

			else:
				examinationCurrentLevel = 0
				examinationIndex = examinationIndex + 1
		self.ft.findText("檢驗")
		self.driver.keyevent("4")
		self.ft.findText("健康燈設定")
		self.driver.keyevent("4")
		self.ft.findText("親友健康")

		if (actionSuccess):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)




		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
		


	def _medicalExamination(self, examinationIndex, examinationCurrentLevel): #examinationIndex: 對應不同的檢驗項目; examinationLevel: 對應各自檢驗項目的數值等級
		if(examinationIndex == 0):
			if (examinationCurrentLevel == 0):
				return "CHOL膽固醇", random.randint(1,199), 3, "正常"
			elif (examinationCurrentLevel == 1):
				return "CHOL膽固醇", random.randint(200,239), 3, "普通"
			elif (examinationCurrentLevel == 2):
				return "CHOL膽固醇", random.randint(240,999), 3, "注意"
			else:
				return "null", -1, 3, "null"


		elif(examinationIndex == 1):
			if (examinationCurrentLevel == 0):
				return "HLD-C高密度脂蛋白膽固醇", random.randint(40,59), 3, "正常"
			elif (examinationCurrentLevel == 1):
				return "HLD-C高密度脂蛋白膽固醇", random.randint(1,39), 3, "留意"
			elif (examinationCurrentLevel == 2):
				return "HLD-C高密度脂蛋白膽固醇", random.randint(60,999), 3, "普通"
			else:
				return "null", -1, 3, "null"

		elif(examinationIndex == 2):
			if (examinationCurrentLevel == 0):
				return "LDL-C低密度脂蛋白膽固醇", random.randint(1,99), 5, "正常"
			elif (examinationCurrentLevel == 1):
				return "LDL-C低密度脂蛋白膽固醇", random.randint(100,129), 5, "普通"
			elif (examinationCurrentLevel == 2):
				return "LDL-C低密度脂蛋白膽固醇", random.randint(130,159), 5, "留意"
			elif (examinationCurrentLevel == 3):
				return "LDL-C低密度脂蛋白膽固醇", random.randint(160,189), 5, "注意"
			elif (examinationCurrentLevel == 4):
				return "LDL-C低密度脂蛋白膽固醇", random.randint(190,999), 5, "緊急"
			else:
				return "null", -1, 5, "null"
		elif(examinationIndex == 3):
			if (examinationCurrentLevel == 0):
				return "TG三酸甘油脂", random.randint(1,149), 4, "正常"
			elif (examinationCurrentLevel == 1):
				return "TG三酸甘油脂", random.randint(150,199), 4, "普通"
			elif (examinationCurrentLevel == 2):
				return "TG三酸甘油脂", random.randint(200,499), 4, "注意"
			elif (examinationCurrentLevel == 3):
				return "TG三酸甘油脂", random.randint(500,999), 4, "緊急"
			else:
				return "null", -1, 4, "null"
		elif(examinationIndex == 4):
			if (examinationCurrentLevel == 0):
				return "GluAC飯前血糖", random.randint(70,99), 7, "正常"
			elif (examinationCurrentLevel == 1):
				return "GluAC飯前血糖", random.randint(100,125), 7, "留意"
			elif (examinationCurrentLevel == 2):
				return "GluAC飯前血糖", random.randint(126,599), 7, "注意"
			elif (examinationCurrentLevel == 3):
				return "GluAC飯前血糖", random.randint(600,999), 7, "緊急"
			elif (examinationCurrentLevel == 4):
				return "GluAC飯前血糖", random.randint(50,69), 7, "留意"
			elif (examinationCurrentLevel == 5):
				return "GluAC飯前血糖", random.randint(40,49), 7, "注意"
			elif (examinationCurrentLevel == 6):
				return "GluAC飯前血糖", random.randint(1,39), 7, "緊急"
			else:
				return "null", -1, 7, "null"
		elif(examinationIndex == 5):
			if (examinationCurrentLevel == 0):
				return "GluPC飯後血糖", random.randint(70,139), 7, "正常"
			elif (examinationCurrentLevel == 1):
				return "GluPC飯後血糖", random.randint(140,199), 7, "留意"
			elif (examinationCurrentLevel == 2):
				return "GluPC飯後血糖", random.randint(200,599), 7, "注意"
			elif (examinationCurrentLevel == 3):
				return "GluPC飯後血糖", random.randint(600,999), 7, "緊急"
			elif (examinationCurrentLevel == 4):
				return "GluPC飯後血糖", random.randint(50,69), 7, "留意"
			elif (examinationCurrentLevel == 5):
				return "GluPC飯後血糖", random.randint(40,49), 7, "注意"
			elif (examinationCurrentLevel == 6):
				return "GluPC飯後血糖", random.randint(1,39), 7, "緊急"
			else:
				return "null", -1, 7, "null"
		elif(examinationIndex == 6):
			if (examinationCurrentLevel == 0):
				value = random.uniform(1, 5.6)
				return "HbA1C糖化血色素", ("%.1f")%value, 3, "正常"
			elif (examinationCurrentLevel == 1):
				value = random.uniform(5.7, 6.4)
				return "HbA1C糖化血色素", ("%.1f")%value, 3, "留意"
			elif (examinationCurrentLevel == 2):
				value = random.uniform(6.5, 99)
				return "HbA1C糖化血色素", ("%.1f")%value, 3, "注意"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 7):
			if (examinationCurrentLevel == 0):
				return "BUN尿素氮", random.randint(6,20), 3, "正常"
			elif (examinationCurrentLevel == 1):
				return "BUN尿素氮", random.randint(1,5), 3, "異常"
			elif (examinationCurrentLevel == 2):
				return "BUN尿素氮", random.randint(21,999), 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 8):
			if (examinationCurrentLevel == 0):
				value = random.uniform(0.6, 1.3)
				return "CREA肌酐酸", ("%.1f")%value, 3, "正常"
			elif (examinationCurrentLevel == 1):
				value = random.uniform(0.1, 0.5)
				return "CREA肌酐酸", ("%.1f")%value, 3, "異常"
			elif (examinationCurrentLevel == 2):
				value = random.uniform(1.4, 9.9)
				return "CREA肌酐酸", ("%.1f")%value, 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 9):
			if (examinationCurrentLevel == 0):
				value = random.uniform(3.4, 7.6)
				return "UA尿酸", ("%.1f")%value, 3, "正常"
			elif (examinationCurrentLevel == 1):
				value = random.uniform(0.1, 3.3)
				return "UA尿酸", ("%.1f")%value, 3, "異常"
			elif (examinationCurrentLevel == 2):
				value = random.uniform(7.7, 9.9)
				return "UA尿酸", ("%.1f")%value, 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 10):
			if (examinationCurrentLevel == 0):
				value = random.uniform(3.8, 5.3)
				return "ALB白蛋白", ("%.1f")%value, 3, "正常"
			elif (examinationCurrentLevel == 1):
				value = random.uniform(0.1, 3.7)
				return "ALB白蛋白", ("%.1f")%value, 3, "異常"
			elif (examinationCurrentLevel == 2):
				value = random.uniform(5.4, 9.9)
				return "ALB白蛋白", ("%.1f")%value, 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 11):
			if (examinationCurrentLevel == 0):
				return "ALK-P鹼性磷酸脢", random.randint(40,129), 3, "正常"
			elif (examinationCurrentLevel == 1):
				return "ALK-P鹼性磷酸脢", random.randint(1,39), 3, "異常"
			elif (examinationCurrentLevel == 2):
				return "ALK-P鹼性磷酸脢", random.randint(130,999), 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 12):
			if (examinationCurrentLevel == 0):
				value = random.uniform(0.1, 0.4)
				return "D-BIL直接膽血素", ("%.1f")%value, 2, "正常"
			elif (examinationCurrentLevel == 1):
				value = random.uniform(0.5, 9.9)
				return "D-BIL直接膽血素", ("%.1f")%value, 2, "異常"
			else:
				return "null", -1, 2, "null" 
		elif(examinationIndex == 13):
			if (examinationCurrentLevel == 0):
				return "GGT麩胺酸轉移脢", random.randint(8, 61), 3, "正常"
			elif (examinationCurrentLevel == 1):
				return "GGT麩胺酸轉移脢", random.randint(1,7), 3, "異常"
			elif (examinationCurrentLevel == 2):
				return "GGT麩胺酸轉移脢", random.randint(62,999), 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 14):
			if (examinationCurrentLevel == 0):
				value = random.uniform(2.5, 3.6)
				return "GLO球蛋白", ("%.1f")%value, 3, "正常"
			elif (examinationCurrentLevel == 1):
				value = random.uniform(0.1, 2.4)
				return "GLO球蛋白", ("%.1f")%value, 3, "異常"
			elif (examinationCurrentLevel == 2):
				value = random.uniform(3.7, 9.9)
				return "GLO球蛋白", ("%.1f")%value, 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 15):
			if (examinationCurrentLevel == 0):
				return "GOT麩胺酸草酸轉胺脢", random.randint(8, 38), 3, "正常"
			elif (examinationCurrentLevel == 1):
				return "GOT麩胺酸草酸轉胺脢", random.randint(1,7), 3, "異常"
			elif (examinationCurrentLevel == 2):
				return "GOT麩胺酸草酸轉胺脢", random.randint(39,999), 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 16):
			if (examinationCurrentLevel == 0):
				return "GPT丙酮酸轉胺脢", random.randint(4, 44), 3, "正常"
			elif (examinationCurrentLevel == 1):
				return "GPT丙酮酸轉胺脢", random.randint(1,3), 3, "異常"
			elif (examinationCurrentLevel == 2):
				return "GPT丙酮酸轉胺脢", random.randint(45,999), 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 17):
			if (examinationCurrentLevel == 0):
				value = random.uniform(0.2, 1.2)
				return "T-BIL總膽血素", ("%.1f")%value, 3, "正常"
			elif (examinationCurrentLevel == 1):
				return "T-BIL總膽血素", 0.1, 3, "異常"
			elif (examinationCurrentLevel == 2):
				value = random.uniform(1.2, 9.9)
				return "T-BIL總膽血素", ("%.1f")%value, 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 18):
			if (examinationCurrentLevel == 0):
				value = random.uniform(6.6, 8.7)
				return "TP總蛋白", ("%.1f")%value, 3, "正常"
			elif (examinationCurrentLevel == 1):
				value = random.uniform(0.1, 6.5)
				return "TP總蛋白", ("%.1f")%value, 3, "異常"
			elif (examinationCurrentLevel == 2):
				value = random.uniform(8.8, 9.9)
				return "TP總蛋白", ("%.1f")%value, 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 19):
			if (examinationCurrentLevel == 0):
				return "AMY澱粉脢", random.randint(43, 116), 3, "正常"
			elif (examinationCurrentLevel == 1):
				return "AMY澱粉脢", random.randint(1,42), 3, "異常"
			elif (examinationCurrentLevel == 2):
				return "AMY澱粉脢", random.randint(117,999), 3, "異常"
			else:
				return "null", -1, 3, "null"
		elif(examinationIndex == 20):
			if (examinationCurrentLevel == 0):
				return "LIPASE脂脢", random.randint(13, 60), 3, "正常"
			elif (examinationCurrentLevel == 1):
				return "LIPASE脂脢", random.randint(1,12), 3, "異常"
			elif (examinationCurrentLevel == 2):
				return "LIPASE脂脢", random.randint(61,999), 3, "異常"
			else:
				return "null", -1, 3, "null"
""""""





"""
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
"""




























