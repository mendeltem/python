from collections import defaultdict

PLANTS = {"V":"Violets","R":"Radishes","C":"Clover","G":"Grass"}
STUDENTS = ["Alice", "Bob" ,"Charlie" ,"David", "Eve", "Fred", "Ginny"," Harriet","Ileana", "Joseph", "Kincaid","Larry"]

class Garden(object):

    def __init__(self, seeds,students = None):
        self.stu = defaultdict(list)
        self.haben = defaultdict(list)
        halbe =  seeds.splitlines()

        if students:
            all_students = sorted(students)
        else:
            all_students = STUDENTS

        for i, st in enumerate(all_students[0:int((len(seeds)-1) /4)]):
            self.haben[st] = [PLANTS[halbe[0][i*2]],
                              PLANTS[halbe[0][1+i * 2]],
                              PLANTS[halbe[1][i*2]],
                              PLANTS[halbe[1][1+i*2]]]

    def plants(self, student):
        return self.haben[student]


gar = Garden("VRCG\nVRCG").plants("Bob")

print(gar)


