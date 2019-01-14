#!/usr/bin/python
# -*- coding: utf-8 -*-

import  sys
#sys.path.appent('C:/Python27/Lib/site-packages')

import os
import unittest
from appium import webdriver
from Script import script


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WacareLoginTest(unittest.TestCase):
    def setUp(self):  #針對TestCase必須自行定義的function, 在測試前會執行
        desired_caps = {} # Appium收到http Request後會解析這個key-value pair
        """key可以參考 https://github.com/DoctorQ/appium/blob/master/docs/en/writing-running-appium/caps.md""" 
        app = ('D:/Desktop/testAppium/proWaCare-googlePlay-alpha-v1.0.0.13.apk') #利用絕對路徑去找到要測試的APK
        desired_caps['app'] = app
        desired_caps['platformName'] = 'Android' #定義測試的系統環境
        desired_caps['platformVersion'] = '5.1.1' #定義版本
        desired_caps['deviceName'] = 'Android Emulator' #定義裝置名稱
        """目前還不知道為什麼使用下面的方法去找apk 會無法做登入"""
        #desired_caps['appPackage'] = 'com.lavidatec.wacare' #要測試的App package名稱
        #desired_caps['appActivity'] = '.com.lavidatec.wacare.Login.LoginMainActivity' #要執行的APK名稱
        desired_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)#隱式等待

    def tearDown(self): #針對TestCase必須自行定義的function, 在測試後會執行
        self.driver.quit()

    def test(self):       
        test = script(self.driver)
        #test.testThree()
        #test.testOne()
        test.testAddEmotion()
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WacareLoginTest)  
    # lodTestsFromTestCase會傳入一個unittest.TestCase物件-> WacareLoginTest
    # 並回傳一個 <class 'unittest.suite.TestSuite>
    unittest.TextTestRunner(verbosity=0).run(suite)
    # verbosity 参数可以控制输出的错误报告的详细程度，只有3个取值：
    #0 (quiet): 只显示执行的用例的总数和全局的执行结果。
    #1 (default): 默认值，显示执行的用例的总数和全局的执行结果，并对每个用例的执行结果（成功T或失败F）有个标注。
    #2 (verbose): 显示执行的用例的总数和全局的执行结果，并输出每个用例的详细的执行结果。

