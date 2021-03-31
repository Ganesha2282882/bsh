# BSH code
# BSH is a simplistic shell.

import os
import sys
import subprocess

def getargs(cmd):
	output = cmd.split(" ")
	del output[0]
	return output

while True:
	cmd = input("% ")
	cmd = cmd.split(" ")

	if "echo" == cmd[0]:
		cmd = " ".join(cmd)
		print(" ".join(getargs(cmd)))

	elif "cd" == cmd[0]:
		cmd = " ".join(cmd)
		os.chdir(" ".join(getargs(cmd)))

	elif "exit" == cmd[0]:
		sys.exit()

	else:
		subprocess.call(cmd.split(" "))
