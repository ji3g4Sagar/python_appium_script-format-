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
		sleep(3)
		self.ft.findTextInWholePage("親友健康")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/iv_userPic",0)
		self.ft.findTextInWholePage("新增健康燈")
		self.ck.clickByString("相簿")
		self.ft.findTextInWholePage("健康動態")
		self.ck.clickByString("＋新增相簿")
		self.ft.findTextInWholePage("設定相簿")
		self.albumName = str(random.randint(1,1000))+" testing album"
		self.ec.enter(self.albumName, self.apkVersionIdName + "/albumName")
		self.ck.clickByString("完成")
		self.ft.findTextInWholePage("健康動態")
		self.ck.clickByString(self.albumName)
		self.ft.findTextInWholePage("分享")
		self.ck.clickByResourceID(self.apkVersionIdName+"/familyPhotoAlbumHistoryAdd")
		self.ft.findTextInWholePage("相簿")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/order",0)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/order",1)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/order",2)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/order",3)
		self.ck.clickByString("確認")
		self.ft.findTextInWholePage("分享")
		self.ck.clickByResourceID(self.apkVersionIdName+"/familyPhotoAlbumHistorySetting")
		self.ck.clickByString("刪除")
		self.ft.findTextInWholePage("提醒")
		self.ck.clickByString("刪除")
		self.gt.search4Toast("刪除完成")
		sleep(4)

