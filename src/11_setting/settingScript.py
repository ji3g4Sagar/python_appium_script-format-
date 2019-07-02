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



class scriptSetting():
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
		self.urgentCard()
		self.editIll()
		self.getCuponFailed()
		self.addPayment()
		self.checkDevices()
		
	def urgentCard(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",4)
		sleep(1)
		self.ft.findTextInWholePage("急難卡")
		self.ck.clickByString("急難卡")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/sw_alert_forever")
		self.ck.clickByResourceID(self.apkVersionIdName+"/sw_alert_forever") # 點擊switch 關閉通知
		self.ck.clickByResourceID(self.apkVersionIdName+"/sw_alert_forever") # 點擊switch 開啟通知
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")		
		self.driver.keyevent("4")
		sleep(3)
	def editIll(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",4)
		sleep(1)
		self.ft.findTextInWholePage("急難卡")
		self.ck.clickByString("急難卡")
		self.ft.findText("編輯")
		self.ck.clickByString("編輯")
		self.ft.findTextInWholePage("疾病史")
		self.ck.clickByString("取消")  #為了測試按鈕
		self.ft.findText("編輯")
		self.ck.clickByString("編輯")
		self.ft.findTextInWholePage("疾病史")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",0)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",1)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",2)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",3) #疾病史多選
		self.ft.findTextInWholePage("癌症")
		self.ck.clickByString("癌症")
		self.ft.findTextInWholePage("重大傷病/其他")
		self.ck.clickByString("重大傷病/其他")
		self.ck.clickByString("下一步")
		#-----------------------------------------#
		#家族疾病史測試
		self.ft.findTextInWholePage("家族疾病史")
		self.ck.clickByString("取消")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_check_detail")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_health_status_edit")
		self.ft.findTextInWholePage("疾病史")
		self.ck.clickByString("下一步")
		self.ft.findTextInWholePage("家族疾病史")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("疾病史")
		self.ck.clickByString("下一步")
		self.ft.findTextInWholePage("家族疾病史")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_back")
		self.ft.findTextInWholePage("疾病史")
		self.ck.clickByString("下一步")
		self.ft.findTextInWholePage("家族疾病史")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",0)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",1)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",2)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",3) 
		self.ft.findTextInWholePage("癌症")
		self.ck.clickByString("癌症")
		self.ft.findTextInWholePage("其他疾病")
		self.ck.clickByString("重大傷病/其他")
		self.ck.clickByString("下一步")
		#--------------------------------------#
		#生活習慣測試
		self.ft.findTextInWholePage("生活習慣")
		self.ck.clickByString("取消")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_check_detail")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_health_status_edit")
		self.ft.findTextInWholePage("疾病史")
		self.ck.clickByString("下一步")
		self.ft.findTextInWholePage("家族疾病史")
		self.ck.clickByString("下一步")
		self.ft.findTextInWholePage("生活習慣")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("家族疾病史")
		self.ck.clickByString("下一步")
		self.ft.findTextInWholePage("生活習慣")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_back")
		self.ft.findTextInWholePage("家族疾病史")
		self.ck.clickByString("下一步")
		self.ft.findTextInWholePage("生活習慣")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",0)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",1)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",2)
		self.ck.clickByString("藥品")
		#self.ec.enterSelectByTextviewText("測試藥品名藥品名", "請輸入藥物名稱")
		self.ck.clickByString("下一步")
		#------------------------------------#
		#精神情緒狀況測試
		self.ft.findTextInWholePage("精神情緒狀態")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage("生活習慣")
		self.ck.clickByString("下一步")
		self.ft.findTextInWholePage("精神情緒狀態")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_back")
		self.ft.findTextInWholePage("生活習慣")
		self.ck.clickByString("下一步")
		self.ft.findTextInWholePage("精神情緒狀態")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",0)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",1)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",2)
		self.ft.findTextInWholePage("失眠")
		self.ck.clickByString("失眠")
		self.ck.clickByString("其他")
		self.ck.clickByString("完成")
		#self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_check_detail")
		self.ft.findTextInWholePage("急難卡")
		#self.ck.clickByResourceID(self.apkVersionIdName+"iv_back")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")	
		self.driver.keyevent("4")	
		sleep(3)
	def getCuponFailed(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 4)
		self.ft.findText("優惠券")
		self.ck.clickByString("優惠券")
		self.ft.findText("領取優惠券")
		self.ck.clickByString("領取優惠券")
		cuponCode = "abcdefghij"
		self.ec.enter(cuponCode, self.apkVersionIdName+"/et_coupon_code")
		self.ck.clickByString("確認")
		if(self.gt.search4Toast("代碼無效或重複領取", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("領取優惠券")
		self.driver.keyevent("4")
		sleep(5)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
	def addPayment(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 4)
		self.ft.findText("付款")
		self.ck.clickByString("付款")
		self.ft.findText("付款方式設定")
		self.ck.clickByString("+新增卡片")
		if(self.ft.findTextInWholePage("本服務由中國信託銀行提供", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("付款方式設定")
		self.driver.keyevent("4")
		sleep(5)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
	def checkDevices(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		actionSuccess = True
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 4)
		self.ft.findText("裝置")
		self.ck.clickByString("裝置")
		self.ft.findText("請選擇您的裝置")
		fitbitDeviceXpath = '//*[@text=\'{}\']/parent::android.widget.LinearLayout\
										/parent::android.widget.LinearLayout\
										/following-sibling::android.widget.LinearLayout'.format("請選擇您的裝置")
		fitbitDeviceObj = self.driver.find_element_by_xpath(fitbitDeviceXpath)
		fitbitDeviceObj.click()
		sleep(10)
		if(self.ft.findTextInWholePage("想要試用 Fitbit？", mode=1)):
			actionSuccess and True
		else:
			actionSuccess and False
			

		self.driver.keyevent("4")
		self.ft.findText("裝置")
		self.ck.clickByString("裝置")
		self.ft.findText("請選擇您的裝置")
		garminDeviceXpath = '//*[@text=\'{}\']/parent::android.widget.LinearLayout\
										/parent::android.widget.LinearLayout\
										/following-sibling::android.widget.LinearLayout\
										/following-sibling::android.widget.LinearLayout\
										/following-sibling::android.widget.LinearLayout'.format("請選擇您的裝置")
		garminDeviceObj = self.driver.find_element_by_xpath(garminDeviceXpath)
		garminDeviceObj.click()
		sleep(10)
		if(self.ft.findTextInWholePage("Sign In", mode=1)):
			actionSuccess and True
		else:
			actionSuccess and False

		sleep(4)
		self.driver.keyevent("4")

		if(actionSuccess):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		sleep(5)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")

	
"""
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
"""


























