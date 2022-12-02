import itertools
import collections
import heapq
from submit import Submit

with open('./2022/day2/input.txt') as data: data = [i.strip() for i in data.readlines()]



#Edit Part 1 Code
def part1():
    counter = 0
    points = {"X":1,"Y":2,"Z":3}
    winning = {"A":"Y", "B":"Z","C":"X"}
    same = {"A":"X","B":"Y","C":"Z"}
    for i in data:
        x,y = i.split(" ")
        counter+=points[y]
        if same[x]==y:
            counter+=3
        elif winning[x]==y:
            counter+=6
        

    return counter

#Edit Part 2 Code
def part2():
    counter = 0
    points = {"X":1,"Y":2,"Z":3}
    winning = {"A":"Y", "B":"Z","C":"X"}
    lose = {"A":"Z","B":"X","C":"Y"}
    same = {"A":"X","B":"Y","C":"Z"}
    for i in data:
        x,y = i.split(" ")
        if y=="X":
            counter+=points[lose[x]]
        elif y=="Y":
            counter+=points[same[x]]
            counter+=3
        else:
            counter+=points[winning[x]]
            counter+=6
        

    return counter

p1 = part1()
print("Your answer to Part 1 is", p1)
p2 = part2()
print("Your answer to Part 2 is", p2)