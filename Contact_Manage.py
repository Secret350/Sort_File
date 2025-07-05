import sys

#File

RfileP = open("Contact-Phone_number.txt", "r+")
RfileE = open("Contact-Email.txt", "r+")
RfileN = open("Contact-Name.txt","r+")

#Luu tru
namequan = [str(i) for i in RfileN.readlines()]
mailquan = [str(i) for i in RfileE.readlines()]
phonequan = [ int(i) for i in RfileP.readlines()]
phonein = [i for i in range (0,len(phonequan))]
namedic = dict(zip(phonequan,phonein))

#Ham chon phuong thuc

def method():
	mthd = input("Choose the method you want: DELETE | SHOW | SHOWALL | OUT\n").upper()
	return mthd

#Ham hien thi toan bo so dien thoai lien he

def show_all():
	for p in range (0,len(phonequan)):
		print("0" + str(phonequan[p]) + ": " + str(namequan[p]).strip())

#Ham nhap so dien thoai lien he

def num():
	key = str(input("Please enter the phone number!\n"))
	return key

#Ham them dia chi vao danh ba

def add(phonenum):
	newcontact_name = str(input("Please enter new contact's name: "))
	newcontact_phone = phonenum
	newcontact_email = str(input("Please enter new contact's email: "))
	if len(namedic) == 0:
		namedic[int(newcontact_phone)] = 0
		RfileP.write(str(newcontact_phone))
		RfileE.write(str(newcontact_email))
		RfileN.write(str(newcontact_name))
	else:
		namedic[int(newcontact_phone)] = len(namedic.values())
		RfileP.write("\n" + str(newcontact_phone))
		RfileE.write("\n" + str(newcontact_email))
		RfileN.write("\n" + str(newcontact_name))

class contact:
	def __init__(self,name,phonenumber,email):
		self.name = name
		self.phonenumber = phonenumber
		self.email = email

	# Ham hien thi thong tin lien he

	def show_info(self):
		print(f"The contact's infomation:\nName: {self.name}Phone_Number: {self.phonenumber}\nEmail: {self.email}")
#Ham xoa dia chi lien he

def delete(phonenum):
	RfileN.seek(0)
	names = RfileN.readlines()
	RfileE.seek(0)
	emails = RfileE.readlines()
	RfileP.seek(0)
	numbers = RfileP.readlines()

	#strip(): xoa \n


	try:
		id = [n.strip() for n in numbers].index(phonenum)
	except ValueError:
		print("Phone number not found!")
		return

	del names[id]
	del numbers[id]
	del emails[id]

	with open("Contact-Name.txt",'w') as n:
		n.writelines(names)
	with open("Contact-Email.txt", "w") as e:
		e.writelines(emails)
	with open("Contact-Phone_number.txt", "w") as p:
		p.write(str(numbers[0].strip()))
		p.writelines("\n" + str(numbers[n].strip()) for n in range(1,len(numbers)))

#Cac thao tac

phonenum = num()

if int(phonenum) not in phonequan:
	print("This is newphone number do you want to add new?\n")
	ans = input("Yes/EnterAgain/End").upper()
	if ans == "YES":
		add(phonenum)
	elif ans == "ENTERAGAIN":
		phonenum = num()
	else:
		sys.exit()

#Chon chuc nang

RfileN.seek(0)
nameread = RfileN.readlines()
RfileE.seek(0)
mailread = RfileE.readlines()
cont = contact(nameread[namedic[int(phonenum)]],phonenum,mailread[namedic[int(phonenum)]])

mthd = method()

if mthd == "DELETE":
	delete(phonenum)
elif mthd == "SHOW":
	cont.show_info()
elif mthd == "OUT":
	sys.exit()
elif mthd == "SHOWALL":
	show_all()
else:
	print("Please try again!")
	mthd = method()