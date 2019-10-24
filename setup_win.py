#!/usr/bin/python3
# File name   : motor.py
# Description : Control Motors
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2018/10/12

import os
import time

for x in range(1,4):
	if os.system("pip3 install -U pip") == 0:
		break

for x in range(1,4):
	if os.system("pip3 install numpy") == 0:
		break

for x in range(1,4):
	if os.system("pip3 install opencv-contrib-python") == 0:
		break

for x in range(1,4):
	if os.system("pip3 install imutils zmq pybase64 psutil") == 0:   ####
		break
