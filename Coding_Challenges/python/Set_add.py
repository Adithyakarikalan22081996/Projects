# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
input_lines = sys.stdin.read().splitlines()

t= int(input_lines[0]) 
countries = set() # create a Empty string

for lines in input_lines[1:]:
    countries.add(lines)

print(len(countries))
