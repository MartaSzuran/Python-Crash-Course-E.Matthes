# code refactoring

import json


def get_stored_username():
    """Get username from the file, if file exist."""
    filename = "user.json"
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Ask user for name and save it into json file."""
    username = input("Input your name: ")
    filename = "user.json"
    with open(filename, "w") as file_object:
        json.dump(username, file_object)
        print("Your name has been saved and will be use later, " + username + "!")
    return username


def greet_user():
    """Greet user using his name."""
    username = get_stored_username()
    filename = "user.json"
    if username:
        print("Hello again, " + username + "!")
    else:
        username = get_new_username()
        print("Your name has been saved and will be use later, " + username + "!")


greet_user()
