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

    def markDict(dict, list_stu):
        print('Please enter the mark of each students in this course: \n')
        for x in range (0, len(list_stu)):
            dict[list_stu[x]] = input()
        return dict

    def printMark(dict, list_stu):
        for x in range(0, len(list_stu)):
            y = list_stu[x]
            z = dict.get(y)
            print('Student ' + x + ': ' + z + '. \n')

    def markRound(dict, list_stu):
        list_mark = []
        for x in range(0, len(list_stu)):
            y = list_stu[x]
            z = dict.get(y)
            list_mark.append(z)
        for x in range(0, len(list_mark)):
            math.floor(list_mark[x])
        for x in range(0, len(list_stu)):
            y = list_stu[x]
            z = list_mark[x]
            dict[y] = z

    def get_name(self):
        return self.name