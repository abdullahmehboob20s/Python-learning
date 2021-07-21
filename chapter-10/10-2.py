import os

os.system("cls")


class Employee:
    company = "Google"
    salary = "$100"

    def getSalary(self):
        print(self.salary)


emp = Employee()

emp.salary = "$12093"

emp.getSalary()
