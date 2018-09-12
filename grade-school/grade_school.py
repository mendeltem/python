from collections import defaultdict


class School(object):
    def __init__(self):
        self.students = defaultdict(list)

    def add_student(self, name, grade):
        self.students[grade].append(name)

    def roster(self):
        studend_list = []
        slist = []
        sorted_studends = sorted(self.students)

        for i in sorted_studends:
            slist.append(sorted(self.students[i]))

        for sublist in slist:
            for i in sublist:
                studend_list.append(i)

        return (studend_list)

    def grade(self, grade_number):
        return sorted(self.students[grade_number])


