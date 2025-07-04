import random

Rfile = open("Highscore.txt","r+")
HS = Rfile.readline()

def guessing(Guess_number,times):
	count = 1
	Guess = int(input("Enter the number here: "))
	while Guess != Guess_number and count<times:
		if Guess > Guess_number:
			count += 1
			print("Your number is higher!")
			Guess = int(input("Try again: "))
		elif Guess < Guess_number:
			count += 1
			print("Your number is lower!")
			Guess = int(input("Try again: "))
		if Guess == Guess_number:
			print(f"Congratulations! The number is {Guess_number}" )
			return count
	else:
		print("Better next time!")
		print(f"The correct number is {Guess_number}!")
		return ""


start = int(input("Enter the starting number: "))

while True:
	end = int(input("Enter the ending number: "))
	if end > start:
		break
	else:
		print("The end number have to greater than start!")

Guess_number = random.randint(start,end)

while True:
	times = int(input("How many time do you want to guess?\n"))
	if times<(end-start):
		break
	else:
		print("Time have to smaller than" , (end - start))

score = guessing(Guess_number,times)

if score =="":
	pass
elif score < int(HS):
	print(f"Your new highscore is: {score}")
	with open("Highscore.txt","w") as wrt:
		wrt.write(str(score))
		wrt.close()
else:
	print(f"Your score is {score}")