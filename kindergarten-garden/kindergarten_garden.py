from typing import List, Any, Union


class Garden(object):

    def __init__(self, string,students = 0):
        dic = {"V":"Violets","R":"Radishes","C":"Clover","G":"Grass"}
        studentlist = ["Alice", "Bob" ,"Charlie" ,"David", "Eve", "Fred", "Ginny"," Harriet","Ileana", "Joseph", "Kincaid","Larry"]

        if students:
            studentlist = students
            studentlist.sort()
        list2 = []; list3 = []

        length = (len(string) - 1) / 2
        for i in range(int(length)):
            list2.append(dic[string[0:int(length)][i]])
            list3.append(dic[string[int(length)+1:][i]])
        study = {}

        #the dictionary with students and items get filled
        for i in range(int(length /2)):
            study[studentlist[i]] = list2[0+(i*2)]
            study[studentlist[i]] += " "
            study[studentlist[i]] += list2[1+(i*2)]
            study[studentlist[i]] += " "
            study[studentlist[i]] += list3[0+(i*2)]
            study[studentlist[i]] += " "
            study[studentlist[i]] += list3[1+(i*2)]
        self.study = study

    def plants(self, student):
        return self.study[student].split(" ")

