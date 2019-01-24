#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor, findSpecificText, getXYLocation, homePage
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
		self.apkVersionIdName = apkVersionIdName
		self.hp = homePage(driver, apkVersionIdName)

	#def sendMessage(self, sharingList, msg = "", sendMessageTarget="王媽"):
	def sendMessage(self, msg = "", sendMessageTarget="王媽"):
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.hp.goBackToHomePage()
		targets = self.driver.find_elements_by_id(self.apkVersionIdName+"/home_tab_icon")
		self.ck.tap(targets[1])
		findSpecificPerson = False

		while (findSpecificPerson ==False):
			if(self.ft.findText(sendMessageTarget,mode=1)):
				findSpecificPerson = True
			else:
				self.sp.swipeUp()
		self.ck.clickByString(sendMessageTarget)
		sleep(2)
		self.ck.clickByString("關懷")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/family_chatroom_back_page")
		self.ck.clickByString("回覆...")
		if(len(msg)==0):
			message = str(random.randint(1,100))+ " test message"
		else:
			message = msg
		#sharingList.append(message)
		self.ec.enter(message, self.apkVersionIdName+"/familyChatRoomMessage")
		self.ck.clickByResourceID(self.apkVersionIdName+"/familyChatRoomSend")
		sleep(3)
		self.ft.findText(message)
		self.driver.keyevent("4")
		self.driver.keyevent("4")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)

	#def receiveMessage(self, sender, sharingList):
	def receiveMessage(self, sender):
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.hp.goBackToHomePage()
		targets = self.driver.find_elements_by_id(self.apkVersionIdName+"/home_tab_icon")
		self.ck.tap(targets[3])
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/fra_toolbar")
		self.ck.clickByString(sender)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/family_chatroom_back_page")
		receivedMsg = "發送測試訊息"
		if(self.ft.findText(receivedMsg, mode=1)):
			print("Successfully received message [%s]" %receivedMsg)
		else:
			print("Did not receive the message [%s]" %receivedMsg)
		sleep(2)
		self.driver.keyevent("4")


		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")		









"""
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
"""



