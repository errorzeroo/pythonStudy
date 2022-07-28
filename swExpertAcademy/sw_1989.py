test_case = int(input())
for i in range(test_case):
    word = input()
    if word[:] == word[::-1]:
        print('#', i+1, ' ', 1, sep='')
    else:
        print('#', i + 1, ' ', 0, sep='')