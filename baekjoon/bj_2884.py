# 알람 시계
H, M = map(int, input().split())
if H == 0:          # 0시 일 때
    if M >= 45:     # 45분 보다 클 때 45분 빼기
        M = M - 45
    else:
        M = M + 15  # 45분 보다 작을 때 15분 더하기
        H = 23      # 23시로
    print(H, M)
else:
    if M >= 45:
        M = M - 45
    else:
        H = H - 1
        M = M + 15
    print(H, M)
