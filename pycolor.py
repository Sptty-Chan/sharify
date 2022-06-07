"""
_________________________________________
* Author: Sptty Chan
* Github: https://github.com/Sptty-Chan
* Facebook:
  • Sptty Chan
  • Fanda X Chan
  • Muhammad Zian Ramadhan
_________________________________________


* Example 1
_________________________________________
from pycolor import printer

printer("<hijau>Hello <ungu>Word")
printer("Nama Saya <kuning>Sptty Chan")
_________________________________________


* Example 2
_________________________________________
from pycolor import colorise

var = colorise("<biru>Hello <merah>Word")
print(var)
_________________________________________


* Color List
_________________________________________
<hijau>       = hijau
<biru>        = biru
<ungu>        = ungu
<kuning>      = kuning
<biru_muda>   = biru muda
<merah>       = merah
<putih>       = putih
_________________________________________
"""

import os,re

# COLOR DICT
colors = {"putih":"\x1b[0;37m","merah":"\x1b[0;31m","hijau":"\x1b[0;32m","kuning":"\x1b[0;33m","biru":"\x1b[0;34m","ungu":"\x1b[0;35m","biru_muda":"\x1b[0;36m","-n":"\n","-r":"\r","-/":'"',"-!":"'","--":r"\x".replace("x","")}

def colorise(value): # TEXT TO COLOR
	finder = re.findall("<(.*?)>",str(value))
	if len(finder)<1:
		return colors["putih"]+str(value)
	else:
		text_list = []
		for color_item in finder:
			if color_item not in colors:
				continue
			else:
				if len(text_list)<1:
					text_list.insert(0,value.replace(f"<{color_item}>",colors[color_item]))
				else:
					text_list.insert(0,text_list[0].replace(f"<{color_item}>",colors[color_item]))
		if len(text_list)<1:
			return colors["putih"]+str(value)
		else:
			return colors["putih"]+text_list[0]

def printer(value): # PRINTER TEXT WITH COLOR
	text_color = colorise(value)
	return print(text_color)

def cleaner(): # CLEAR TERMINAL
	os.system("clear")
