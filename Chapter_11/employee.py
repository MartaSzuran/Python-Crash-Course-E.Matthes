# create class employee

class Employee:
    """Create employee with name, lastname and annual income."""
    def __init__(self, name, lastname, income):
        self.name = name
        self.lastname = lastname
        self.income = int(income)

    def give_raise(self, employee_raise=""):
        if employee_raise:
            self.income += int(employee_raise)
        else:
            self.income += 5000
        return self.income