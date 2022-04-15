# module JSON - JavaScript Object Notation
# write data into files to give possibility to use it again
# that files can be read with many programming languages

import json

# write data into file
# json.dump() - write data into file
numbers = [2, 3, 5, 7, 11, 13]

filename = "numbers.json"
with open(filename, "w") as file_object:
    json.dump(numbers, file_object)

# load data from file
# json.load()

filename = "numbers.json"
with open(filename) as file_object:
    numbers = json.load(file_object)

print(numbers)
