# testing classes

class AnonymousSurvey:
    """"Keep anonymous answers for questions in the survey."""

    def __init__(self, question):
        """Keep the question and prepare to keep the answer."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show question from survey."""
        print(self.question)

    def store_response(self, new_response):
        """Keep single response at the question from survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all answers."""
        print("The answers: ")
        for response in self.responses:
            print("- ", response)
