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
        self.files = File(day,year,True)
        self.loadInput() 

    def loadInput(self):
        print(f'https://adventofcode.com/{self.year}/day/{self.day}/input')
        self.r = requests.post(f'https://adventofcode.com/{self.year}/day/{self.day}/input', cookies=self.cookies)
        self.soup = BeautifulSoup(self.r.text, 'html.parser')
        self.inputPath = self.files.path+"input.txt"
        self.inputFile = open(self.inputPath, "w")
        for line in self.soup.text.splitlines():
            self.inputFile.write(line+"\n")
        self.inputFile.close()


if (len(sys.argv) == 3):
    getData(sys.argv[1],sys.argv[2])
elif (len(sys.argv) == 2):
    getData(sys.argv[1])
else:
    d = datetime.datetime.now()
    getData(int(d.strftime("%d")))