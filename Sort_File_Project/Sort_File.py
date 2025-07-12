import os
import shutil
from pathlib import Path

#Luu tru
direct = r"E:\Python\Python_Project\Sort_File_Project\Downloads"
Rfile = open("suffix.txt","r+")
suffix = [i.strip() for i in Rfile.readlines()]
lst_name = os.listdir(r"E:\Python\Python_Project\Sort_File_Project\Downloads")

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
		if (i not in suffix) and (i != ''):
			os.chdir(r"E:\Python\Python_Project\Sort_File_Project\Downloads")
			os.mkdir(str(i))
			with open("suffix.txt","w+") as w:
				w.writelines(str(i))
create_new()

#Ham di chuyen file

def movefile():
	for i in lst_name:
		if Path(i).suffix != '':
			path = os.path.join(direct,i)
			snfx = Path(i).suffix
			newdirect = os.path.join(direct,snfx,i)
			shutil.move(path,newdirect)
movefile()

