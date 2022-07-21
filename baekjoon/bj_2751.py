# 수 정렬하기 2
from sys import stdin
N = int(input())         # 인풋 받을 갯수 인풋
count = []               # count 리스트로 초기화
for i in range(N):       # 인풋 받은 N만큼 for문 돌기
    num = int(stdin.readline())
    count.append(num)      # 빈 count 리스트에 인풋 받은 num 넣기
for i in sorted(count):  # count 정렬 하고 for문 돌려 값 뽑기
    print(i)
