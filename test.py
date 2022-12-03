import shutil
import os


orgPath = "C:\\Users\\jack1\Documents\\Coding\Sophomore\AOC\AdventOfCode2022\\2022\day2"

dest = "C:\\Users\\jack1\Documents\\Coding\Sophomore\AOC\AdventOfCode2022\\Archived\\2022"

files = os.listdir(orgPath)

for f in files:
        shutil.move(os.path.join(orgPath, f), os.path.join(dest, f))