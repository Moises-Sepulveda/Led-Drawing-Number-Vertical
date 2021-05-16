#!/usr/bin/env python3
#_*_ coding: utf8 _*_

import drawing
import platform
import os

if platform.system() == "Windows":
	os.system("cls")
	print(""" 
		=======================================
		     WELCOME TO LED DRAWING NUMBER
		=======================================
		""")
elif platform.system()=="Linux":
	os.system("clear")
	print(""" 
		=======================================
		     WELCOME TO LED DRAWING NUMBER
		=======================================
		""")
else:
	print(""" 
		=======================================
		     WELCOME TO LED DRAWING NUMBER
		=======================================
		""")

number_led = input ("Introduce the number that you want draw: ")

if __name__=="__main__":
	drawing.led_number_drawer(number_led)