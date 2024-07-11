with open('file1.txt', 'r') as f:
    num = list(map(int, f.readlines()))
avg = sum(num)//len(num)
count, i = 0, 0
while num.count(avg) != len(num):
    if num[i] > avg:
        num[i] -= 1
    elif num[i] < avg:
        num[i] +=1
    if num[i] == avg:
        i += 1
    count += 1
    print ( count)