#!/usr/bin/python
# -*- coding: utf-8 -*-

#import multiprocessing as mp 

class SharingListGetAndSet():
	def __init__(self):
		self.sharingList = list()

	def sharingListSetter(self, sharingListOuter):
		self.sharingList = sharingListOuter

	def sharingListGetter(self):
		return self.sharingList

	
