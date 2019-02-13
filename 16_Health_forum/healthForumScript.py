#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import *
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver import Remote #for keyevent
import random



class scriptForHelthForum_1_1():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.gt = getToast(driver)
		self.xy = getXYLocation(driver)
		self.hp = homePage(driver, apkVersionIdName)
		self.apkVersionIdName = apkVersionIdName
	def starter(self):
		self.clickCurrentTopic()
		self.swipeInTopicPage()
		self.backBtn()
		self.checkArticle()
	def clickCurrentTopic(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_ask")
		self.driver.keyevent("4")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		self.wf.implicitWait(time=3)
	def swipeInTopicPage(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.sp.swipeUp(n=2)
		self.sp.swipeDown(n=2)
		self.sp.swipeUp(n=2)
		self.sp.swipeDown(n=2)
		self.sp.swipeDown(n=2)
		self.sp.swipeUp(n=2)
		self.sp.swipeDown(n=2)
		self.sp.swipeDown(n=2)
		self.sp.swipeUp(n=2)
		self.sp.swipeUp(n=2)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def backBtn(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.driver.keyevent("4")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")	
		sleep(5)
	def checkArticle(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_more")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_themeDetailClose")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_themeDetailClose")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_ask")
		self.driver.keyevent("4")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)

class scriptForHelthForum_1_2():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.gt = getToast(driver)
		self.ft = findSpecificText(driver)
		self.xy = getXYLocation(driver)
		self.hp = homePage(driver, apkVersionIdName)
		self.apkVersionIdName = apkVersionIdName
	def starter(self):
		#self.Question()
		#self.QuestionAnonymous()
		#self.QuestionNonAnonymous()
		#self.EditQuestion()
		#self.DeleteQuestion()
		#self.ReplaySelfQuestion()
		#self.QuestionWithPicture()
		self.QuestionWithTakePhoto()
		#self.DeleteReplayMessage()
	def Question(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		#self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.ck.clickByString("老人獨居")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_ask")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_ask")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_healthForumPostClose")
		self.ck.clickByResourceID(self.apkVersionIdName + "/ed_healthForumPostArticleTitle")
		title = "我是標題"
		self.ec.enter(title, self.apkVersionIdName + "/ed_healthForumPostArticleTitle")
		questionText = str(random.randint(1,1000))
		self.ec.enterSelectByTextviewText(questionText+"Question", "請將您的問題描述詳細，專家能更精準的為您解答...")
		self.ck.clickByResourceID(self.apkVersionIdName + "/cb_healthForumPostAnonymous")
		self.ck.clickByResourceID(self.apkVersionIdName + "/cb_healthForumPostAnonymous")
		self.ck.clickByResourceID(self.apkVersionIdName + "/cb_healthForumPostLottery")
		self.ck.clickByResourceID(self.apkVersionIdName + "/cb_healthForumPostLottery")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_healthForumPostUpload")
		self.gt.search4Toast("上傳完成")
		self.driver.keyevent("4")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)		
	def QuestionAnonymous(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		#self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.ck.clickByString("老人獨居")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_ask")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_ask")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_healthForumPostClose")
		self.ck.clickByResourceID(self.apkVersionIdName + "/ed_healthForumPostArticleTitle")
		title = "我是標題(匿名上傳測試)"
		self.ec.enter(title, self.apkVersionIdName + "/ed_healthForumPostArticleTitle")
		self.ck.clickByString("請將您的問題描述詳細，專家能更精準的為您解答...")
		questionText = str(random.randint(1,1000))
		self.ec.enterSelectByTextviewText(questionText+"Question", "請將您的問題描述詳細，專家能更精準的為您解答...")
		self.ck.clickByResourceID(self.apkVersionIdName + "/cb_healthForumPostAnonymous")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_healthForumPostUpload")
		self.gt.search4Toast("上傳完成")
		self.driver.keyevent("4")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def QuestionNonAnonymous(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		#self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.ck.clickByString("老人獨居")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_ask")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_ask")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_healthForumPostClose")
		self.ck.clickByResourceID(self.apkVersionIdName + "/ed_healthForumPostArticleTitle")
		title = "我是標題(非匿名上傳測試)"
		self.ec.enter(title, self.apkVersionIdName + "/ed_healthForumPostArticleTitle")
		self.ck.clickByString("請將您的問題描述詳細，專家能更精準的為您解答...")
		questionText = str(random.randint(1,1000))
		self.ec.enterSelectByTextviewText(questionText+"Question", "請將您的問題描述詳細，專家能更精準的為您解答...")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_healthForumPostUpload")
		self.gt.search4Toast("上傳完成")
		self.driver.keyevent("4")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def EditQuestion(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		#self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.ck.clickByString("老人獨居")
		self.ft.findTextInWholePage("test999")
		self.ck.clickByString("test999")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_forumQuestionDot")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_forumQuestionDot")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/connect_device")
		self.ck.clickByString("編輯")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_healthForumPostUpload")
		target = self.driver.find_element_by_id(self.apkVersionIdName + "/ed_healthForumPostEditor")
		T = target.find_element_by_class_name("android.widget.EditText")
		for i in range(len(T.text)):
			self.driver.keyevent("67")
		T.send_keys("String after edited")
		self.ck.clickByString("上傳")
		self.gt.search4Toast("上傳完成")
		#下面利用子元素選擇的方法選擇imagebutton
		self.driver.keyevent("4")
		returnBtn = self.driver.find_element_by_id(self.apkVersionIdName + "/toolbar")
		RBtn = returnBtn.find_element_by_class_name("android.widget.ImageButton")
		RBtn.click()
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def DeleteQuestion(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		#self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.ft.findTextInWholePage("老人獨居")
		self.ck.clickByString("老人獨居")
		self.ft.findTextInWholePage("test999")
		self.ck.clickByString("test999")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_forumQuestionDot")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_forumQuestionDot")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/connect_device")
		self.ck.clickByString("刪除")
		self.driver.keyevent("4")
		self.driver.keyevent("4")
		self.driver.keyevent("4")		
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def ReplaySelfQuestion(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		#self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.ck.clickByString("老人獨居")
		sleep(2)
		self.ft.findTextInWholePage("WaCare016")
		self.ck.clickByString("WaCare016")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_forumQuestionBack")
		self.ck.clickByString("回應...")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/cb_forumQuestionAnn")
		replyNum = random.randint(1,1000)
		self.ec.enterSelectByTextviewText(str(replyNum), "回應...")
		#self.ck.clickByString("匿名")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_forumQuestionSend")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_forumQuestionBack")
		self.ft.findTextInWholePage(str(replyNum))
		self.driver.keyevent("4")
		self.driver.keyevent("4")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def DeleteReplayMessage(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		#self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.ck.clickByString("老人獨居")
		self.ft.findTextInWholePage("test999")
		self.ck.clickByString("test999")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_forumQuestionBack")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_forumQuestionDot")
		self.ck.clickByString("刪除")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
		sleep(5)
	def QuestionWithPicture(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/et_search_keyword")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_forumTopicTitle")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/tv_ask")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_ask")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/iv_healthForumPostAlbum")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_healthForumPostAlbum")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/upload_photo")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/order", 0)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/order", 1)
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/order", 2)
		self.ck.clickByResourceID(self.apkVersionIdName+"/upload_photo")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/iv_healthForumPostItemPhoto")
		title = "我是標題"
		self.ec.enter(title, self.apkVersionIdName + "/ed_healthForumPostArticleTitle")
		questionText = str(random.randint(1,1000))
		self.ec.enterSelectByTextviewText(questionText+"Question", "請將您的問題描述詳細，專家能更精準的為您解答...")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_healthForumPostUpload")
		self.gt.search4Toast("上傳完成")
		self.driver.keyevent("4")
		sleep(5)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
	def QuestionWithTakePhoto(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/et_search_keyword")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_forumTopicTitle")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/tv_ask")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_ask")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/iv_healthForumPostAlbum")
		self.ck.clickByResourceID(self.apkVersionIdName+"/iv_healthForumPostAlbum")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/upload_photo")
		xpath = "//android.widget.TextView[@resource-id='"+ self.apkVersionIdName + "/order" + "']/parent::android.widget.FrameLayout/preceding-sibling::android.widget.ImageView"
		target = self.driver.find_element_by_xpath(xpath)
		target.click()
		self.driver.keyevent("27")
		self.wf.explicitWaitByResourceID("com.android.camera2:id/done_button")
		self.ck.clickByResourceID("com.android.camera2:id/done_button")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/iv_healthForumPostItemPhoto")
		title = "我是標題"
		self.ec.enter(title, self.apkVersionIdName + "/ed_healthForumPostArticleTitle")
		questionText = str(random.randint(1,1000))
		self.ec.enterSelectByTextviewText(questionText+"Question", "請將您的問題描述詳細，專家能更精準的為您解答...")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_healthForumPostUpload")
		self.gt.search4Toast("上傳完成")
		self.driver.keyevent("4")
		sleep(5)
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
	def AnswerOtherPost(self):
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName+"/home_tab_icon", 2)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/et_search_keyword")
		self.ck.clickByResourceID(self.apkVersionIdName+"/tv_forumTopicTitle")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName+"/tv_ask")

		
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")


"""
		self.hp.goBackToHomePage()
		print("-----Start test ", sys._getframe().f_code.co_name, "!!!------\n")
		print("-----Test for ", sys._getframe().f_code.co_name, " finish!!!!!!\n")
"""


























