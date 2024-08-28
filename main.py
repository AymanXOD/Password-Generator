from random import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Easy Version
import random

p_l = ""
p_s = ""
p_n = ""

pass_letter = random.choices(letters, k=nr_letters)
for x in pass_letter:
    p_l += x

pass_symbols = random.choices(symbols, k=nr_symbols)
p_s = str(p_s)
for x in pass_symbols:
    p_s += x

pass_number = random.choices(numbers, k=nr_numbers)
p_n = str(p_n)
for x in pass_number:
    p_n += x

ez_pass = p_l + p_s + p_n
print(f"Your desired password is {ez_pass} [Simple]")

# Optimized one:
# ez_pass = ''.join(pass_letter + pass_symbols + pass_number)
# print(f"Your desired password is {ez_pass} [Simple]")

# Hard Version

password = str(ez_pass)

hd_password = "".join(random.sample(password, len(password)))

print(f"Your desired password is {hd_password} [Complex]")
