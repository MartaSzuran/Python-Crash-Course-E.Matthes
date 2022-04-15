# check if user already input his name
# if not ask him
# else greet him
# using try and except

import json

filename = "user.json"

try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("Input your name: ")
    with open(filename, "w") as file_object:
        json.dump(username, file_object)
        print("Your name has been saved and will be use later, " + username + "!")
else:
    print("Hello again, " + username + "!")
