from collections import defaultdict


class School(object):
    def __init__(self):
        #a dictionary with the students to return for grade function
        self.students = defaultdict(list)
        #a list to return with roster function
        self.sorted_list = []

        #temp list file
        self.listen = []

        #first dictionary with the raw file, which get extracted to a list and dictionary
        self.student_class = defaultdict(list)
        self.student_class = {1: "", 2: "", 3: "", 4: "", 5:"", 6:"", 7:""}

    def add_student(self, name, grade):
        #the raw dictionary gets filled
        self.student_class[grade] += name+";"
        student_list = []
        string_tmp = ""

        #the raw file get extracted to a  sorted list and dictionary
        for i,y in self.student_class.items():
            for u in y:
                if u != ";":
                    string_tmp += u
                else:
                    student_list.append(string_tmp)
                    string_tmp = ""
            self.listen.append(sorted(student_list))
            self.students[i] = sorted(student_list)
            student_list = []


        self.sorted_list = []
        #flatten the lists fro list of list to a single list
        for i in range(7):
            self.sorted_list+= self.listen[i]

        self.listen = []
    def roster(self):
        return (self.sorted_list)

    def grade(self, grade_number):
        return self.students[grade_number]
