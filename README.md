### AdventOfCode2022
A template and solutions for completing Advent Of Code in a quick and neatly fashion.

# Blank Template
If you wish to use the repository on your own, donwload the template from [Here](https://github.com/Jack-Crowley/AdventOfCode2022/releases/tag/BlankTemplate "Here")

# Setup
1. After installing the repository, create a file called ".env" in the main folder
2. Follow the template of the of ".sample.env" and copy your session ID from the Advent oOf Code website

# Usage
### For current day problem
`$ python aoc.py`

### For day in current yeer
`$ python aoc.py {day}`

Example `$ python aoc.py 5`

### For any advent of code problem
`$ python aoc.py {day} {year}`

Example `$ python aoc.py 5 2015`

# Load Input
If you already have the code, but want to reload your input, you can just remake the input.
### For current day problem
`$ python loadInput.py`

### For day in current yeer
`$ python loadInput.py {day}`

Example `$ python loadInput.py 5`

### For any advent of code problem
`$ python loadInput.py {day} {year}`

Example `$ python loadInput.py 5 2015`

# Dependencies
`$ pip install bs4`

`$ pip install requests`

`$ pip install python-dotenv`
