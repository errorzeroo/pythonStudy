num = int(input())
num_list = []
for i in range(1, num+1):
    if num % i == 0:
        num_list.append(i)
for i in num_list:
    print(i, end=' ')
