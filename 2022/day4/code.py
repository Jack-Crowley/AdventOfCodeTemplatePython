import itertools
import collections
import heapq
from submit import Submit

with open('./2022/day4/input.txt') as data: data = [i.strip() for i in data.readlines()]

submit = Submit(2022, 4)

file = open('./2022/day4/codetracker.txt')
part = file.readline().strip()
file.close()

#Edit Part 1 Code
def part1():
    counter = 0
    for i in data:
        one,two = i.split(",")
        o1,o2 = one.split("-")
        t1,t2=two.split('-')
        o1=int(o1)
        o2=int(o2)
        t1=int(t1)
        t2=int(t2)
        if (o1 >= t1 and o2 <= t2):
            counter+=1
        elif (t1 >= o1 and t2 <= o2):
            counter+=1
    return counter

#Edit Part 2 Code
def part2():
    counter = 0
    for i in data:
        one,two = i.split(",")
        o1,o2 = one.split("-")
        t1,t2=two.split('-')
        o1=int(o1)
        o2=int(o2)
        t1=int(t1)
        t2=int(t2)
        if (o1 >= t1 and t2 >= o1):
            counter+=1
        elif (t1 >= o1 and o2 >= t1):
            counter+=1
    return counter

time = 0
p2 = part2()
print("Your answer to Part 2 is", p2)

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