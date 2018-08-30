class Allergies(object):

    def __init__(self, score):
        score =  score % 256
        self.list = []
        item_dict = {1:"eggs" ,2:"peanuts" ,4: "shellfish" ,8:"strawberries" ,16:"tomatoes" ,32: "chocolate" ,64:"pollen" ,128:"cats"}
        for i,k in item_dict.items():
            if score & i:
                self.list.append(k)

    def is_allergic_to(self, item):
        if item in self.list:
            return True
        return False

    @property
    def lst(self):
        return self.list

