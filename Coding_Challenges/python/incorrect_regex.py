# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re
input_details = sys.stdin.read() # read all inputs in one line
input_lines = input_details.splitlines() # split lines

T = int(input_lines[0]) # read first entry as T as per Example

for line in input_lines[1:]: # Read lines from index one to end
    try:
        re.compile(line) # check this is valid regex or not
        print(True)
    except re.error:
        print(False)

    