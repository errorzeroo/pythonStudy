# 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
mul = list(str(A*B*C))  # 3수의 곱
for i in range(10):  # 10 까지의 숫자
    i = mul.count(str(i))  # 곱에서 1~9까지 숫자가 몇 번 쓰였는지 확인
    print(i)