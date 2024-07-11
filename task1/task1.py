n, m= int(input('n =')), int(input('m ='))
j, f, i = 4, 1, 0 #Длина обхода, следующее число, инкремент
for i in range (j):
    print(f, end = '')
    f = 1 + (f + m - 2) % n