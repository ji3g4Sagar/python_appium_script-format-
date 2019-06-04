 #!/usr/bin/python
# -*- coding: utf-8 -*-
"""
.. module:: Motion
	:synopsis: A module for all basic motion (ex: swipe)

.. moduleauthor:: Sagar


"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class swipePage():
	def __init__(self, driver):
		try:
			self.driver = driver
			self.screenWidth = driver.get_window_size()['width']
			self.screenHeight = driver.get_window_size()['height']
		except:
			print("Swipe page init error!\n") 

	def swipeUp(self, t=400, n=1, xStart=0.5, yStart=0.75, yEnd=0.3):
		"""這個函數會模擬手指向下滑動的操作

			* Args:
				1. t **(int)** :預設值為400ms, 用來決定這個滑動所花費的時間
				2. n **(int)** :預設值為1, 用來決定這個滑動的次數
				3. xStart **(int)** :預設值為0.5, 表示起始滑動點為Ｘ軸的一半（0.5), 範圍為0.1 ~ 1
				4. yStart **(int)** :預設值為0.75, 表示起始滑動點為Y軸的0.75處開始, 範圍為0.1 ~ 1
				5. yEnd **(int)** :預設值為0.3, 滑動結束點為Ｙ軸的0.3處, 範圍為0.1 ~ 1
			
			* 回傳值: 
				None.
		>>> swipeUp()
		"""
		try:
			sleep(1)
			x1 = self.screenWidth * xStart    
			y1 = self.screenHeight * yStart  
			y2 = self.screenHeight * yEnd  
			for i in range(n):
				sleep(1)
				self.driver.swipe(x1, y1, x1, y2, t)
		except():
			print("SwipeUp error!!\n") 
	def swipeDown(self, t=400, n=1, xStart=0.5, yStart=0.3, yEnd=0.75):
		"""這個函數會模擬手指向下滑動的操作

			* Args:
				1. t **(int)** :預設值為400ms, 用來決定這個滑動所花費的時間
				2. n **(int)** :預設值為1, 用來決定這個滑動的次數
				3. xStart **(int)** :預設值為0.5, 表示起始滑動點為Ｘ軸的一半（0.5), 範圍為0.1 ~ 1
				4. yStart **(int)** :預設值為0.3, 表示起始滑動點為Y軸的0.75處開始, 範圍為0.1 ~ 1
				5. yEnd **(int)** :預設值為0.75, 滑動結束點為Ｙ軸的0.3處, 範圍為0.1 ~ 1

		    * 回傳值: 
				None.
		>>> swipeDown()
		"""
		try:
			x1 = self.screenWidth * xStart       
			y1 = self.screenHeight * yStart     
			y2 = self.screenHeight * yEnd      
			for i in range(n):
				self.driver.swipe(x1, y1, x1, y2,t)
		except:
			print("SwipeDown error!!\n") 
	def swipeLeft(self, t=400, n=1, yStart=0.5, xStart=0.8, xEnd=0.05):
		"""這個函數會模擬手指向下滑動的操作

			* Args:
				1. t **(int)** :預設值為400ms, 用來決定這個滑動所花費的時間
				2. n **(int)** :預設值為1, 用來決定這個滑動的次數
				3. yStart **(int)** :預設值為0.5, 表示起始滑動點為Y軸的0.5處開始, 範圍為0.1 ~ 1
				4. xStart **(int)** :預設值為0.8, 表示起始滑動點為Ｘ軸的0.8處, 範圍為0.1 ~ 1
				5. xEnd **(int)** :預設值為0.05, 滑動結束點為X軸的0.05處, 範圍為0.1 ~ 1

			* 回傳值:
				None.
		>>> swipeLeft()
		"""
		try:
			x1 = self.screenWidth * xStart
			y1 = self.screenHeight * yStart
			x2 = self.screenWidth * xEnd
			for i in range(n):
				self.driver.swipe(x1, y1, x2, y1, t)
		except:
			print("SwipeLeft error!!\n") 
	def swipeRight(self, t=400, n=1, yStart=0.5, xStart=0.1, xEnd=0.75):
		"""這個函數會模擬手指向下滑動的操作

			* Args:
				1. t **(int)** :預設值為400ms, 用來決定這個滑動所花費的時間
				2. n **(int)** :預設值為1, 用來決定這個滑動的次數
				3. yStart **(int)** :預設值為0.5, 表示起始滑動為Ｙ軸的0,5處開始, 範圍為0.1 ~ 1
				4. xStart **(int)** :預設值為0.1, 表示起始滑動為Ｘ軸的0.1處開始, 範圍為0.1 ~ 1
				5. xEnd **(int)** :預設值為0.75, 表示滑動結束為Ｘ軸的0.75處, 範圍為0.1 ~ 1

			* 回傳值：
				None.
		>>> swipeRight()
		"""
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
		"""這個函數會依據傳入的元件id以及字串，將字串輸入指定的元件中

			* Args:
				1. context **(str)** :要輸入的文字內容
				2. resource_id **(str)** : 要選擇做輸入的元素id

			* 回傳值: 
				None.
		>>> enter("我是要輸入的文字", "我是元素id")
		
		"""
		try:
			testfiled = self.driver.find_element_by_id(resource_id)
		except:
			print("[Enter string]Can not find the target %s" % resource_id) 
		else:
			testfiled.set_text(context)

	def enterSelectByTextviewText(self, context, textviewText): 
		"""利用Textview上預設顯示的文字當作為選擇依據,選擇到元件做輸入

			* Args:
				1. context **(str)** :要輸入的文字內容
				2. textviewText **(str)** :Textview預設的文字內容

			* 回傳值：
				None.
		>>> enterSelectByTextviewText("我是要輸入的文字", "我是Textview上預設文字")
		"""
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
		"""利用手機元件的id來點擊特定元件

			* Args: 
				1. resource_id **(str)** : 要被點擊的元件id

			* 回傳值：
				None.
		>>> clickByResourceID("要點擊的元件id")
		"""
		try:
			target = self.driver.find_element_by_id(resource_id)
		except:
			print("[click]Can not find the target %s " % resource_id) 
		else:
			target.click()
	
	def clickByString(self, targetString):
		"""點擊含有特定文字的元件

			* Args:
				1. targetString **(str)** : 被點擊的元件上所包含的文字內容
			
			* 回傳值：
				None.
		>>> clickByString("要點擊的元件上含有的文字")
		"""
		try:
			string = '//*[@text=\'{}\']'.format(targetString)
			target = self.driver.find_element_by_xpath(string)
		except:
			print("[click]Can not find the target %s " % targetString) 
		else:
			target.click()

	def clickFromManyThingsByResourceID(self, resources_id, index):
		"""點擊多個相同元件id中, 特定索引的元件

			* Args: 
				1. resources_id **(str)** : 要被點擊的元件id
				2. index **(int)** : 被點擊的元件索引, 索引值從0開始

			* 回傳值：
				None.
		>>> clickFromManyThingsByResourceID("要點擊的元件id", 1)
		"""
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
		"""讓程式暫停，等待特定時間

			* Args:
				1. time **(int)** : 等待的時間,以秒為單位,預設為5秒

			* 回傳值： 
				None.
		>>> implicitWait()			
		"""
		self.driver.implicitly_wait(time)

	def explicitWaitByResourceID(self, resource_id, index = -1, time = 30, freuency = 1):
		"""讓程式暫停，等待畫面上特定元件出現

			* Args:
				1. resource_id **(int)** : 要等待的特定元件id
				2. index **(int)** : 函數的模式設定，預設為-1
					+ -1：表示要等待的元件id為唯一
					+ 其他任意數字表示要等待的元件id有多個元件相同，數字表示要等待的元素索引值
				3. time **(int)** : 等待的時間，單位為秒，預設為30秒
				4. frequncy **(int)** : 檢查特定元素是否存在的頻率，單位為秒，預設為1秒
			
			* 回傳值：
				True: 有找到目標元件

				False: 找尋時間超時，無法尋找到指定元件
		>>> explicitWaitByResourceID("要等待的元件ID")
		"""
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
			locator = self.driver.find_elements_by_id(resource_id)# 選取全部擁有相同ID的元素
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

	def search4Toast(self, toastMessage, mode=0):
		"""找尋特定文字的Toast訊息

			* Args: 
				1. toastMessage **(str)** : 要找尋的Toast顯示的文字內容

			* 回傳值：
				None.
		>>> search4Tost("Toast的訊息")
		"""
		try:
			message = '//*[@text=\'{}\']'.format(toastMessage)
			target = self.driver.find_element_by_xpath(message)
			wait = WebDriverWait(self.driver, 30)
			element = wait.until(EC.invisibility_of_element_located(target))
		except:
			print("Toast does not exist!!!" )
			if(mode == 1):	
				return False	
		else:
			print("FInd toast!!!!")
			if(mode == 1):
				return True
class findSpecificText():
	def __init__(self, driver):
		self.driver = driver
	def findText(self, targetText, mode = 0): 
		"""透過文字找尋特定元件是否存在

			* Args: 
				1. targetText **(str)** : 所有找尋的文字內容
				2. mode **(int)** : 用來決定這個函數的回傳值，預設為0
					+ 0：回傳值為找尋到的元件driver **物件**
					+ 1：
						True：有找到指定元件

						False：沒有找到指定元件

			* 回傳值
				driver物件 或 True/False
		>>> findText("被找尋的元件包含的文字")
		"""
		sleep(1)
		try:
			message = '//*[@text=\'{}\']'.format(targetText)
			target = self.driver.find_element_by_xpath(message)
		except:
			print("[findSpecificText]Can not locate target text [%s] \n" % targetText)
			if(mode==1):
				return False
		else:
			print("Successfully find the target text [%s] \n" % targetText)
			if (mode==0):
				return target
			else:
				return True

	def findSpecificItemByResourceID(self, targetID, mode=0, index=-1):
		"""利用元件id找尋特定物件

			* Args:
				1. targetId **(str)** :要找尋的目標物件id
				2. mode **(int)** :決定這個函數的回傳值，預設為0
					+ 0：回傳值為找尋到的元件driver物件
					+ 1：回傳值為True/False
				3. index **(int)** :用以表示找尋的物件是否唯一，預設為-1
					+ -1：要等待的元件id為唯一
					+ 其他任意數字表示要等待的元件id有多個相同元件, 數字表示要找尋的元素索引值

			* 回傳值：
				driver物件 或 True/False
		>>> findSpecificItemByResourceID("要找尋的元件id")
		"""
		if(index==-1):
			try:
				target = self.driver.find_element_by_id(targetID)
			except:
				print("[findSpecificItemByResourceID]Can not locate!")
				if(mode==1):
					return False
			else:
				print("Successfully find the target with sourceID %s \n" % targetID)
				if(mode == 0):
					return target
				else:
					return True
		else:
			try:
				targets = self.driver.find_elements_by_id(targetID)
			except:
				print("[findSpecificItemByResourceID]Can not locate!")
				if(mode == 1):
					return False
			else:
				print("Successfully find the target with sourceID %s \n" % targetID)
				if(mode == 0):
					return target[index]
				else:
					return True
	def findTextInWholePage(self, targetText, mode=0):
		sleep(1)
		"""在整個頁面中找尋含有特定文字的元件 

			* Args：
				1. targetText **(str)** :要找尋的元件包含的文字

			* 回傳值：
				None.
		>>>	findTextInWholePage("要找尋的元件上的文字")	
		"""
		targetFind = False
		sp = swipePage(self.driver)
		time = 0 
		while(targetFind != True):
			if(time == 3):
				targetFind = True
				sp.swipeDown(n=3)
				if(mode == 1):
					return False
			elif(self.findText(targetText, mode = 1)):
				targetFind = True
				if(mode == 1):
					return True
			else:
				sp.swipeUp()
				time = time +1
		sleep(1)

	def findItemByIdInWholePage(self, sourde_id):
		"""在整個頁面中找尋含有特定元件id的元件 

			* Args：
				1. sourde_id **(str)** :要找尋的元件的id

			* 回傳值：
				None.
		>>>	findItemByIdInWholePage("要找尋的元件的id")	
		"""
		targetFind = False
		sp = swipePage(self.driver)
		time = 0 
		while(targetFind!=True):
			if(time == 3 ):
				targetFind = True
				sp.swipeDown(n=3)
			elif(self.findSpecificItemByResourceID(sourde_id, mode = 1)):
				targetFind=True
				return self.findSpecificItemByResourceID(sourde_id)
			else:
				sp.swipeUp()
				time = time +1	
		sleep(1)			
class getXYLocation():
	def __init__(self, driver):
		try:
			self.driver = driver
		except:
			print("[getXYLocation] Init error!!\n")
	
	def getXYByResourceID(self, resource_id, index=-1):
		"""透過元件id取得特定的元件Ｘ、Ｙ座標

			* Args：
				1. resource_id **(srt)** :目標元件id

			* 回傳值：
				元件的座標
		>>> getXYByResourceID("元件id")
		"""
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
			self.ft = findSpecificText(driver)
		except:
			print("[checkForStartPage] Init error!\n")
	def goBackToHomePage(self):
		sleep(3)
		"""呼叫於每次操作前，返回動態牆畫面使用
			1.檢查畫面最下方的home tab是否存在
			2.利用tap進到動態牆頁面
			3.檢查畫面中是否出現Notification元件,用以確認是否返回動態牆最上方

			* Args：
				None.

			* 回傳值：
				None.
		>>> goBackToHomePage()
		"""
		self.ft.findSpecificItemByResourceID(self.apkVersionIdName+ "/home_tab_icon")
		#self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/home_tab_icon")
		#target = self.driver.find_elements_by_id(self.apkVersionIdName+ "/home_tab_icon")
		#sleep(2)
		#self.ck.tap(target[0])
		#self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 0)
		self.ck.clickByResourceID(self.apkVersionIdName+"/home_tab_icon")
		findNotification = False
		while (findNotification == False):
			#if(self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/home_notification", time=2, freuency=1)):
			if(self.ft.findSpecificItemByResourceID(self.apkVersionIdName+"/home_notification", mode =1)):
				findNotification = True
			else:
				self.sp.swipeDown(n=3)
		print("Successuflly go back to dynaamic wall!!\n")
class getContext():
	def __init__(self, driver):
		try:
			self.driver = driver
		except:
			print("Init error!!\n")
	def context(self):
		return self.driver.page_source

	   




























