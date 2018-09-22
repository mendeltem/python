from collections import defaultdict



class School(object):
    def __init__(self):
        self.students = defaultdict(list)
        self.sorted_list = []

        self.student_class = defaultdict(list)
        self.student_class = { 1 : "", 2 : "", 3 : "", 4 : ""}

    def add_student(self, name, grade):
        self.student_class[grade] += name+";"

        #print(self.student_class)
        temp = 0
        string_tmp = ""
        for i,y in self.student_class.items():
            temp = y
            for u in y:
                if u != ";":
                    string_tmp += u
                else:
                    self.students[i].append(string_tmp)
                    string_tmp = ""
                #self.students[i] += u

                #self.students[i].append(u)
            #print(i,y)
            temp = 0
            #print(y)





        print("dict: ", self.students)
    def roster(self):
        return (self.sorted_list)

    def grade(self, grade_number):
        return sorted(self.students[grade_number])

school = School()
school.add_student("Mendel", 1)
school.add_student("Bindy", 1)

for name, grade in [
    ('Peter', 2),
    ('Anna', 1),
    ('Barb', 1),
    ('Zoe', 2),
    ('Alex', 2),
    ('Jim', 3),
    ('Charlie', 1),
]: school.add_student(name, grade)
