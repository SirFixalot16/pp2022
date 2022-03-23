
class Courses:
    def _init_(self, id, name, num_stu, mark_list):
        self.id = id
        self.name = name
        self.num_stu = num_stu

    def _show_(self):
        print ('Course {self.name} has ID {self.id}.')
    


class Student:
    def _init_(self, id, name, dob, courses):
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = courses

    def _intro_(self):
        print('Student {self.name}, ID: {self.id}, DOB: {self.dob}, attend courses: ')
        for x in range (0, len(self.courses)):
            print("\n", self.courses[x])
    
    def get_info(self):
        print("Enter student information:\n")
        self.id = input("ID: ")
        self.name = input("\nName: ")
        self.dob = input("\nDate of birth: ")





print("Hellow orld") # Quick debug code, pay no mind