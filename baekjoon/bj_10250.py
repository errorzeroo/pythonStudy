T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    room_num = 0
    while 1:
        if H > N:
            break
        N = N - H
        if N == 0:
            N = H
            break
        room_num += 1
    if room_num >= 9:
        print(N, room_num+1, sep='')
    else:
        print(N, 0, room_num+1, sep='')