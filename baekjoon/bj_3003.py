chess = list(map(int, input().split()))
chess_list = [1, 1, 2, 2, 2, 8]
for idx, i in enumerate(chess):
    if i == chess_list[idx]:
        print(0, end=' ')
    else:
        print(chess_list[idx]-i, end=' ')