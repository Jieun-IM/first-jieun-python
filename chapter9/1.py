from difflib import Match
import re
f = open('data/UNDHR.txt')

for line in f:
    line = line.rstrip()
    if re.search('^\([0-9]+\)', line):
        print(line)