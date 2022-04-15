from survey import AnonymousSurvey

# create question and survey
question = "What is your language?"
my_survey = AnonymousSurvey(question)

# show question and keep its answer
my_survey.show_question()
print("Press 'q' to quit\n")

while True:
    response = input("Language: ")
    if response == "q":
        break
    my_survey.store_response(response)

# print survey output
print("\nThank you for yours answers!")
my_survey.show_results()
