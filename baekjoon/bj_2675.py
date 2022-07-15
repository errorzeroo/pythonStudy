# 문자열 반복
S = int(input())  # 몇번 반복할 지 설정
for i in range(S):
    R, P = input().split()
    R = int(R)               # R을 숫자형으로
    for j in range(len(P)):  # P의 길이만큼 반복
        s = R*P[j]           # s에 R만큼의 P의 글자를 반복
        print(s, end='')
    print()