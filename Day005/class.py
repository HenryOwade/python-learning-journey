# Classes Trial Example

class Student:
    pass

    # Creating student 1 upto student 10 as instances of class Student.
    # Student is a class while student1 all the way to student 10 are instances of a class.
    # Must be created outside of the class

student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
student5 = Student()
student6 = Student()
student7 = Student()
student8 = Student()
student9 = Student()
student10 = Student()

print(student1)
print(student2)
print(student3)
print(student4)
print(student5)
print(student6)
print(student7)
print(student8)
print(student9)
print(student10)

student1.firstname = "Mark"
student1.lastname = "John"
student1.email = "henryowade@gmail.com"
student1.hostel = "Migingo"

student2.firstname = "Jacob"
student2.lastname = "Jack"
student2.email = "jackjacob@gmail.com"
student2.hostel = "Mirima"

print(student2.email)
print(student1.lastname)

# Rather than creating those vaviables manually, 
# we use a special init method using the __init__ constructor.



