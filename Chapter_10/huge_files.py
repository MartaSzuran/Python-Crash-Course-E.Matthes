# working with million digits
# print first 53

filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

# check if my birth date is inside first digits of pi number

birthday = input("Input your birthday (format: ddmmyy): ")
if birthday in pi_string:
    print("Your birthday is in first 409592 numbers in pi number.")
else:
    print("Sorry! Your birthday is not in first 409592 numbers in pi number.")
