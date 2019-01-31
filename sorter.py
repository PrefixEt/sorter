#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import re

class Sorter():
	def __init__(self, arg = ""):
		self.COMMON_LOG_ADR = arg #address log
		print(self.COMMON_LOG_ADR)
		self.FILE_FOLDER = ''
		self.ADDRESSES_DICT = {}; 
		self.FILE_LEN = 0

	def __file_read(self):

		if self.COMMON_LOG_ADR:
			with open(self.COMMON_LOG_ADR, 'r') as file_strings:
				for file_string in file_strings:
					self.FILE_LEN =+ 1 
					yield file_string
			
	def __file_write(self, string):
		date_time = ''
		pass
	
	def __file_sorter(self):
		pass
	
	def sorted(self):
		print(self.__file_read())
		print(str(self.FILE_LEN))




if __name__ == '__main__':
	app = Sorter('access_log')
	app.sorted()

