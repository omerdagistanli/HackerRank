import math
import os
import random
import re
import sys

def solve(s):
    name = []
    name = s.split()
    for i in range(len(name)):
        print(name[i].capitalize(), end=" ")

fptr = open(os.environ['OUTPUT_PATH'], 'w')
s = input()
result = solve(s)
fptr.write(result + '\n')
fptr.close()