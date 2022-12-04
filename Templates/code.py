import itertools
import collections
import heapq
from submit import Submit

with open("input.txt") as data: data = [i.strip() for i in data.readlines()]

submit = Submit(2015, 5)

file = open("./codetracker.txt")
part = file.readline().strip()
file.close()

#Edit Part 1 Code
def part1(data=data):
    counter = 0

    return counter

#Edit Part 2 Code
def part2(data=data):
    counter = 0
    
    return counter

time = 0

SampleInput = """"""
SampleInput = [i.strip() for i in SampleInput.split("\n")]

#Backup incase submit is failing

# "Part 1 Backup"
# p1 = part1(SampleInput)
# print("Your sample test case answer to Part 1 is", p1)
# p1 = part1()
# print("Your answer to Part 1 is", p1)

# "Part 2 Backup"
# p2 = part2(SampleInput)
# print("Your sample test case answer to Part 2 is", p2)
# p2 = part2()
# print("Your answer to Part 2 is", p2)

if part == '1':
    p1 = part1(SampleInput)
    print("Your sample test case answer to Part 1 is", p1)
    p1 = part1()
    print("Your answer to Part 1 is", p1)
    if (input("Would you like to submit this answer (y/n)").upper() == "Y"):
        submit.submitAnswer(p1)
elif part=='2':
    p1 = part1(SampleInput)
    print("Your sample test case answer to Part 1 is", p1)
    p2 = part2()
    print("Your answer to Part 2 is", p2)
    if (input("Would you like to submit this answer (y/n)").upper() == "Y"):
        submit.submitAnswer(p2)