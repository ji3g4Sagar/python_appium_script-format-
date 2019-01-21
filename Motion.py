#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os

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
			os.system("pause")
			x1 = self.screenWidth * xStart    
			y1 = self.screenHeight * yStart  
			y2 = self.screenHeight * yEnd  
			for i in range(n):
				os.system("pause")
				print("x1: ", x1, " y1: ", y1, "y2: ", y2)
				self.driver.swipe(x1, y1, x1, y2, t)
		except:
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
class click():
	def __init__(self, driver):
		try:
			self.driver = driver
		except:
			print("ClickAndTap init error!!\n")

	def clickByResourceID(self, resource_id):
		try:
			target = self.driver.find_element_by_id(resource_id)
			#self.driver.implicitly_wait(time = 3)
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
class waittingFor():
	def __init__(self, driver):
		self.driver = driver

	def implicitWait(self, time = 5):
		self.driver.implicitly_wait(time)

	def explicitWaitByResourceID(self, resource_id, index = -1, time = 30, freuency = 1): #利用index 來判斷是否要找尋特定元素是否存在
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
			locator = self.driver.find_elements_by_id(resource_id)
			target = locator[index]
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
			print("Successfully find the target text %s \n" % targetText)
			if (mode==0):
				return target
			else:
				return True

	#def findSpecificItemByResourceID(self, targetID, mode =0):

			


# 目前已知選擇器 
	#  - find_element_by_accessibility_id
	#  id - find_element(s)_by_id
	#  class - find_element(s)_by_class_name
	#  name - find_element(s)_by_name
		
	   