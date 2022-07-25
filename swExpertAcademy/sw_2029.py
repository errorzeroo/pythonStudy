num = int(input())
for i in range(num):
    num_1, num_2 = map(int, input().split())
    print('#', i+1, ' ', num_1//num_2, ' ', num_1%num_2, sep='')