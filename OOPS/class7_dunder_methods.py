class Employee:

    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):       #it is a construnctor
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

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return 'Employee({},{},{})'.format(self.fname, self.lname, self.salary)

    def __str__(self):      #if only written print(harry) it return from the construct str and if written print(repr(harry) it returns from construct repr.
        return 'The name of employee is {}'.format(self.fname)
        
harry = Programmer('Harry', 'Jackson', 44000, 'python', '5 yrs')
rohan = Employee('Rohan', 'Das', 44000)

print(harry)
print(repr(harry))

#lovish = Employee.from_str("Lovish-Jackson-76000")
