num = int(input())
for i in range(num):
    nums = map(int, input().split())
    print('#', i+1, ' ', max(nums), sep='')