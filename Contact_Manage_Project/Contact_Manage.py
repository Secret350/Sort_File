import sys

#File

RfileP = open("Contact-Phone_number.txt", "r+")
RfileE = open("Contact-Email.txt", "r+")
RfileN = open("Contact-Name.txt","r+")

#Luu tru

namequan = [str(i).strip() for i in RfileN.readlines()]
mailquan = [str(i).strip() for i in RfileE.readlines()]
phonequan = [ int(i) for i in RfileP.readlines()]
phonein = [i for i in range (0,len(phonequan))]
namedic = dict(zip(phonequan,phonein))
meth = ["ADD", "DELETE", "SHOW", "SHOWALL", "OUT"]

#Ham refresh data

def refresh_data():
	global namequan, mailquan, phonequan, phonein, namedic
	with open('Contact-Name.txt', 'r') as fN, \
		 open('Contact-Email.txt', 'r') as fE, \
		 open('Contact-Phone_number.txt', 'r') as fP:
		namequan = [line.strip() for line in fN.readlines()]
		mailquan = [line.strip() for line in fE.readlines()]
		phonequan = [int(line.strip()) for line in fP.readlines()]
		phonein = list(range(len(phonequan)))
		namedic = dict(zip(phonequan, phonein))

#Ham chon phuong thuc

def method():
	mth = input("Choose the method you want: ADD | DELETE | SHOW | SHOWALL | OUT\n").upper()
	while mth not in meth:
		print("Please try again!")
		mth = input("Choose the method you want: ADD | DELETE | SHOW | SHOWALL | OUT\n").upper()
	return mth

#Ham hien thi toan bo so dien thoai lien he

def show_all():
	refresh_data()
	for p in range (0,len(phonequan)):
		print("0" + str(phonequan[p]) + " : " + str(namequan[p]).strip())
	main()
#Ham nhap so dien thoai lien he

def num():
	key = int(input("Please enter the phone number!\n"))
	while key not in phonequan:
		print("Phone number not found! To add new phone number, choose ADD.")
		main()
	return key

#Ham them dia chi vao danh ba

def add(anm):
	newcontact_name = str(input("Please enter new contact's name: "))
	newcontact_email = str(input("Please enter new contact's email: "))
	if len(namedic) == 0:
		namedic[int(anm)] = 0
		RfileP.write(str(anm))
		RfileE.write(str(newcontact_email))
		RfileN.write(str(newcontact_name))
	else:
		namedic[int(anm)] = len(namedic.values())
		RfileP.write("\n" + str(anm))
		RfileE.write("\n" + str(newcontact_email))
		RfileN.write("\n" + str(newcontact_name))
	refresh_data()
	main()

class contact:
	def __init__(self,name,phonenumber,email):
		self.name = name
		self.phonenumber = phonenumber
		self.email = email

	# Ham hien thi thong tin lien he

	def show_info(self):
		refresh_data()
		print(f"The contact's infomation:\nName: {self.name}\nPhone_Number: {self.phonenumber}\nEmail: {self.email}")
		main()

#Ham xoa dia chi lien he

def delete(nm):
	RfileN.seek(0)
	names = RfileN.readlines()
	RfileE.seek(0)
	emails = RfileE.readlines()
	RfileP.seek(0)
	numbers = RfileP.readlines()

	#strip(): xoa \n

	try:
		id = [n.strip() for n in numbers].index(nm)
	except ValueError:
		print("Phone number not found!")
		return

	del names[id]
	del numbers[id]
	del emails[id]

	with open("Contact-Name.txt",'w') as n:
		n.write(str(names[0].strip()))
		n.writelines("\n" + names[i].strip() for i in range (1,len(names)))
	with open("Contact-Email.txt", "w") as e:
		e.write(str(emails[0].strip()))
		e.writelines("\n" + emails[i].strip() for i in range (1,len(emails)))
	with open("Contact-Phone_number.txt", "w") as p:
		p.write(str(numbers[0].strip()))
		p.writelines("\n" + str(numbers[n].strip()) for n in range(1,len(numbers)))
	refresh_data()
	main()

#Ham nhap so dien thoai them vao

def addnum():
	addnm = str(input("Enter adding number: "))
	if int(addnm) in phonequan:
		print("This phone number is already in contact!")
		sys.exit()
	return addnm

#Chon chuc nang
def main():
	RfileN.seek(0)
	nameread = RfileN.readlines()
	RfileE.seek(0)
	mailread = RfileE.readlines()
	RfileP.seek(0)
	phoneread = RfileP.readlines()

	mthd = method()

	if mthd == "ADD":
		add(addnum())
	elif mthd == "DELETE":
		delete("0"+ str(num()))
	elif mthd == "SHOW":
		refresh_data()
		snm = num()
		cont = contact(nameread[namedic[int(snm)]].strip(), phoneread[namedic[int(snm)]].strip(), mailread[namedic[int(snm)]].strip())
		cont.show_info()
	elif mthd == "OUT":
		sys.exit()
	elif mthd == "SHOWALL":
		show_all()
main()
