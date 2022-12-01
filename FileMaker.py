import os

class File():
    def __init__(self, day, year):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.createYearFolder(year)
        self.createDayFolder(day)
    
    def createYearFolder(self, year):
        self.path = self.path+"/"+str(year)
        if not os.path.exists(self.path):
            os.makedirs(self.path)


    def createDayFolder(self, day):
        self.path = self.path+"/day"+str(day)+"/"
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        else:
            if (input("This file already exists, would you like to overwrite it (y/n)").upper()=="N"):
                quit()