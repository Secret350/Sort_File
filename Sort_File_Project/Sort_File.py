import os
import shutil
from pathlib import Path

#Luu tru
Rfile = open("suffix.txt","r+")
lst = os.listdir(r"E:\Python\Python_Project\Sort_File_Project\Downloads")


def findend():
	store = []
	for i in lst:
		store.append(Path(i).suffix)
	return store

def create():

#def crt():

