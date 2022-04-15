# show how to open and read files

# open() function returns the object
# with closes the file when connection to it will no longer be needed
# if file will have error and we use close() at the end file will never be close...
with open("pi_digits.txt") as file_object:
    # read() returns empty file at the end of contents
    contents = file_object.read()
    print(contents)
    # to dispose of empty line use rstrip()
    print(contents.strip())
