# create single string from file

filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))

pi_string_2 = ""

for line in lines:
    # rstrip()
    pi_string_2 += line.rstrip()

print(pi_string_2)
print(len(pi_string_2))

pi_string_3 = ""

for line in lines:
    # strip()
    pi_string_3 += line.strip()

print(pi_string_3)
print(len(pi_string_3))
