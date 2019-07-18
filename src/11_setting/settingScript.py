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
		self.changePhoneNumber()
		self.changePassword()

		self.deleteAccountTest()
		self.checkServiceTerm()
		self.checkPrivatePolicy()
		self.checkHelp()
		
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
		#self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/cb_subject",0)
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
		sleep(10)
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
	def changePhoneNumber(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 4)
		self.ft.findText("設定")
		self.ft.findTextInWholePage("帳號")
		self.ck.clickByString("帳號")
		self.ft.findText("變更手機號碼")
		self.ck.clickByString("變更手機號碼") 
		self.ft.findText("請輸入目前的手機號碼")
		flag1Xpath = '//*[@text=\'{}\']/preceding-sibling::android.widget.RelativeLayout\
										/child::android.widget.RelativeLayout\
										/child::android.widget.RelativeLayout\
										/child::android.widget.LinearLayout\
										/child::android.widget.LinearLayout\
										/child::android.widget.ImageView'.format("請輸入目前的手機號碼")
		flag1Obj = self.driver.find_element_by_xpath(flag1Xpath)

		flag2Xpath = '//*[@text=\'{}\']/preceding-sibling::android.widget.RelativeLayout\
										/child::android.widget.RelativeLayout\
										/child::android.widget.RelativeLayout\
										/child::android.widget.LinearLayout\
										/child::android.widget.LinearLayout\
										/child::android.widget.ImageView'.format("請輸入新的手機號碼")
		flag2Obj = self.driver.find_element_by_xpath(flag2Xpath)
		flag1Obj.click()
		self.ft.findText("選擇國家")
		self.ec.enter("taiwan", self.apkVersionIdName+"/editText_search")
		self.ft.findText("臺灣 (TW)")
		self.ck.clickByString("臺灣 (TW)")
		self.ft.findText("變更手機號碼")
		self.ec.enter("0111111111", self.apkVersionIdName+"/et_old_phone_num")

		flag2Obj.click()
		self.ft.findText("選擇國家")
		self.ec.enter("taiwan", self.apkVersionIdName+"/editText_search")
		self.ft.findText("臺灣 (TW)")
		self.ck.clickByString("臺灣 (TW)")
		self.ft.findText("變更手機號碼")
		self.ec.enter("0911111111", self.apkVersionIdName+"/et_new_phone_num")
		self.ck.clickByString("檢查號碼")

		if(self.gt.search4Toast("此組電話號碼不存在，請確認號碼是否正確", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("帳號")
		self.driver.keyevent("4")
		self.ft.findText("設定")
		sleep(5)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")	
	def changePassword(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 4)
		self.ft.findText("設定")
		self.ft.findTextInWholePage("帳號")
		self.ck.clickByString("帳號")
		self.ft.findText("變更密碼")
		self.ck.clickByString("變更密碼")
		self.ft.findText("請輸入使用中的密碼")
		self.ec.enter("123456", self.apkVersionIdName+"/et_old_pass")
		self.ec.enter("654321", self.apkVersionIdName+"/et_new_pass")
		self.ec.enter("654321", self.apkVersionIdName+"/et_new_repass")
		self.ck.clickByString("確認")

		if(self.gt.search4Toast("密碼錯誤，請確認密碼是否正確", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("帳號")
		self.driver.keyevent("4")
		self.ft.findText("設定")
		sleep(5)


		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")

	def deleteAccountTest(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 4)
		self.ft.findText("設定")
		self.ft.findTextInWholePage("帳號")
		self.ck.clickByString("帳號")
		self.ft.findText("刪除帳號")
		self.ck.clickByString("刪除帳號")
		if(self.ft.findText("刪除WaCare帳號後，您將無法再使用該帳號登入。確定要繼續嗎？", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.ck.clickByString("取消")
		self.ft.findText("帳號")
		self.driver.keyevent("4")
		self.ft.findText("設定")
		sleep(5)

		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")

	def checkServiceTerm(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 4)
		self.ft.findText("設定")
		self.ft.findTextInWholePage("服務條款")
		self.ck.clickByString("服務條款")
		sleep(5)
		if(self.ft.findText("WaCare - 服務條款", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)

		self.driver.keyevent("4")
		self.ft.findText("設定")
		sleep(5)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")

	def checkPrivatePolicy(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 4)
		self.ft.findText("設定")
		self.ft.findTextInWholePage("隱私權政策")
		self.ck.clickByString("隱私權政策")
		sleep(5)
		if(self.ft.findText("WaCare 隱私權承諾書", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("設定")
		sleep(5)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")

	def checkHelp(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 4)
		self.ft.findText("設定")
		self.ft.findTextInWholePage("幫助")
		self.ck.clickByString("幫助")
		if(self.ft.findText("關於WaCare", mode=1)):
			print("[PASS]-"+sys._getframe().f_code.co_name)
		else:
			print("[FAIL]-"+sys._getframe().f_code.co_name)
		self.driver.keyevent("4")
		self.ft.findText("設定")
		sleep(5)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")

	
"""
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
"""


























