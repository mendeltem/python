class Allergies(object):

    def __init__(self, score):
        #delete if the range is too big
        while score >=256:
            score -=256
        # convert dezimal to binary and reverse 
        self.score =  bin(score)[2:][::-1]
        itemlist = ["eggs" ,"peanuts" ,"shellfish" ,"strawberries" ,"tomatoes" , "chocolate" ,"pollen" ,"cats" ]
        list = []
        z = 0
        #fill the list with allergic items
        for i in self.score:
            if i == "1":
                list.append(itemlist[int(z)])
            z +=1
        self.list = list

    def is_allergic_to(self, item):
        if item in self.list:
            return True
        return False

    @property
    def lst(self):
        return self.list
