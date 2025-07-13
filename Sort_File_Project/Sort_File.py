import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

#tkinter
root = tk.Tk()
root.withdraw()
file_path = filedialog.askdirectory(title="Select a folder!")
print(type(file_path))

#Luu tru

Rfile = open("suffix.txt","r+")
suffix = [i.strip() for i in Rfile.readlines()]
lst_name = os.listdir(file_path)
suffix_folder = []
for i in lst_name:
	if (Path(i).suffix == "") and (i[0] == '.'):
		suffix_folder.append(i)
print(suffix_folder)

#Ham tim phan mo rong cua file

def findend():
	store = []
	for i in lst_name:
		store.append(Path(i).suffix)
	return store

#Ham xoa cac phan tu trung lap trong danh sach cac phan mo rong

def remove_repeat():
	store = []
	for i in findend():
		if (i not in store) and (i!=''):
			store.append(i)
	return store

#Ham ghi file

def wrt():
	with open("suffix.txt","w+") as writefile:
		for i in range (0,len(remove_repeat())):
			if i<len(remove_repeat())-1:
				writefile.writelines(str(remove_repeat()[i])+"\n")
			else:
				writefile.writelines(str(remove_repeat()[i]))
wrt()

#Ham tao thu muc moi

def create_new():
	for i in remove_repeat():
		if (i not in suffix) or (i not in suffix_folder) and (i != ''):
			os.chdir(file_path)
			os.mkdir(str(i))
			with open("suffix.txt","w+") as w:
				w.writelines(str(i))
create_new()

#Ham di chuyen file

def movefile():
	for i in lst_name:
		if Path(i).suffix != '':
			path = os.path.join(file_path,i)
			snfx = Path(i).suffix
			newdirect = os.path.join(file_path,snfx,i)
			shutil.move(path,newdirect)
movefile()

