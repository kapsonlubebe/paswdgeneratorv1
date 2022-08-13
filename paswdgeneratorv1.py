import random
import string

print("Welcome to password generator...")

length = int(input('\nEnter the length of your password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print("Your new password is: " , password)
print("\n**************************")
answer = input("-Do you like to your password 'Y/n' :")

while answer == 'n':
  
  temp = random.sample(all,length)
  password = "".join(temp)
  print("\n**************************")
  print("Your new password is: " , password)
  answer = input("-Do you like to your password 'Y/n' :")
  
  if answer == 'Y' and answer == 'y':
    break
  
  elif answer != 'Y' and answer != 'y' and answer != 'n':
    print("\n**************************")
    answer = input("Please enter a valid answer! 'Y/n' :")

