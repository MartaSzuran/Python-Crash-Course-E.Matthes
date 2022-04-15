# try and except function
# working with errors

# print(5/0)

# Traceback (most recent call last):
#   File "C:\Users\Marta\Desktop\GIT\Python-Crash-Course-E.Matthes\Chapter_10\zero_division_error.py",
#   line 4, in <module>
#     print(5/0)
# ZeroDivisionError: division by zero
# ZeroDivisionError is an object which python created when some error occurs

try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide with 0!")
    