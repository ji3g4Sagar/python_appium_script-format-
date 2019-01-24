#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import os
import sys

class swipePage():
	def __init__(self, driver):
		try:
			self.driver = driver
			self.screenWidth = driver.get_window_size()['width']
			self.screenHeight = driver.get_window_size()['height']
		except:
			prin("Swipe page init error!\n")

	def swipeUp(self, t=400, n=1, xStart=0.5, yStart=0.75, yEnd=0.3):
		try:
			sleep(1)
			x1 = self.screenWidth * xStart    
			y1 = self.screenHeight * yStart  
			y2 = self.screenHeight * yEnd  
			for i in range(n):
				sleep(1)
				self.driver.swipe(x1, y1, x1, y2, t)
		except():
			#a, b, c = sys.exc_info()
			#print(a)
			print("SwipeUp error!!\n")
	def swipeDown(self, t=400, n=1, xStart=0.5, yStart=0.3, yEnd=0.75):
		try:
			x1 = self.screenWidth * xStart       
			y1 = self.screenHeight * yStart     
			y2 = self.screenHeight * yEnd      
			for i in range(n):
				self.driver.swipe(x1, y1, x1, y2,t)
		except:
			print("SwipeDown error!!\n")
	def swipLeft(self, t=400, n=1, yStart=0.5, xStart=0.8, xEnd=0.05):
		try:
			x1 = self.screenWidth * xStart
			y1 = self.screenHeight * yStart
			x2 = self.screenWidth * xEnd
			for i in range(n):
				self.driver.swipe(x1, y1, x2, y1, t)
		except:
			print("SwipeLeft error!!\n")
	def swipRight(self, t=400, n=1, yStart=0.5, xStart=0.1, xEnd=0.75):
		try:
			x1 = self.screenWidth * xStart
			y1 = self.screenHeight * yStart
			x2 = self.screenWidth * xEnd
			for i in range(n):  
				self.driver.swipe(x1, y1, x2, y1, t)    
		except:
			print("SwipeRight error!!\n")
class enterContext():
	def __init__(self, driver):
		try:
			self.driver = driver
		except:
			print("EnterContext init error!!\n")

	def enter(self, context, resource_id):
		try:
			testfiled = self.driver.find_element_by_id(resource_id)
		except:
			print("[Enter string]Can not find the target %s" % resource_id)
		else:
			testfiled.set_text(context)
			
	def enterSelectByTextviewText(self, context, textviewText): #利用Textview預設文字選擇
		try:
			message = '//*[@text=\'{}\']'.format(textviewText)
			target = self.driver.find_element_by_xpath(message)
		except:
			print("[enterSelectByTextviewText] Selecting target  %s can not be locate!" % textviewText)
		else:
			target.send_keys(context)		

class click():
	def __init__(self, driver):
		try:
			self.driver = driver
		except:
			print("Click init error!!\n")

	def clickByResourceID(self, resource_id):
		try:
			target = self.driver.find_element_by_id(resource_id)
		except:
			print("[click]Can not find the target %s " % resource_id)
		else:
			target.click()
	
	def clickByString(self, targetString):
		try:
			string = '//*[@text=\'{}\']'.format(targetString)
			target = self.driver.find_element_by_xpath(string)
		except:
			print("[click]Can not find the target %s " % targetString)
		else:
			target.click()

	def clickFromManyThingsByResourceID(self, resources_id, index):
		try:
			targets = self.driver.find_elements_by_id(resources_id)
		except:
			print("[clickFromManyThings]Cant not find the target %s" % resources_id)
		else:
			targets[index].click()

	def tap(self, driver):
		actions = TouchAction(self.driver)
		actions.tap(driver)
		actions.perform()
