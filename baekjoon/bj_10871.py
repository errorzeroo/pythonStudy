# X보다 작은 수
N, X = map(int, input().split())     # A 인풋 개수, 숫자 인풋
A = list(map(int, input().split()))  # A 인풋
for i in A:                          # A에서 X 보다 작은 수 출력
    if i < X:
        print(i, end=' ')