# Password generator project
import random

# list of numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]

# list of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z',]

# list of symbols
special = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', 
    ':', "'", '"', ',', '.', '<', '>', '/', '?', '`']


print("Welcome to my Password Generator!")

n_letters = int(input("How many letters do you want to include on your password? "))
n_numbers = int(input("How many numbers do you want to include on your password? "))
n_symbols = int(input("How many symbols do you want to input on your passowrd? "))


# first approach, add empty list of password

password_list = []

for _ in range(n_letters):
  password_list.append(random.choice(letters))
  
for _ in range(n_numbers):
  password_list.append(random.choice(numbers))
  
for _ in range(n_symbols):
  password_list.append(random.choice(special))


random.shuffle(password_list)
password = ''.join(password_list)
print(f"Your password is {password}")


# second approach

password_list_2 = []

for _ in range(1, n_letters + 1):
  password_list_2 += (random.choice(letters))
  
for _ in range(1, n_numbers + 1):
  password_list_2 += (random.choice(numbers))
  
for _ in range(1, n_symbols + 1):
  password_list_2 += (random.choice(special))
  

print(password_list_2)
random.shuffle(password_list_2)
print(password_list_2)

password_2 = ""
for char in password_list_2:
  password_2 += char
  
print(password)

  
  
  

