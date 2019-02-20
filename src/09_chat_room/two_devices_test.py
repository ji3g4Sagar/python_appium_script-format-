#coding=utf-8
from appium import webdriver
import time
import threading
import multiprocessing as mp
import unittest
from chatroomScript import script
from apkVersionAndCellConfig import Config
from multiprocessSharingList import SharingListGetAndSet

apkName="qaExternalWaCare-v1.0.3.1.5.apk"
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
desired_caps2['deviceName'] = '127.0.0.1:62026' #定義裝置名稱
desired_caps2['automationName'] = 'uiautomator2'
desired_caps2['noReset'] = 'true'




class WaCareTest1(unittest.TestCase):
	def setUp(self):
		#configfile = Config(apkName = "proWaCare-v1.0.1.4.apk")# For 正式站
		configfile = Config(apkName = "qaExternalWaCare-v1.0.3.1.5.apk", desired_caps_outer=desired_caps, port="4723")
		self.driver = configfile.getDriver()
		self.driver.implicitly_wait(10)#隱式等待
		self.apkVersionIdName = configfile.getApkVersionIdName()
		

	def tearDown(self):
		self.driver.quit()

	def test(self):
		test = script(self.driver, self.apkVersionIdName)
		test.sendMessage(msg = "發送測試訊息")
class WaCareTest2(unittest.TestCase):
	def setUp(self):
		#configfile = Config(apkName = "proWaCare-v1.0.1.4.apk")# For 正式站
		configfile = Config(apkName = "qaExternalWaCare-v1.0.3.1.5.apk", desired_caps_outer=desired_caps2, port="4725")
		self.driver = configfile.getDriver()
		self.driver.implicitly_wait(10)#隱式等待
		self.apkVersionIdName = configfile.getApkVersionIdName()

	def tearDown(self):
		self.driver.quit()

	def test(self):
		test = script(self.driver, self.apkVersionIdName)
		test.receiveMessage(sender="test999")

def task1(l):
	l.acquire()
	#Wa1 = WaCareTest1(sharinglist)
	suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest1)
	unittest.TextTestRunner(verbosity=0).run(suite)
	l.release()
 
def task2(l):
	l.acquire()
	#Wa2 = WaCareTest2(sharinglist)
	suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest2)
	unittest.TextTestRunner(verbosity=0).run(suite)
	l.release()


if __name__ == '__main__':
	multiprocess = []
	manager = mp.Manager()
	sharinglist= manager.list()
	lock = mp.Lock()
	p1 = mp.Process(target=task1, args=(lock,))
	multiprocess.append(p1)
	p2 = mp.Process(target=task2, args=(lock,))
	multiprocess.append(p2)	

	#for p in multiprocess:
	#	p.start()
	
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	
	#for t in threads:
	#	t.start()
	









"""
threads = []
t1 = threading.Thread(target=task1)
threads.append(t1)
 
t2 = threading.Thread(target=task2)
threads.append(t2)
"""
