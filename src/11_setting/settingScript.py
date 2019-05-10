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
		#self.urgentCard()
		#self.editIll()
		#self.helthInfo()
		self.clickExpertMedic()

		
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
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_check_detail")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_health_status_edit")
		self.ft.findTextInWholePage("疾病史")
		self.ck.clickByString("取消")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_check_detail")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_health_status_edit")
		self.ft.findTextInWholePage("疾病史")
		self.driver.keyevent("4")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_check_detail")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_health_status_edit")
		self.ft.findTextInWholePage("疾病史")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_back")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_check_detail")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_health_status_edit")
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
	def clickExpertMedic(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		self.ft.findTextInWholePage("找專家")
		self.ck.clickByString("找專家")
		#self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/et_search_keyword")
		self.ck.clickByString("醫護人員")
		self.ck.clickByString(" 快速搜尋 ")
		self.ft.findTextInWholePage("選擇專家條件")
		#self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_quick_search")
		#self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_select_all")
		self.ck.clickByString(" 全部選取 ")
		#self.ck.clickByResourceID(self.apkVersionIdName+"/tv_select_all")
		sleep(2)
		self.ck.clickByString("完成") #搜尋結束後，回到專家搜尋頁面
		self.ft.findTextInWholePage("醫護人員")
		#self.ck.clickByResourceID(self.apkVersionIdName+"/tv_submit")
		#self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_sex")
		#self.ck.clickByResourceID(self.apkVersionIdName+"/tv_submit")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/lin_content")#等待搜尋結果
		self.ck.clickByResourceID(self.apkVersionIdName+"/lav_favorite")
		sleep(1)
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_expert_name")
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_expert_subject") #進到專家頁面後，查看是否有出現專家科別，判斷跳轉頁面成功
		self.ft.findTextInWholePage("性別")
		self.ft.findTextInWholePage("關鍵字")
		self.ft.findTextInWholePage("專長")
		self.ft.findTextInWholePage("語言")
		self.ft.findTextInWholePage("問答次數")
		self.ft.findTextInWholePage("經歷")
		self.ft.findTextInWholePage("專家認證")
		self.driver.keyevent("4")
		self.ft.findTextInWholePage(" 快速搜尋 ")
		#self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/tv_quick_search")
		self.driver.keyevent("4")
	def editEmergencyPerson(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",4)
		sleep(1)
		self.ft.findTextInWholePage("急難卡")
		self.ck.clickByString("急難卡")
		self.ft.findTextInWholePage("＋新增緊急聯絡人")
		sleep(1)
		self.ck.clickByString("＋新增緊急聯絡人")
		self.ft.findTextInWholePage("緊急聯絡人")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_name")
		self.ft.findTextInWholePage("關係")
		self.ck.clickByString("聯絡人")
		sleep(1)
		self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/tv_emergency_contact_edit")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_emergency_contact_edit")
		self.ft.findItemByIdInWholePage(self.apkVersionIdName+"/iv_delete")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_delete")
		sleep(1)
		self.ft.findTextInWholePage("瀏覽")
		self.ck.clickByString("瀏覽")

		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
		self.driver.keyevent("4")
		sleep(5)	
	def helthInfo(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",4)
		sleep(1)
		self.ft.findTextInWholePage("健康資訊")
		self.ck.clickByString("健康資訊")
		self.ft.findTextInWholePage("個人資訊")
		self.ck.clickByString("個人資訊")
		self.ft.findTextInWholePage("基本資料")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_edit")
		sleep(1)
		self.ck.clickByString("編輯")
		self.ft.findTextInWholePage("相簿")
		self.ck.clickByResourceID(self.apkVersionIdName+"/order")
		self.ck.clickByString("確認")
		sleep(10)
		newName = str(random.randint(1,1000))+" test name"
		targetName = self.driver.find_element_by_id(self.apkVersionIdName+"/et_name")
		"""targetName = self.driver.find_element_by_id(self.apkVersionIdName+"/et_name")
		defaultName = targetName.get_attribute("text")
		print("Name !!!!!!", defaultName)
		sleep(3)
		
		print("new name ", newName)
		self.ec.enterSelectByTextviewText(newName, defaultName)
		"""
		#print (len(targetName.get_attribute("text")))
		#self.ck.clickByResourceID(self.apkVersionIdName+"/tv_edit")
		#self.ck.clickByResourceID(self.apkVersionIdName+"/et_name")
		#for _ in range(len(targetName.get_attribute("text"))):
		#	self.driver.keyevent("67")
		#targetName.send_keys(newName)

		#self.ec.enter(newName, self.apkVersionIdName+"/et_name")
		# 寫到更改姓名


		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
		sleep(5)		

"""
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!")
"""


























