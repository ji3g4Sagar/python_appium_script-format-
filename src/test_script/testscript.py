#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
from PIL import Image
import cv2
import numpy as np
import pytesseract
sys.path.append("..")
from Motion import *
#from logging import Log
from time import sleep
import time
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
		self.ft = findSpecificText(driver)
		self.apkVersionIdName = apkVersionIdName
		self.hp = homePage(driver, apkVersionIdName)
		self.gt = getToast(driver)

	def starter(self):
		self.tester()
	
	def tester(self):
		self.hp.goBackToHomePage()

		print("-----Test for "+sys._getframe().f_code.co_name+" start!!!!!!")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon",1)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("健康燈設定")
		self.ck.clickByString("相簿")
		self.ft.findTextInWholePage("健康動態")
		activity = self.driver.current_activity;
		print("Tpye: ", type(activity))
		print(activity)
		print("-----Test for "+sys._getframe().f_code.co_name+" finish!!!!!!")
		sleep(4)

