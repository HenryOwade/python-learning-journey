# Classes Trial Example
# The  __init__ constructor

class Student:
    def __init__(self, firstname, lastname, hostel):
        self.firstname = firstname
        self.lastname = lastname
        self.hostel = hostel
        self.email = firstname + "." + lastname + "@" + "company.com"

student1 = Student("Mark", "John", "Migingo")
student2 = Student("Jacob", "Jack", "Mirima")

print(student1.email)
print(student2.email)
print(student1.lastname)

print( "{} {}".format(student1.firstname, student1.lastname))

# firstname, lastname, email, hostel are all attributes of our class Student




