import os
import time
import sys

from os import system
from time import sleep
from sys import exit

# Instal termux-api otomatis
print("\033[32mInstalling\033[0m")
system("pkg install termux-api")
print("\033[32mSuccesfull\033[0m")
sleep(1)
system("clear")

def banner():
	print("""\033[32m
 ██████╗ ██████╗ ███████╗███╗   ██╗      ██╗    ██╗██████╗
██╔═══██╗██╔══██╗██╔════╝████╗  ██║      ██║    ██║██╔══██╗
██║   ██║██████╔╝█████╗  ██╔██╗ ██║█████╗██║ █╗ ██║██████╔╝
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║╚════╝██║███╗██║██╔══██╗
╚██████╔╝██║     ███████╗██║ ╚████║      ╚███╔███╔╝██████╔╝
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝       ╚══╝╚══╝ ╚═════╝\033[0m
\033[41m Website Opener from Terminal \033[0m\n""")
banner()

try:
	url = input("\033[32mEnter the site URL \033[0m: ")
	if url == "":
		print("\033[31mMalah dikosongi\033[0m")
		exit()

	sleep(1)
	print("\033[32mWait a moment!\033[0m")
	system("termux-open "+url)

except KeyboardInterrupt:
	print("\033[31mMalah di CTRL + C\033[0m")

except EOFError:
	print("\033[31mMalah keluar\033[0m")
