# 수 정렬하기
N = int(input())         # 인풋 받을 갯수 인풋
count = []               # count 리스트로 초기화
for i in range(N):       # 인풋 받은 N만큼 for문 돌기
    i = int(input())
    count.append(i)      # 빈 count 리스트에 인풋 받은 i 넣기
for j in sorted(count):  # count 정렬 하고 for문 돌려 값 뽑기
    print(j)