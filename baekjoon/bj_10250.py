T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())  # 층, 호수, N번째 손님 인풋 받기
    room_num = 0
    while 1:
        if H > N:                        # 층보다 손님 수가 작을 때 와일문 멈춤
            break
        N = N - H                        # 손님 수에서 층을 뺀 숫자가 층수
        if N == 0:                       # 층이 0 이 될 때 꼭대기 층으로 지정
            N = H
            break
        room_num += 1                    # 호수 누적
    if room_num >= 9:                    # 호수가 10 이상이 되면 그냥 호수 출력
        print(N, room_num+1, sep='')
    else:
        print(N, 0, room_num+1, sep='')  # 10 이하면 0과 호수 출력
