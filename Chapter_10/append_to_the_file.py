# append to the file

filename = "programming.txt"

# when file already exist we should use append to open,
# because using "w" will overwrite that file and content will be deleted
with open(filename, "a") as file_object:
    file_object.write("\nI love to practise new functionalities.")
