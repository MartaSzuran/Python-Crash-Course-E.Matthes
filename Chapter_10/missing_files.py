# handle with missing files with FileNotFoundError

filename = "alice.txt"

# with open(filename) as file_object:
#    contents = file_object.read()

# Traceback (most recent call last):
#   File "C:\Users\Marta\Desktop\GIT\Python-Crash-Course-E.Matthes\Chapter_10\missing_files.py", line 5, in <module>
#     with open(filename) as file_object:
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, but file " + filename + " do not exist."
    print(msg)
