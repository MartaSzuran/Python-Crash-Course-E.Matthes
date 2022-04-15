# creating list of rows
# to keep access beside "with" function
filename = "pi_digits.txt"

with open(filename) as file_object:
    # save each line in list lines
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
