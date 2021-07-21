import os

os.system("cls")


class Employee:
    comapny = "Microsoft"
    salary = 4500
    salaryBonus = 500

    # Known as (getter)
    # it will only calculate the sum of two things and return it as property (not as a function)
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salaryBonus


a = Employee()
print(a.totalSalary)
a.totalSalary = 7000
print(a.totalSalary)