#__init__ is a constructor here

class Student:

#default constructor
    def __init__(self):
        pass

#parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database...")


s1 = Student("Karan", 97)
print(s1.name, s1.marks)
 
s2 = Student("Arjun", 88)
print(s2.name, s2.marks)
        

#Yaha har student ka naam different kr skte h 
