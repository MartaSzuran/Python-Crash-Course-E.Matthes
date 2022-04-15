# working with data given by user
# save data to reuse then after running program again

import json

username = input("Input your name: ")

filename = "username.json"
with open(filename, "w") as file_object:
    json.dump(username, file_object)
    print("Your name has been saved and will be use later, " + username + "!")
