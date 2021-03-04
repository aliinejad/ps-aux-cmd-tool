import os
import os.path
from os import path

proc_dir = "/proc"
for i in os.listdir(proc_dir):
	if i.isdigit():
		current_dir = "/proc/" + i
		for j in os.listdir(current_dir):
			detail = []	
			detail.append(i)
			if path.exists(current_dir + "/cmdline"): 
				f = open(current_dir + "/cmdline")
				cmdline = f.readlines()
				for index in range (len(cmdline)):
					detail.append(cmdline[index])
		for d in os.listdir(current_dir + "/fd"):
			if d.isdigit():
				detail.append(os.readlink(current_dir + "/fd/" + d))
		print('PID      command       openFiles')
		flag = 0
		for b in detail: 
			if  flag <= 1 :
				if flag == 0:
					print('{:05}    '.format(int(b)), end ="")
				else:
					print('{}    '.format(b), end ="")

				flag +=1
			else:
				print()
				print(len('                      '.format(detail[0][0:10],detail[1][0:10]))*' '+b, end ="")

		print("\n")
		print("------------------------------------------------------------")
