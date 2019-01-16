#!/usr/bin/python
# -*- coding: utf-8 -*-

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class swipePage():
	def __init__(self, driver):
		self.driver = driver
		self.screenWidth = driver.get_window_size()['width']
		self.screenHeight = driver.get_window_size()['height']
	def swipeUp(self, t=250, n=1):
		x1 = self.screenWidth * 0.5    
		y1 = self.screenHeight * 0.75   
		y2 = self.screenHeight * 0.1   
		for i in range(n):
			self.driver.swipe(x1, y1, x1, y2, t)
	def swipeDown(self, t=250, n=1):
		x1 = self.screenWidth * 0.5         
		y1 = self.screenHeight * 0.1       
		y2 = self.screenHeight * 0.75        
		for i in range(n):
			self.driver.swipe(x1, y1, x1, y2,t)
	def swipLeft(self, t=300, n=1):
		x1 = self.screenWidth * 0.8
		y1 = self.screenHeight * 0.5
		x2 = self.screenWidth * 0.05
		for i in range(n):
			self.driver.swipe(x1, y1, x2, y1, t)
	def swipRight(self, t=250, n=1):
		l = driver.get_window_size()
		x1 = self.screenWidth * 0.1
		y1 = self.screenHeight * 0.5
		x2 = self.screenWidth * 0.75
		for i in range(n):  
			self.driver.swipe(x1, y1, x2, y1, t)    

class enterContext():
	def __init__(self, driver):
		self.driver = driver
	def enter(self, context, resource_id):
		#testfiled = self.driver.find_elements_by_class_name("android.widget.EditText")
		testfiled = self.driver.find_element_by_id(resource_id)
		#testfiled.send_keys(context)
		testfiled.set_text(context)

class clickAndTap():
	def __init__(self, driver):
		self.driver = driver

	def tap(self, target):
		self.driver.tap(target)

	def click(self, resource_id):
		try:
			target = self.driver.find_element_by_id(resource_id)
			self.driver.implicitly_wait(3)
		except:
			print("[click]Can not find the target %s " % resource_id)
		else:
			target.click()

	def clickFromManyThings(self, resources_id, index):
		try:
			targets = self.driver.find_elements_by_id(resources_id)
		except:
			print("[clickFromManyThings]Cant not find the target %s" % resources_id)
		else:
			targets[index].click()


class waittingFor():
	def __init__(self, driver):
		self.driver = driver

	def implicitWait(self):
		self.driver.implicitly_wait(5)

	def explicitWait(self, resource_id, index = -1): #利用index 來判斷是否要找尋特定元素是否存在
		if index == -1:
			try:
				wait = WebDriverWait(self.driver, 30)
				element = wait.until(EC.presence_of_element_located((By.ID, resource_id)))
			except:
				print("Time out!!! Element %s does not exist" % resource_id )
		else:
			locator = self.driver.find_elements_by_id(resource_id)
			target = locator[index]
			try:
				wait = WebDriverWait(self.driver, 30)
				element = waait.until(EC.presence_of_element_located(target))
			except:
				print("Time out!!!! Element %s does not exist!!!" % resource_id)


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





# 目前已知選擇器 
		#  - find_element_by_accessibility_id
		#  id - find_element(s)_by_id
		#  class - find_element(s)_by_class_name
		#  name - find_element(s)_by_name
		#el = self.driver.find_element_by_accessibility_id("Add Contact")
		#el.click()
	   