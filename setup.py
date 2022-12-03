import os
from termcolor import colored
import sys
import stat
import time
import shutil

print("Welcome to the AOC template")
reset = input("Would you like to reset the template? (Hint: this would archive all the solutions for 2022) (y/n): ")
sessionID = input("What is your session ID (Hint: https://adventofcode.com/2022/day/1/input): ")
path = os.path.dirname(os.path.abspath(__file__))
backslash = "\\"
currBarLength=0

archivePath="Archived/archive-1"

if not os.path.exists(os.path.join(path, "Archived")):
    os.makedirs(os.path.join(path, "Archived"))

while (os.path.exists(os.path.join(path,archivePath))):
    a,b = archivePath.split('-')
    b=int(b)+1
    archivePath=a+"-"+str(b)

os.mkdir(os.path.join(path,archivePath))
if reset.lower()=="y":
    for i in range(2015, 2023):
        tpath = path+"/"+str(i)
        if os.path.exists(tpath):
            for subdir, dirs, files in os.walk(tpath):
                print(len(files))
                for file in files:
                    f = open(f".\\{i}\\{str(subdir).split(backslash)[-1]}\\{file}","w")
                    f.write("")
                    f.close()
        else:
            print(f'\r{i} |{"█"*currBarLength}| {currBarLength/20}% Cleaning', end = "\r")
            for x in range(20):
                print(f'\r{i} |{"█"*x}| {x/20}% Cleaning', end = "\r")
                time.sleep(.001)
            currBarLength=20
            print(f'\r{i} |'+colored("█"*currBarLength, "green")+f'| {currBarLength/20*100:.0f}% Cleaning - Finished', end = "\r")
            time.sleep(0.5)
            currBarLength=0
        print()




else:
    pass