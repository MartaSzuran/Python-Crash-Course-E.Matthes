# how to save data into file

filename = "programming.txt"
string_to_replace = ""

with open(filename, "w") as file_object:
    file_object.write("I love to programme!")

with open(filename, "r") as file_object:
    lines = file_object.readlines()

for line in lines:
    string_to_replace += line

# checking out replace function
new_string = string_to_replace.replace("programme!", "swim")

print(string_to_replace)
print(new_string)
