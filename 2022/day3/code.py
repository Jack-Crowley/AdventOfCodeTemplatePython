import itertools
import collections
import heapq
from submit import Submit

with open('./2022/day3/input.txt') as data: data = [i.strip() for i in data.readlines()]

submit = Submit(2022, 3)

file = open('./2022/day3/codetracker.txt')
part = file.readline().strip()
file.close()

def findCommonCharacter(p1, p2):
    for i in range(len(p1)):
        if p1[i] in p2:
            return p1[i]

def calculateScore(i):
    if str(i).isupper():
        return ord(i)-65+27
    else:
        return ord(i)-96

#Edit Part 1 Code
def part1():
    counter = 0
    for i in data:
        p1,p2 = i[:int(len(i)/2)],i[int(len(i)/2):]
        counter+=calculateScore(findCommonCharacter(p1,p2))
    return counter

def findCommonCharacterPart2(p1, p2, p3):
    for i in min([p1,p2,p3], key=len):
        if i in p1 and i in p2 and i in p3:
            return i


#Edit Part 2 Code
def part2():
    counter = 0
    x = 0
    temp = []
    for i in data:
        temp.append(i)
        x+=1
        if (x%3==0):
            counter+=calculateScore(findCommonCharacterPart2(temp[0],temp[1],temp[2]))
            temp = []
    return counter

time = 0

if part == '1':
    p1 = part1()
    print("Your answer to Part 1 is", p1)
    if (input("Would you like to submit this answer (y/n)").upper() == "Y"):
        submit.submitAnswer(p1)
elif part=='2':
    p2 = part2()
    print("Your answer to Part 2 is", p2)
    if (input("Would you like to submit this answer (y/n)").upper() == "Y"):
        submit.submitAnswer(p2)