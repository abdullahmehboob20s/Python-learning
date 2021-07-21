import os

os.system("cls")


class Employee:
    company = "Google"
    salary = 100
    location = "Karachi"

    # it will not change the actual "salary" attribute above "location"
    # instead, it will make another instance attribute of "salary" and change that
    def changeSalary0(self, sal):
        self.salary = sal

    # it will change the actual "salary" attribute : Method 1
    def changeSalary(self, sal):
        self.__class__.salary = sal

    # it will change the actual "salary" attribute : Method 2
    @classmethod
    def changeSalary2(cls, sal):
        cls.salary = sal


a = Employee()
print(f"Before: {a.salary}")
a.changeSalary2(200)
print(f"After: {Employee.salary}"
      )  # if you want check the actual salary attribute
print(f"After: {a.salary}")