import sys
input_lines = sys.stdin.read().splitlines()

T = int(input_lines[0])
for line in input_lines[1:T+1]:
    a,b = map(str, line.split())
    try :
        print(int(a)//int(b))
    except Exception as e:
        print('Error Code:', e)