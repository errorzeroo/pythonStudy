num = list(map(int, input().split()))
if num == list(range(1, 9)):
    print('ascending')
elif num == list(range(8, 0, -1)):
    print('descending')
else:
    print('mixed')