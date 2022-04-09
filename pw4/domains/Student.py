from domains.Courses import Courses

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = []
        self.marklist = {}
        self.gpa = 0

    def intro(self):
        print ("Student " + self.name + " has ID: " + self.id +  " attends the following courses: ")
        for x in range (0, len(self.courses)):
            self.courses[x].show()

    def printMark(self):
        print("Printing student marklist:")
        for x in range(0, len(self.marklist)):
            y = self.courses[x]
            print("Course " + y + ": " + self.marklist.get(y) + ".")

    
    def get_info(self):
        print("Enter student information:\n")
        self.id = input("ID: ")
        self.name = input("\nName: ")
        self.dob = input("\nDate of birth: ")


    def get_course(self):
        return self.courses     
    def set_course(self, x):
        self.courses = x

    def get_marklist(self):
        return self.marklist     
    def set_course(self, x):
        self.marklist = x

    def get_course(self):
        return self.gpa     
    def set_course(self, x):
        self.gpa = x

    def get_name(self):
        return self.name