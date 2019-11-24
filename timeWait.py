# -*- encoding=utf8 -*-
__author__ = "bowen"

import time, datetime


'''
等待到指定时间
'''
def timeWait(timeWait):
	print(timeWait)
	timeArray = time.strptime(timeWait, "%Y-%m-%d %H:%M:%S")
	print(timeArray)
	timeStamp = int(time.mktime(timeArray))

	while(True):
		timeNow = time.time()
		if (timeNow >= timeStamp):#判断当前时间是否到达指定时间
			print('time now')#到达指定时间
			break;
		else:
			print('wait more')#未到达时间

# 等待到指定时间停止
timeWait('2019-11-24 16:18:00');
