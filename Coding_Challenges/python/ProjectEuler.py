'''
If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Find the sum of all the multiples of  or  below .

'''
# Solution 1:

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x = 0
    for i in range (1,n):
        if i%3 == 0 or i%5==0:
            x = x +i
    
    print(x)

# Solution 2 : using arithmentic progression

import sys

def sum_of_multiples(k, n):
    p = (n - 1) // k
    return k * p * (p + 1) // 2


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    total = sum_of_multiples(3, n) + sum_of_multiples(5, n) - sum_of_multiples(15, n)
    print(total)