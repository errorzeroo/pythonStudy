k = []
for num in range(5):
    num = input()
    k.append(num)
for i in k:
    a = int(i[0]) + int(i[2]) + int(i[4]) + int(i[6])
    for j in range(1, 7, 2):
        if i[j] != '0':
            a *= int(i[j])
    print(a%10)