from domains.Courses import Courses
from domains.Student import Student

def AddStu():
    print('Please enter the details of this new student: ')
    x = input('Student ID: ')
    y = input('Student name: ')
    z = input('DOB: ')
    student = Student(x, y, z)
    return student