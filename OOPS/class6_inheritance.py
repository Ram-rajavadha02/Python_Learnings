class Employee:

    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.4
        Employee.no_of_employees += 1

    def increase(self):
        self.salary = int(self.salary*Employee.increment)

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day == "sunday":
            return False
        else:
            return True

class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)      #super() inherites the class which is called and calls its construct.
        self.proglang = proglang
        self.exp = exp

    def increase(self):
        self.salary = int(self.salary*(self.increment+0.2))
        return self.salary

#shub = Employee('shubham', 'das', 88000)
#print(Employee.isopen('monday'))

harry = Programmer('Harry', 'Jackson', 44000, 'python', '5 yrs')
print(harry.exp)

print(harry.increase())         #this print prints the return value of def increase(self)

#lovish = Employee.from_str("Lovish-Jackson-76000")
#rohan = Employee('Rohan', 'Das', 44000)

#print(lovish.fname)
#print(lovish.lname)
#print(lovish.salary)