# getting first tests

from name_function import get_formatted_name


print("Write 'q', to quit")

while True:
    first = input("\nInput your name: ")
    if first == "q":
        break
    last = input("\nInput your last name: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print("\tYour name using elegant formatting: " + formatted_name + ".")
