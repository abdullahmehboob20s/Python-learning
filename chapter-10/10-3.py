import os

os.system("cls")

# Static methods


class Employee:
    company = "Google"
    salary = "$100"

    def getSalary(self):
        print(self.salary)

    @staticmethod
    def greet():
        print("Good Morning, Sir")


emp = Employee()
emp.greet()