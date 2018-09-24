from collections import defaultdict


class School(object):
    def __init__(self):
        self.students = defaultdict(list)

    def add_student(self, name, grade):
        self.students[grade].append(name)

    def roster(self):
        return [u for i,y in sorted(self.students.items()) for u in sorted(y)]

    def grade(self, grade_number):
        return self.students[grade_number]
