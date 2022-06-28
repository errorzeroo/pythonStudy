S = int(input())
for i in range(S):
    R, P = input().split()
    R = int(R)
    for j in range(len(P)):
        s = R*P[j]
        print(s, end='')
    print()