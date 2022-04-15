# show use of try except and else

print("Input two numbers, which will be divide.")
print("Write q, to quit.")

while True:
    first_answer = input("\nFirst number: ")
    if first_answer == "q":
        break
    second_answer = input("\nSecond number: ")
    if second_answer == "q":
        break
    try:
        # here should be part of code which can generate error
        answer = int(first_answer) / int(second_answer)
    except ZeroDivisionError:
        # if operation from try is wrong print information about error
        print("You cannot divide with 0!")
    else:
        # if operation went right do else part of the code
        print(answer)
