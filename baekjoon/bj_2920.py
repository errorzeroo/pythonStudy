# 음계
num = list(map(int, input().split()))
if num == list(range(1, 9)):        # list로 1~8까지 받기
    print('ascending')
elif num == list(range(8, 0, -1)):  # list로 8~1까지 받기
    print('descending')
else:
    print('mixed')