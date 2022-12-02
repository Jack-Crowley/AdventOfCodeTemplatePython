from bs4 import BeautifulSoup
import requests
from FileMaker import File
import os
from dotenv import load_dotenv
import sys
import datetime

class getData():
    def __init__(self, day, year=2022 ):
        #Change Session ID
        load_dotenv()
        sessionID = os.getenv("session")
        self.cookies = {'session': sessionID}
        self.day = day
        self.year = year
        self.files = File(day,year)
        self.loadInput()
        self.createSubmitFile()  
        self.createCodeFile() 
             

    def loadInput(self):
        self.r = requests.post(f'https://adventofcode.com/{self.year}/day/{self.day}/input', cookies=self.cookies)
        self.soup = BeautifulSoup(self.r.text, 'html.parser')
        self.inputPath = self.files.path+"input.txt"
        self.inputFile = open(self.inputPath, "w")
        for line in self.soup.text.splitlines():
            self.inputFile.write(line+"\n")
        self.inputFile.close()

    def createSubmitFile(self):
        self.currTime = datetime.datetime.now()
        self.date_format = "%m:%d:%Y:%H:%M:%S"
        self.codeTracker = open(self.files.path+"codetracker.txt", "w")
        self.codeTracker.write(f"1\n{self.currTime.strftime(self.date_format)}")
        self.submitFile = open(self.files.path+"submit.py", "w")
        with open(os.path.dirname(os.path.abspath(__file__))+"\Templates\submit.py") as data:
            self.template = [i for i in data]
        
        for i in range(len(self.template)):
            if i == 10:
                self.submitFile.write(f"        self.file = open('./{self.year}/day{self.day}/codetracker.txt')\n")
            elif i == 26:
                self.submitFile.write(f"            file2 = open('./{self.year}/day{self.day}/codetracker.txt')\n")
            elif i == 53:
                self.submitFile.write(f"            file2 = open('./{self.year}/day{self.day}/codetracker.txt', 'w')\n")
            elif i == 67:
                self.submitFile.write(f"                file2 = open('./{self.year}/day{self.day}/codetracker.txt', 'w')\n")
            else:
                self.submitFile.write(self.template[i])

    def createCodeFile(self):    
        self.codeFile = open(self.files.path+"code.py", "w")
        with open(os.path.dirname(os.path.abspath(__file__))+"\Templates\code.py") as data:
            self.template = [i for i in data]
        for i in range(len(self.template)):
            if i == 5:
                self.codeFile.write(f"with open('./{self.year}/day{self.day}/input.txt') as data: data = [i.strip() for i in data.readlines()]\n")
            elif i == 7:
                self.codeFile.write(f"submit = Submit({self.year}, {self.day})\n")
            elif i == 9:
                self.codeFile.write(f"file = open('./{self.year}/day{self.day}/codetracker.txt')\n")
            else:
                self.codeFile.write(self.template[i])


if (len(sys.argv) == 3):
    getData(sys.argv[1],sys.argv[2])
elif (len(sys.argv) == 2):
    getData(sys.argv[1])
else:
    d = datetime.datetime.now()
    getData(int(d.strftime("%d")))