class waittingFor():
	def __init__(self, driver):
		self.driver = driver

	def implicitWait(self, time = 5):
		self.driver.implicitly_wait(time)

	def explicitWaitByResourceID(self, resource_id, index = -1, time = 30, freuency = 1):
		#利用index 來判斷是否要從多個相同resourceID的元素中找尋特定元素
		sleep(3)
		if index == -1:
			try:
				wait = WebDriverWait(self.driver, timeout = time, poll_frequency = freuency)
				element = wait.until(EC.presence_of_element_located((By.ID, resource_id)))
			except:
				print("Time out!!! Element %s does not exist" % resource_id)
				sleep(3)
				return False
			else:
				print("The element waitting for %s appear!" % resource_id)
				sleep(3)
				return True
		else:
			locator = self.driver.find_elements_by_id(resource_id)# 抓取全部擁有相同ID的元素
			target = locator[index]#利用index 辨別要選取的
			try:
				wait = WebDriverWait(self.driver, timeout = time, poll_frequency = freuency)
				element = wait.until(EC.presence_of_element_located(target))
			except:
				print("Time out!!!! Element %s does not exist!!!" % resource_id)
				sleep(3)
				return False
			else:
				print("The element waitting for %s appear!" % resource_id)
				sleep(3)
				return False

	def explicitWaitByTargetString(self, targetString):# 怪怪的!待修!
		self.implicitWait()
		try:
			string = '//*[@text=\'{}\']'.format(targetString)
			target = self.driver.find_element_by_xpath(string)
		except:
			print("Can not locate element %s" % targetString)
		else:
			try:
				sleep(1)
				wait = WebDriverWait(self.driver, timeout = 30, poll_frequency = 1)
				element = wait.until(EC.presence_of_element_located(target))
			except:
				print("Time out!!! Element %s does not exist!!" % targetString)
			else:
				sleep(3)
class getToast():
	def __init__(self, driver):
		self.driver = driver

	def search4Toast(self, toastMessage):
		#print (target.text)
		try:
			message = '//*[@text=\'{}\']'.format(toastMessage)
			target = self.driver.find_element_by_xpath(message)
			wait = WebDriverWait(self.driver, 30)
			element = wait.until(EC.invisibility_of_element_located(target))
		except:
			print("Toast does not exist!!!" )
		else:
			print("FInd toast!!!!")
class findSpecificText():
	def __init__(self, driver):
		self.driver = driver
	def findText(self, targetText, mode = 0): 
		# Mode 0 for return object instance
		# Mode 1 for return True/Flase
		try:
			message = '//*[@text=\'{}\']'.format(targetText)
			target = self.driver.find_element_by_xpath(message)
		except:
			print("[findSpecificText]Can not locate target text %s \n" % targetText)
			if(mode==1):
				return False
		else:
			print("Successfully find the target text [%s] \n" % targetText)
			if (mode==0):
				return target
			else:
				return True

	def findSpecificItemByResourceID(self, targetID, mode=0, index=-1):
		if(index==-1):
			try:
				target = self.driver.find_element_by_id(targetID)
			except:
				print("[findSpecificItemByResourceID]Can not locate!")
				if(mode==1):
					return False
			else:
				print("Successfully find the target with sourceID %s \n" % targetID)
				if(mode==0):
					return target
				else:
					return True
		else:
			try:
				targets = self.driver.find_elements_by_id(targetID)
			except:
				print("[findSpecificItemByResourceID]Can not locate!")
				if(mode==1):
					return False
			else:
				print("Successfully find the target with sourceID %s \n" % targetID)
				if(mode==0):
					return target[index]
				else:
					return True
class getXYLocation():
	def __init__(self, driver):
		try:
			self.driver = driver
		except:
			print("[getXYLocation] Init error!!\n")
	
	def getXYByResourceID(self, resource_id, index=-1):
		if(index==-1):
			return (self.driver.find_element_by_id(resource_id).location)
		else:
			target = self.driver.find_elements_by_id(resource_id)
			return (target[index].location)
class homePage():
	def __init__(self, driver, apkVersionIdName):
		try: 
			self.driver = driver
			self.apkVersionIdName = apkVersionIdName
			self.wf = waittingFor(driver)
			self.ck = click(driver)
			self.sp = swipePage(driver)
		except:
			print("[checkForStartPage] Init error!\n")
	def goBackToHomePage(self):
		# 呼叫於每次操作前，返回動態牆畫面使用
		"""
			1.檢查畫面最下方的home tab是否存在
			2.利用tap進到動態牆頁面
			3.檢查畫面中是否出現Notification元件,用以確認是否返回動態牆最上方
		"""
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/home_tab_icon")
		target = self.driver.find_elements_by_id(self.apkVersionIdName+ "/home_tab_icon")
		self.ck.tap(target[0])
		findNotification = False
		while (findNotification == False):
			if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/home_notification", time=2, freuency=1)):
				findNotification = True
			else:
				self.sp.swipeDown()
		print("Successuflly go back to dynaamic wall!!\n")



			


# 目前已知選擇器 
	#  - find_element_by_accessibility_id
	#  id - find_element(s)_by_id
	#  class - find_element(s)_by_class_name
	#  name - find_element(s)_by_name
		 
	   