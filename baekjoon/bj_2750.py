N = int(input())
count = []
for i in range(N):
    i = int(input())
    count.append(i)
for j in sorted(count):
    print(j)