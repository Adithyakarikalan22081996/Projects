''' .remove(x)
This operation removes element x from the set.
If element x does not exist, it raises a KeyError.
The .remove(x) operation returns None.

.discard(x)

This operation also removes element x from the set.
If element x does not exist, it does not raise a KeyError.
The .discard(x) operation returns None.

.pop()

This operation removes and return an arbitrary element from the set.
If there are no elements to remove, it raises a KeyError.

'''

'''
Task

You have a non-empty set s , and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
input_lines = sys.stdin.read().splitlines()
T = int(input_lines[0])
input_set = set(map(int, input_lines[1].split(' ')))
Commands = int(input_lines[2])

for i in range(Commands):
    command_line = input_lines[i+3].split()
    
    if command_line[0] == 'pop':
        try:
            #input_set.pop()
            input_set.remove(min(input_set))
        except KeyError:
           pass
        
    elif command_line[0] == 'discard':
        value = int(command_line[1])
        input_set.discard(value)
    elif command_line[0] == 'remove':
        value = int(command_line[1])
        try:            
            input_set.remove(value)
        except KeyError:
           pass
    
print(sum(input_set))
