class Garden(object):
    def __init__(self, string,students = 0):
        dic = {"V":"Violets","R":"Radishes","C":"Clover","G":"Grass"}
        studentlist = ["Alice", "Bob" ,"Charlie" ,"David", "Eve", "Fred", "Ginny"," Harriet","Ileana", "Joseph", "Kincaid","Larry"]

        if students:
            studentlist = students
            studentlist.sort()
        list1 = []
        list2 = []
        list3 = []
        length = 0
        #Items appended in a list
        for z in string:
            if z != "\n":
                list1.append(dic[z])
                length +=1
        length = length /2

        #the list turned in two lists each grom different row
        for i in range(int(length)):
            list2.append(list1[i])
            list3.append(list1[i+int(length)])
        study = {}
        length = int(length /2)
        #the dictionary with students and items get filled
        for i in range(length):
            study[studentlist[i]] = list2[0+(i*2)]
            study[studentlist[i]] += " "
            study[studentlist[i]] += list2[1+(i*2)]
            study[studentlist[i]] += " "
            study[studentlist[i]] += list3[0+(i*2)]
            study[studentlist[i]] += " "
            study[studentlist[i]] += list3[1+(i*2)]
        self.study = study
        self.studentlist = studentlist

    def plants(self, student):
        return self.study[student].split(" ")
