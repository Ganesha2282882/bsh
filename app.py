#!/usr/bin/env python
# BSH code
# BSH is a simplistic shell.

import os
import sys

def getargs(cmd):
	output = cmd.split(" ")
	del output[0]
	return output

while True:
	cmd = input("% ")
	if "echo " in cmd:
		print(" ".join(getargs(cmd)))

	elif "cd " in cmd:
		os.chdir(" ".join(getargs(cmd)))

	elif "exit" in cmd:
		sys.exit()

	else:
		os.system(cmd)
