# 수 정렬하기 3
from sys import stdin
N = int(input())                # 인풋 받을 갯수 인풋
count = [0]*10001               # count 안에 10001개 초기화
for i in range(N):              # 인풋 받은 N만큼 for문 돌기
    num = int(stdin.readline())
    count[num] += 1             # count 리스트에 인풋 받은 num의 인덱스에 +1
for j in range(len(count)):     # count 10001개 돌기
    for k in range(count[j]):   # count 안의 j 인덱스 만큼 돌기
        print(j)                # j가 숫자야 그거 출력
