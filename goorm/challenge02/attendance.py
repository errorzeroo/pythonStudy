num, find = map(int, input().split())
attendance = []
for i in range(num):
    attendance.append(input().split())
attendance.sort()
print(attendance[find-1][0], attendance[find-1][1])