#!/usr/bin/env python3
#_*_ coding: utf8 _*_

leds_patters = {
				0:"#### ## ## ####",
				1:"#  #  #  #  #  ",
				2:"###  #####  ###",
				3:"###  ####  ####",
				4:"# ## ####  #  #",
				5:"####  ###  ####",
				6:"####  #### ####",
				7:"###  #  #  #  #",
				8:"#### ##### ####",
				9:"#### ####  ####"}

def led_number_drawer(number_led):
	counter = 0
	counter2 = 3
	lista = []

	for i in number_led:
		for o in range(5):
			print(leds_patters[int(i)][counter:counter2])		
			counter+=3
			counter2+=3
		counter=0
		counter2=3