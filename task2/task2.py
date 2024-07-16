import math
import sys
f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'r')
px, py = map(int, f1.readline().split())
r = int(f1.readline())
while f2:
    clist = list(map(int, f2.readline().split()))
    if len(clist) == 0:
        break
    n = math.sqrt(math.fabs((px - clist[0]) ** 2 + (py - clist[1]) ** 2))
    if n == r:
        print('0')
    elif n < r:
        print('1')
    else:
        print('2')
f1.close(), f2.close()


