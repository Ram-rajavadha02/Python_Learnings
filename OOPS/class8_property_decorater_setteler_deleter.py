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

    @property       #it says we made a function but see that function as arttribute and not function.
    def email(self):
        if self.fname == None:
            return 'email not set'
        else:
            return self.fname + '.' + self.lname + '@email.com'

    @email.setter
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        print(name_list)
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

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

if __name__=="__main__":
    harry = Employee('harry', 'jackson', '99000')
    rohan = Employee('rohan', 'das', '9')
    print(harry.email, rohan.email)
    rohan.lname = 'khanna'
    print(rohan.email)
    rohan.email = 'khanna.rohan@gmail.com'
    print(rohan.email)
    del rohan.email
    print(rohan.email)
