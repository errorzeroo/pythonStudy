test_case = int(input())
for i in range(test_case):
    num = map(int, input().split())
    mean = int(round(sum(num)/10, 0))
    print('#', i+1, ' ', mean, sep='')