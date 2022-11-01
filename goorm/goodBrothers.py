from math import ceil
jinwo, sunwo = map(int, input().split())
days = int(input())
for i in range(1, days+1):
    if i % 2 == 1:
        sunwo += ceil(jinwo/2)
        jinwo -= ceil(jinwo/2)
    else:
        jinwo += ceil(sunwo/2)
        sunwo -= ceil(sunwo/2)
print(jinwo, sunwo)

'''
처음에는 ceil 안 쓰고 했는데 틀렸다고 나와서 구글링해서 ceil 쓴 코드를 찾아서 풀었다.
'''