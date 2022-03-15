Stu_Mark = {"Zero": 0} # Dict of marks, belong to each course, store: Name: Mark

Cor0 = ["000", "Zero New Idea", Stu_Mark[0]] # List of info about course: ID - Name

Cor_of_Stu = [Cor0] # List of courses a student is in

Stu0 = ["000", "Zero", "00/00/0000", Cor_of_Stu[0]] # List of info about student: ID - Name - DOB - Courses that student is in

student = [Stu0] # List of students in a class
course = [Cor0] # List of courses 

def get_num_Stu():
  num = input("Enter the number of students: ")
  return num

def get_stuID():
  thisStu = ["", "", "", ""]
  print("Enter student information:\n")
  thisStu[0] = input("ID: ")
  thisStu[1] = input("Name: ")
  thisStu[2] = input("Date of birth: ")
  return thisStu

def get_num_Course():
  num = input("Enter the number of courses: ")
  return num

def get_courseID():
  thisCor = ["", "", ""]
  print("Enter course information:\n")
  thisCor[0] = input("ID: ")
  thisCor[1] = input("Name: ")
  return thisCor

def course_fill(course_n, student):
    n = len(student)
    for x in range(0,n):
        m = len(student[x][3])
        for y in range(0,m):
            if student[x][3][y] == course_n:
                print("Please enter student " + student[x][1] + " mark: ")
                course_n[student[x][1]] = input
                continue
    return course_n