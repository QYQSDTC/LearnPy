'''
Author: Yiqian Qian
Description: Lear how does path work.
Date: 2020-10-13 19:24:47
LastEditors: Yiqian Qian
LastEditTime: 2020-10-13 19:46:53
FilePath: /undefined/Users/qyq/Development/LearnPy/Py excercise/Path.py
'''
from os import path
filepath1 = path.dirname(__file__)
print(f"dirname is:{filepath1}")

filepath2 = path.realpath(__file__)
print("real path is:{}".format(filepath2))