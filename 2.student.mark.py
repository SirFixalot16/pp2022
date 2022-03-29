
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

    def get_numstu(self):
        self.num_stu = input("Enter number of students in class: ")

    
class Student:
    def __init__(self, id, name, dob, courses):
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = courses

    def intro(self):
        print ("Student " + self.name + " has ID: " + self.id +  " attends the following courses: ")
        for x in range (0, len(self.courses)):
            print(self.courses[x].name, "\n")
    
    def get_info(self):
        print("Enter student information:\n")
        self.id = input("ID: ")
        self.name = input("\nName: ")
        self.dob = input("\nDate of birth: ")

    def course_list(self):
        print("Enter student's courses':\n")
        
CourseList = []
StuList = []

Course0 = Courses("000", "Zero", 123)
Course0.show()
Cor0 = []
Stu0 = Student("240", "Tai", "16/01/1995", Cor0)
Cor0.append(Course0)
Stu0.intro()

CourseList.append(Cor0)
StuList.append(Stu0)

def CoursePrint():
    print("All courses: ")
    for x in range(0, len(CourseList)):
        print(CourseList[x], "\n")

def StuPrint():
    print("All students: ")
    for x in range(0, len(StuList)):
        print(StuList[x], "\n")


print("\nHellow orld") # Quick debug code, pay no mind