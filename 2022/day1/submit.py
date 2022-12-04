import datetime
from termcolor import colored, cprint
import requests
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from bs4 import BeautifulSoup
import os

class Submit():
    def __init__(self, year, day):
        self.file = open('./2022/day1/codetracker.txt')
        self.part = self.file.readline().strip()
        print(self.part)
        self.year = year
        self.day = day
        
    def submit(self, answer):
        if self.checkValid():
            self.submitAnswer(answer)

    def checkValid(self):
        self.currTime = datetime.datetime.now()
        self.date_format = "%m:%d:%Y:%H:%M:%S"
        print("date and time:", self.currTime-datetime.datetime.strptime("12:01:2022:15:54:44", self.date_format))
        diff=(self.currTime-datetime.datetime.strptime(self.file.readline().strip(), self.date_format)).total_seconds()
        if diff > 60:
            file2 = open('./2022/day1/codetracker.txt')
            file2.write(f"{self.part}\n")
            file2.write(f"{self.currTime.strftime(self.date_format)}")
            return True
        else:
            print(colored(f"Please wait {60-diff:.0f} more seconds before submitting","white","on_blue"))
            return False

    def submitAnswer(self, answer):
        load_dotenv(find_dotenv())
        sessionID = os.getenv("session")
        cookie = {'session': sessionID}
        data = {"level": self.part, "answer":answer}
        url = f'https://adventofcode.com/{self.year}/day/{self.day}/answer'
        website = requests.post(url, data, cookies=cookie)
        self.soup = BeautifulSoup(website.text, 'html.parser')
        self.printOutput()

    def printOutput(self):
        self.currTime = datetime.datetime.now()
        self.date_format = "%m:%d:%Y:%H:%M:%S"
        response = self.soup.find("main").find("article").find("p").text.lower()
        print(response)
        if "You gave an answer" in response:
            print(colored(response.split("[")[0],"white","on_green"))
        elif "solving" in response:
            print(colored(response.split(".")[0]+" Part has been updated please retry","white","on_yellow"))
            file2 = open('./2022/day1/codetracker.txt', 'w')
            file2.write(f"2\n" if self.part == "1" else "1\n")
            file2.write(f"{self.currTime.strftime(self.date_format)}")
            file2.close()
        elif "not" in response:
            if "high" in response:
                print(colored(f"That is not the right answer; your answer is to HIGH","white","on_red"))
            elif "low" in response:
                print(colored(f"That is not the right answer; your answer is to LOW","white","on_red"))
            else:
                print(colored(f"That is not the right answer","white","on_red"))
        elif "right" in response:
            print(colored(f"That is the right answer","white","on_green"))
            if self.part == '1':
                file2 = open('./2022/day1/codetracker.txt', 'w')
                file2.write(f"2\n")
                file2.write(f"{self.currTime.strftime(self.date_format)}")
                file2.close()
        else:
            print(self.soup.text)
            print(colored(f"Unexpected error","white","on_blue"))