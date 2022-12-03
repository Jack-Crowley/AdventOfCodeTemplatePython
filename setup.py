import os
from termcolor import colored
import sys
import stat
import time
import shutil

def progressBar(prefix,x,index,total):
    print(f"{prefix} |{'█'*x}{'.'*(50-x)}| {index}/{total}", end='\r', file=sys.stdout, flush=True)

def progressBarSuccess(prefix,index):
    x=50
    print(f"{prefix} - Completed |"+colored('█'*x,"green")+f"{'.'*(50-x)}| {index}/{index}", end='\r', file=sys.stdout, flush=True)

def progressBarFailed(prefix,index):
    x=50
    print(f"{prefix} - Failed |"+colored('█'*x,"red")+f"{'.'*(50-x)}| {index}/{index}", end='\r', file=sys.stdout, flush=True)

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

archivedDir = os.path.join(path,archivePath)
os.mkdir(archivedDir)
if reset.lower()=="y":
    try:
        for i in range(2015, 2023):
            orgPath = os.path.dirname(__file__)+"\\"+str(i)
            if os.path.exists(orgPath):
                shutil.move(orgPath, archivedDir)
            x=int((i-2015)*(50/7))
            progressBar("Archiving Folders",x,i-2015,7)
            time.sleep(0.1)
        progressBarSuccess("Ärchiving Folders",7)
    except Exception as e:
        progressBarFailed("Ärchiving Folders",7)
        print(e)
        quit()

print()

imports = ["collections","heapq","datetime","termcolor","requests","python-dotenv","pathlib","bs4","os","sys"]

x = 0/50*5
i = 0

try:
    import collections
    progressBar("Testing Imports",i*5,i,10)
    i+=1
except:
    progressBarFailed("Testing Imports",10)
    print(colored("\nPlease install "+imports[i],"red"))
    quit()
time.sleep(0.1)
try:
    import heapq
    progressBar("Testing Imports",i*5,i,10)
    i+=1
except:
    progressBarFailed("Testing Imports",10)
    print(colored("\nPlease install "+imports[i],"red"))
    quit()
time.sleep(0.1)
try:
    import datetime
    progressBar("Testing Imports",i*5,i,10)
    i+=1
except:
    progressBarFailed("Testing Imports",10)
    print(colored("\nPlease install "+imports[i],"red"))
    quit()
time.sleep(0.1)
try:
    from termcolor import colored, cprint
    progressBar("Testing Imports",i*5,i,10)
    i+=1
except:
    progressBarFailed("Testing Imports",10)
    print(colored("\nPlease install "+imports[i],"red"))
    quit()
time.sleep(0.1)
try:
    import requests
    progressBar("Testing Imports",i*5,i,10)
    i+=1
except:
    progressBarFailed("Testing Imports",10)
    print(colored("\nPlease install "+imports[i],"red"))
    quit()
time.sleep(0.1)
try:
    from dotenv import load_dotenv, find_dotenv
    progressBar("Testing Imports",i*5,i,10)
    i+=1
except:
    progressBarFailed("Testing Imports",10)
    print(colored("\nPlease install "+imports[i],"red"))
    quit()
time.sleep(0.1)
try:
    from pathlib import Path
    progressBar("Testing Imports",i*5,i,10)
    i+=1
except:
    progressBarFailed("Testing Imports",10)
    print(colored("\nPlease install "+imports[i],"red"))
    quit()
time.sleep(0.1)
try:
    from bs4 import BeautifulSoup
    progressBar("Testing Imports",i*5,i,10)
    i+=1
except:
    progressBarFailed("Testing Imports",10)
    print(colored("\nPlease install "+imports[i],"red"))
    quit()
time.sleep(0.1)
try:
    import os
    progressBar("Testing Imports",i*5,i,10)
    i+=1
except:
    progressBarFailed("Testing Imports",10)
    print(colored("\nPlease install "+imports[i],"red"))
    quit()
time.sleep(0.1)
try:
    import sys
    progressBar("Testing Imports",i*5,i,10)
    i+=1
except:
    progressBarFailed("Testing Imports",10)
    print(colored("\nPlease install "+imports[i],"red"))
    quit()
time.sleep(0.1)
progressBarSuccess("Testing Imports",10)
print()

progressBar("Storing Session ID",0,0,1)
time.sleep(0.5)
try:
    f=open(".env","w")
    f.write("session = "+sessionID)
    f.close()
    progressBarSuccess("Storing Session ID",1)
except:
    progressBarFailed("Storing Session ID",1)
    print(e)
    quit()
time.sleep(0.1)
print()
progressBar("Finishing Up",0,0,1)
time.sleep(0.5)
progressBarSuccess("Finishing Up",1)
print("\nSetup complete")