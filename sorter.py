#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#author github..com/prefixet
import sys
import os
import re

class Sorter():
    def __init__(self, address = ""):
        self.__COMMON_LOG_ADR = address #address log
        self.__DESTRIBUTOR_DICT = {}
        self.__FILE_FOLDER = os.path.join(os.path.dirname(__file__), 'logs')
        self.__location = lambda x: os.path.join(self.__FILE_FOLDER, str(x) + '.log')
        self.__re_pattern = r'(([0-9])|([0-2][0-9])|([3][0-1]))\/(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\/\d{4}'

    def __file_read(self):
        if self.__COMMON_LOG_ADR:
            with open(self.__COMMON_LOG_ADR, 'r') as file_strings:
                for file_string in file_strings:
                    yield file_string

    def __file_write(self, date, data):
        file_address = self.__DESTRIBUTOR_DICT.setdefault(date, self.__location(date))
        with open(file_address, 'a') as file:
            file.write(data)
        print('write ' + data[:18] + '... in ' + file_address[-21:])

    def __file_sorter(self):
        for data_line in self.__file_read():
            date = re.search(self.__re_pattern, data_line)
            if date:
                date = date.group(0)
                date = date.replace('/', '-')
                self.__file_write(date, data_line)

    def sorted(self):
        if not os.path.isdir(self.__FILE_FOLDER):
            os.mkdir(self.__FILE_FOLDER)
        self.__file_sorter()


if __name__ == '__main__':
    app = Sorter(sys.argv[1])
    app.sorted()




