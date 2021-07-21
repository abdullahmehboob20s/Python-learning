import os

os.system("cls")

# Create a class Employee and add salary and increment properties to it.
# write a method "salaryAfterIncreament" method with a @property decorator with a setter which changes the value of increament based on salary


class Employee:
    salary = 1000
    increament = 1.5

    @property
    def salaryAfterIncreament(self):
        return self.salary * self.increament

    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self, sai):
        self.increament = sai / self.salary


a = Employee()
print(a.salaryAfterIncreament)
print(a.increament)
a.salaryAfterIncreament = 2000
print(a.increament)