'''
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

Input Format

The first line will contain the number of test cases, .
The first line of each test case contains the number of elements in set .
The second line of each test case contains the space separated elements of set .
The third line of each test case contains the number of elements in set .
The fourth line of each test case contains the space separated elements of set .

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
input_lines = sys.stdin.read().splitlines()

No_of_test_cases = int(input_lines[0])

line = 1
for i in range(No_of_test_cases):
    set_A = set(map(int,input_lines[line+1].split(' ')))
    set_B = set(map(int,input_lines[line+3].split(' ')))
    if len(set_A.difference(set_B)) == 0:
        print(True)
    else:
        print(False)
    
    line +=4