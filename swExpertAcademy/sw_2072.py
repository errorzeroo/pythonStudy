test_case = int(input())
for i in range(test_case):
    num = list(map(int, input().split()))
    odd_list = []
    for j in range(len(num)):
        if num[j] % 2 == 1:
            odd_list.append(num[j])
    print('#', i+1, ' ', sum(odd_list), sep='')