# Import all the Modules and Libraries.
import string
import random

# Store all the Characters in the Lists. 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# Ask User about the Number of Characters
user_input = input("How many characters do you want in your password : ")

# Check this input is it number? is it more than 8?
while True:
	try:
		characters_number = int(user_input)
		if characters_number < 8:
			print("Your Password length should be atleast 8.")
			user_input = input("Please, Enter your number again : ")
		else:
			break
	except:
		print("Please, Enter the numbers only.")
		user_input = input("How many characters do you want in your password : ")

# Shuffle all the Lists.
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# Calculate 30% & 20% of number of characters
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

# Generation of the password (60% letters and 40% digits & punctuations)
result = []

for x in range(part1):
	result.append(s1[x])
	result.append(s2[x])

for x in range(part2):
	result.append(s3[x])
	result.append(s4[x])

# Shuffle the Result
random.shuffle(result)

# Join the Result and Final Output.
password = "".join(result)
print("Your Password is : ", password)
print("Your Password has been Created Successfully.")
print("Thank You.")
