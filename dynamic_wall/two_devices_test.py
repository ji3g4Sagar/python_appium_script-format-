
#coding=utf-8

from appium import webdriver
import time
import threading
import unittest
from dynamicWallScript import script
from apkVersionAndCellConfig import Config

apkName="qaExternalWaCare-v1.0.3.1.2.apk"
desired_caps = {} # Appium收到http Request後會解析這個key-value pair
app = ('http://35.194.192.102:5000/getfile?filename='+apkName)
desired_caps['app'] = app
desired_caps['platformName'] = 'Android' #定義測試的系統環境
desired_caps['platformVersion'] = '5.1.1' #定義版本
desired_caps['deviceName'] = '127.0.0.1:62001' #定義裝置名稱
desired_caps['automationName'] = 'uiautomator2'
desired_caps['noReset'] = 'true'
 
desired_caps2 = {} # Appium收到http Request後會解析這個key-value pair
app = ('http://35.194.192.102:5000/getfile?filename='+apkName)
desired_caps2['app'] = app
desired_caps2['platformName'] = 'Android' #定義測試的系統環境
desired_caps2['platformVersion'] = '5.1.1' #定義版本
desired_caps2['deviceName'] = '127.0.0.1:62027' #定義裝置名稱
desired_caps2['automationName'] = 'uiautomator2'
desired_caps2['noReset'] = 'true'

class WaCareTest1(unittest.TestCase):
	def setUp(self):
		#configfile = Config(apkName = "proWaCare-v1.0.1.4.apk")# For 正式站
		configfile = Config(apkName = "qaExternalWaCare-v1.0.3.1.3.apk", desired_caps_outer=desired_caps, port="4723")
		self.driver = configfile.getDriver()
		self.driver.implicitly_wait(10)#隱式等待
		self.apkVersionIdName = configfile.getApkVersionIdName()

	def tearDown(self):
		self.driver.quit()

	def test(self):
		test = script(self.driver, self.apkVersionIdName)
		#test.checkForDynamicWall()
		#test.swipeAroundInDynamicWall()
		test.hiFiveCheck()
		#test.deleteFriendOfHiFive()
		#test.checkForAlbum()
		#test.deleteFriendOfAlbum()

class WaCareTest2(unittest.TestCase):
	def setUp(self):
		#configfile = Config(apkName = "proWaCare-v1.0.1.4.apk")# For 正式站
		configfile = Config(apkName = "qaExternalWaCare-v1.0.3.1.3.apk", desired_caps_outer=desired_caps2, port="4725")
		self.driver = configfile.getDriver()
		self.driver.implicitly_wait(10)#隱式等待
		self.apkVersionIdName = configfile.getApkVersionIdName()

	def tearDown(self):
		self.driver.quit()

	def test(self):
		test = script(self.driver, self.apkVersionIdName)
		test.checkForDynamicWall()
		#test.swipeAroundInDynamicWall()
		#test.hiFiveCheck()
		#test.deleteFriendOfHiFive()
		#test.checkForAlbum()
		#test.deleteFriendOfAlbum()
 


def task1():
	suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest1)
	unittest.TextTestRunner(verbosity=0).run(suite)
 
def task2():
	suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest2)
	unittest.TextTestRunner(verbosity=0).run(suite)

 
threads = []
t1 = threading.Thread(target=task1)
threads.append(t1)
 
t2 = threading.Thread(target=task2)
threads.append(t2)
 
if __name__ == '__main__':
	for t in threads:
		t.start()