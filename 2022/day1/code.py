import itertools
import collections
import heapq
from submit import Submit

with open('./2022/day1/input.txt') as data: data = [i.strip() for i in data.readlines()]

submit = Submit(2022, 1)

file = open('./2022/day1/codetracker.txt')
part = file.readline().strip()
file.close()

#Edit Part 1 Code
def part1(data=data):
    counter = 0
    elves = []
    for i in data:
        if i != "":
            counter+=int(i)
        else:
            elves.append(counter)
            counter = 0
    elves.append(counter)
    return max(elves)

#Edit Part 2 Code
def part2(data=data):
    counter = 0
    elves = []
    for i in data:
        if i != "":
            counter+=int(i)
        else:
            elves.append(counter)
            counter = 0
    elves.append(counter)
    elves.sort()
    return sum(elves[-3:])

time = 0

SampleInput = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

SampleInput = [i.strip() for i in SampleInput.split("\n")]

#Backup incase submit is failing

# Part 1 Backup
# p1 = part1(SampleInput)
# print("Your sample test case answer to Part 1 is", p1)
# p1 = part1()
# print("Your answer to Part 1 is", p1)

# Part 2 Backup
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