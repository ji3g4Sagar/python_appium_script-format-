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
		self.addMedicalExamination()

	def addMedicalExamination(self):
		self.hp.goBackToHomePage()
		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 1)
		self.ft.findText("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic", 0)
		self.ft.findTextInWholePage("檢驗")
		self.ck.clickByString("檢驗")
		sleep(10)
		examinationIndex = 0
		examinationCurrentLevel = 0
		actionSuccess = True
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


