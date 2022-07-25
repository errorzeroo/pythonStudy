num = int(input())
for i in range(num):
    num_1, num_2 = map(int, input().split())
    if num_1 > num_2:
        print('#', i+1, ' ', '>', sep='')
    elif num_1 == num_2:
        print('#', i+1, ' ', '=', sep='')
    else:
        print('#', i+1, ' ', '<', sep='')