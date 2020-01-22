# -*- encoding=utf8 -*-

print('hello')

import sys,getopt

opts, args = getopt.getopt(sys.argv[1:], "s:",
["help", "src=", "dst=", "major=", "version=", "platform=", "channels="])

for option in opts:
	print(option)
