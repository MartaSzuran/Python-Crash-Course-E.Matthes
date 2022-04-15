# text analysis
# founding out how many words are in book alice adventures in wonderland

# showing how split() function works
title = "ALICE’S ADVENTURES IN WONDERLAND"
print(title.split())


def count_words(file_name):
    try:
        # to work with error: UnicodeDecodeError:
        # need to use: encoding="utf8" in open function
        with open(file_name, encoding="utf8") as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        msg = "Sorry, but file " + file_name + " do not exist."
        print(msg)
        # if I don't want python to show any information about error I can use:
        # pass and python will ignore mistake
    else:
        words = contents.split()
        number_of_words = len(words)
        print(number_of_words)


filename = "alice.txt"
count_words(filename)

filenames = ["alice.txt", "moby_dick.txt", "siddhartha.txt"]
for file in filenames:
    count_words(file)
