import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
j, f, i = 5, 1, 0 #Длина обхода, следующее число, инкремент
for i in range (j):
    print(f, end = '')
    f = 1 + (f + m - 2) % n