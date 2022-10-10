length, num = map(int, input().split())
cnt = 0
for i in range(num):
    garo, sero = map(int, input().split())
    if garo == 1:
        if sero == 1 or sero == length:
            cnt += 3
        elif sero != 1 and sero != length:
            cnt += 4
    elif garo == length:
        if sero == 1 or sero == length:
            cnt += 3
        elif sero != 1 and sero != length:
            cnt += 4
    elif garo != 1 and garo != length:
        if sero == 1 or sero == length:
            cnt += 4
        elif sero != 1 and sero != length:
            cnt += 5
print(cnt)
'''
3 3
3 3
3 3
1 1
9
4 4
1 1
4 4
3 3
2 4
15
'''