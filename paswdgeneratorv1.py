import random
import string
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Fore.CYAN + Style.BRIGHT + "**************************")
print(Fore.RED+ Style.BRIGHT +"Welcome to password generator...")

length = int(input(Fore.YELLOW + Style.BRIGHT + '\nEnter the length of your password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print( Fore.GREEN + Style.BRIGHT + "Your new password is: " , password)
print(Fore.CYAN + Style.BRIGHT + "\n**************************")
answer = input(Fore.MAGENTA + Style.BRIGHT +"-Do you like to your password 'Y/n' :")

while answer == 'n':

  temp = random.sample(all,length)
  password = "".join(temp)
  print( Fore.CYAN + Style.BRIGHT + "\n**************************")
  print( Fore.GREEN + Style.BRIGHT + "Your new password is: " , password)
  answer = input(Fore.GREEN + Style.BRIGHT +"-Do you like to your password 'Y/n' :")

  if answer == 'Y' and answer == 'y':
    break

  elif answer != 'Y' and answer != 'y' and answer != 'n':
    print(Fore.RED+ Style.BRIGHT +"\n**************************")
    answer = input(Fore.RED+ Style.BRIGHT +"Please enter a valid answer! 'Y/n' :")
