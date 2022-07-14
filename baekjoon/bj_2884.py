H, M = map(int, input().split())
if H == 0:
    if M >= 45:
        M = M - 45
    else:
        M = M + 15
        H = 23
    print(H, M)
elif M == 0:
    if M >= 45:
        M = M - 45
    else:
        M = M + 15
        H = 23
    print(H, M)
else:
    if M >= 45:
        M = M - 45
    else:
        H = H - 1
        M = M + 15
    print(H, M)
