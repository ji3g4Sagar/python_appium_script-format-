#!/usr/bin/python
# -*- coding: utf-8 -*-

from appium import webdriver
import os



class Config():
	def __init__(self, apkName="qaExternalWaCare-v1.0.4.1.6.apk", desired_caps_outer={}, port ="4723"):
		if (len(desired_caps_outer)==0):
			self.apkName = apkName
			desired_caps = {} # Appium收到http Request後會解析這個key-value pair
			app = ('http://35.194.192.102:5000/getfile?filename='+apkName)
			desired_caps['app'] = app
			desired_caps['platformName'] = 'Android' #定義測試的系統環境
			desired_caps['platformVersion'] = '8.0' #定義版本
			desired_caps['deviceName'] = 'TestDevices' #定義裝置名稱
			desired_caps['automationName'] = 'uiautomator2'
			desired_caps['noReset'] = 'true'
			self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		else:
			self.apkName = apkName
			appiumAddress = 'http://localhost:'+port+'/wd/hub'
			print(appiumAddress)
			self.driver = webdriver.Remote(appiumAddress, desired_caps_outer)



	def getDriver(self):
		return self.driver

	def getApkVersionIdName(self):
		if(self.apkName.startswith("qaExternalWaCare")):
			return ("com.lavidatec.wacareqaexternal:id")
		elif(self.apkName.startswith("qaExternalWaPro")):
			return ("com.lavidatec.waproqaexternal:id")
		elif(self.apkName.startswith("dev")):
			return ("com.lavidatec.wacaredev:id")
		elif(self.apkName.startswith("pre")):
			return ("com.lavidatec.wacareprealpha:id")


			

			


