# Classes and Objects
# Classes Trial Example
# The __init__ constructot
# Creating Methods


class Student:
    def __init__(self, firstname, lastname, hostel):
        self.firstname = firstname
        self.lastname = lastname
        self.hostel = hostel
        self.email = firstname + "." + lastname + "@" + "company.com"

# Creating a Method
    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)
    

student1 = Student("Mark", "John", "Migingo")
student2 = Student("Jacob", "Jack", "Mirima")

print(student1.fullname())
print(student2.fullname())










