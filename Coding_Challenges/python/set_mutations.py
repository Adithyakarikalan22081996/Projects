'''
We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.

.update() or |=
Update the set by adding elements from an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])

.difference_update() or -=
Update the set by removing elements found in an iterable/another set.
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])

.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
'''

'''
TASK
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

input_lines = sys.stdin.read().splitlines()

no_of_elements_in_set_A = int(input_lines[0])
set_A = set(map(int,input_lines[1].split(' ')))
no_of_other_sets = int(input_lines[2])
line = 3
for i in range(no_of_other_sets):

    action = input_lines[line].split(' ')[0]
    other_set = set(map(int, input_lines[line + 1].split()))
    if action == "update":
        set_A.update(other_set)
    elif action == "intersection_update":
        set_A.intersection_update(other_set)
    elif action == "difference_update":
        set_A.difference_update(other_set)
    elif action == "symmetric_difference_update":
        set_A.symmetric_difference_update(other_set)
    line = line+2


print(sum(set_A))
        
    