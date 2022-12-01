import itertools
import collections
import heapq

with open("./2022/day01/input.txt") as data: data = [int(i.strip()) if i != "\n" else "" for i in data.readlines()]

def part1():
	temp=0
	array=[]
	for i in data:
		if i!="":
			temp+=i
		else:
			array.append(temp)
			temp=0
	array.sort()
	print(array[-1])


def part2():
	temp=0
	array=[]
	for i in data:
		if i!="":
			temp+=i
		else:
			array.append(temp)
			temp=0
	array.sort()
	print(array[-1]+array[-2]+array[-3])

print('Part 1')
part1()
print('Part 2')
part2()