from math import *
from numpy import array

class Courses:
    def __init__(self, id, name, num_stu):
        self.id = id
        self.name = name
        self.num_stu = num_stu

    def show(self):
        print ("Course " + self.name + " has ID: " + self.id +  ".")
    

    def get_info(self):
        print("Enter course information:\n")
        self.id = input("ID: ")
        self.name = input("\nName: ")

    def set_numstu(self):
        self.num_stu = input("Enter number of students in class: ")

    def markDict(dict, list):
        print('Please enter the mark of each students in this course: \n')
        for x in range (0, len(list)):
            dict[list[x]] = input()
        return dict

    def printMark(dict, list):
        for x in range(0, len(list)):
            y = list[x]
            z = dict.get(y)
            print('Student ' + x + ': ' + z + '. \n')

    def get_name(self):
        return self.name


    
class Student:
    def __init__(self, id, name, dob, courses):
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = courses

    def intro(self):
        print ("Student " + self.name + " has ID: " + self.id +  " attends the following courses: ")
        for x in range (0, len(self.courses)):
            self.courses[x].show()
    
    def get_info(self):
        print("Enter student information:\n")
        self.id = input("ID: ")
        self.name = input("\nName: ")
        self.dob = input("\nDate of birth: ")

    def get_course(self):
        return self.courses
      
    def set_course(self, x):
        self.courses = x

    def get_name(self):
        return self.name
    
        
#############################


def CoursePrint():
    print("All courses: ")
    for x in range(0, len(CourseList)):
        print(CourseList[x], "\n")

def StuPrint():
    print("All students: ")
    for x in range(0, len(StuList)):
        print(StuList[x], "\n")

def Student_Autofill(StuList, CourseList):
    for x in range (0, len(CourseList)):
        course = CourseList[x]
        for y in range (0, len(StuList)):
            List = StuList[y].get_course()
            for z in range(0, len(List)):
                if List.get_name() == CourseList[x].get_name():
                    CourseList.append(StuList[y].get_name())

        
CourseList = []
StuList = []

Course0 = Courses("000", "Zero", 123)
Course1 = Courses("001", "Un", 123)
Course2 = Courses("002", "Deux", 123)
Course3 = Courses("003", "Trois", 123)
Course4 = Courses("004", "Quatre", 123)

Course0.show()
Cor0 = []
Stu0 = Student("240", "Tai", "16/01/1995", Cor0)
Cor0.append(Course0)
Cor0.append(Course1)
Stu0.intro()

CourseList.append(Cor0)
StuList.append(Stu0)

print("\nHellow orld") # Quick debug code, pay no mind