# read file line after line

# show just string with information about place where the file is
filename = "pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line)

with open(filename) as file_object:
    print("\n")
    for line in file_object:
        print(line.rstrip())
