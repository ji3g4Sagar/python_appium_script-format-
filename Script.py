#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import logging
from Motion import swipePage, enterContext, clickAndTap, waittingFor

class script():
	logging.basicConfig(filename=__name__+'.log',format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level = logging.ERROR)
	def __init__(self, driver):
		self.driver = driver
		self.SP = swipePage(driver)
		self.EC = enterContext(driver)
		self.CT = clickAndTap(driver)
		self.WF = waittingFor(driver)

		#下面是出log用的
		self.logger = logging.getLogger('sagar_log') #自訂義 log的名稱
		self.logger.setLevel(logging.INFO) #定義log的等級
		self.handler = logging.FileHandler('Script.log', 'a')  

		self.handler.setLevel(logging.DEBUG)
		self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')
		self.handler.setFormatter(self.formatter)
		self.logger.addHandler(self.handler)

	def basicMotion(self):
		#利用顯式等待, 判斷app是否正常開啟, 利用起始畫面的特定元素是否存在 
		#self.WF.explicitWait("com.lavidatec.wacare:id/animationJson")
		sleep(4)
		self.SP.swipLeft(n=3)	
	def find_Toast(self,message,timeout=5,poll_frequency = 0.5):  #xpath查找toast值
		
		#logging.info("獲取toast值---'%s'" %message)
		try:
			message = '//*[@text=\'{}\']'.format(message)
			#toast_loc = ("xpath",".//*[contains(@text,'%s')]" %message)
			#WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(toast_loc))
			WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_xpath(message))
			
			#logging.info("查找到toast--'%s'"%message)
			self.logger.info("Find toast!!\n")
			return True
		except:
			#logging.info("未查找到toast--'%s'"%message)
			self.logger.info("Not find toast")
			return False
	"""def find_Toast2(self,message):  #查找toast值
		
		#self.logger.info(" find toast value---'%s'" %(message))
		try:
			#message = '//*[@text=\'{}\']'.format(message)
			WebDriverWait(self.driver,5,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,message)))
			self.logger.info("find toast!!")
			#self.logger.info("查找到toast----%s"%message)
			return True
		except:
			self.logger.info("Not find toast!!")
			#self.logger.info("未查找到toast----%s"%message)
			return False"""
	def testOne(self): #正常登陸
		self.basicMotion()
		self.CT.click("com.lavidatec.wacare:id/teachCloseLayout")
		self.EC.enter("0931540341","com.lavidatec.wacare:id/et_phone_num")
		self.EC.enter("ji3g4wj6", "com.lavidatec.wacare:id/et_login_pass")
		self.CT.click("com.lavidatec.wacare:id/tv_login")
		"""利用顯式等待等登入後的頁面(動態牆)出現"""
		self.WF.explicitWait("com.lavidatec.wacare:id/home_tab_icon")

	def testTwo(self):#更改國籍
		self.basicMotion()
		self.CT.click("com.lavidatec.wacare:id/teachCloseLayout")
		self.EC.enter("0931540331","com.lavidatec.wacare:id/et_phone_num")
		self.EC.enter("ji3g4wj6", "com.lavidatec.wacare:id/et_login_pass")
		self.CT.click("com.lavidatec.wacare:id/linear_flag_border")
		self.CT.click("com.lavidatec.wacare:id/textView_countryName")
		self.CT.click("com.lavidatec.wacare:id/tv_login")      
	def testThree(self):#帳號密碼錯誤
		self.basicMotion()
		self.CT.click("com.lavidatec.wacare:id/teachCloseLayout")

		self.EC.enter("0931540341","com.lavidatec.wacare:id/et_phone_num")
		self.EC.enter("ji3g4555", "com.lavidatec.wacare:id/et_login_pass")
		self.CT.click("com.lavidatec.wacare:id/tv_login")
		self.find_Toast2("輸入帳號或密碼有誤")
	def testFour(self):#密碼不足六位
		self.basicMotion()
		self.CT.click("com.lavidatec.wacare:id/teachCloseLayout")
		self.EC.enter("0931540331","com.lavidatec.wacare:id/et_phone_num")
		self.EC.enter("ji", "com.lavidatec.wacare:id/et_login_pass")
		self.CT.click("com.lavidatec.wacare:id/tv_login")
	def testFive(self):#手機不曾註冊
		self.basicMotion()
		self.CT.click("com.lavidatec.wacare:id/teachCloseLayout")
		self.EC.enter("0931540331","com.lavidatec.wacare:id/et_phone_num")
		self.EC.enter("ji3g4w6", "com.lavidatec.wacare:id/et_login_pass")
		self.CT.click("com.lavidatec.wacare:id/tv_login")
	def testAddEmotion(self):
		self.basicMotion()
		self.CT.click("com.lavidatec.wacare:id/teachCloseLayout")
		self.EC.enter("0931540341","com.lavidatec.wacare:id/et_phone_num")
		self.EC.enter("ji3g4wj6", "com.lavidatec.wacare:id/et_login_pass")
		self.CT.click("com.lavidatec.wacare:id/tv_login")
		self.WF.explicitWait("com.lavidatec.wacare:id/home_tab_icon")
		self.CT.clickFromManyThings("com.lavidatec.wacare:id/home_tab_icon", 1)
		self.WF.explicitWait("com.lavidatec.wacare:id/tv_status_level")
		self.CT.clickFromManyThings("com.lavidatec.wacare:id/tv_status_level", 1)
		self.WF.explicitWait("com.lavidatec.wacare:id/iv_next")
		self.CT.clickFromManyThings("com.lavidatec.wacare:id/iv_next", 1)
		self.WF.explicitWait("com.lavidatec.wacare:id/addEmotion")
		self.CT.click("com.lavidatec.wacare:id/addEmotion")
		self.WF.explicitWait("com.lavidatec.wacare:id/faceImage4")
		self.CT.click("com.lavidatec.wacare:id/faceImage4")
		self.EC.enter("心情還不錯", "com.lavidatec.wacare:id/emotionContent")
		self.CT.click("com.lavidatec.wacare:id/myEmotionPostText")
		self.WF.explicitWait("com.lavidatec.wacare:id/addEmotion")
		sleep(5)






