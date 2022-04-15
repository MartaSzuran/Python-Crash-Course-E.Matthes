# use name from json file

import json

filename = "username.json"

with open(filename) as file_object:
    username = json.load(file_object)
    print("Hello again, " + username + "!")
    