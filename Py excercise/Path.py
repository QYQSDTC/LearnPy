'''
Author: Yiqian Qian
Description: Lear how does path work.
Date: 2020-10-13 19:24:47
LastEditors: Yiqian Qian
LastEditTime: 2020-10-13 19:28:21
FilePath: /undefined/Users/qyq/Development/LearnPy/Py excercise/Path.py
'''
from os import path
filepath = path.join(path.dirname(__file__),"resources")
print(filepath)