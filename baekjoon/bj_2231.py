# 분해합
N = int(input())       # 분해합을 인풋 받는다
answer = 0             # 생성자가 없는 분해합은 0으로 출력할 기본값
for i in range(1, N):  # 분해합까지를 반복문을 돌려 생성자를 찾는다
    M = i              # 찾을 분해합(M)은 i로 리셋한다
    for j in str(i):   # 분해합을 찾으려 i를 str으로 받는다(i=15일때 1, 5)
        M += int(j)    # 찾을 분해합(M)에 int로 변환한 i를 합친다.(15+1+5)
    if M == N:         # 찾을 분해합(M=21)과 분해합(N)이 같을 때
        answer = i     # i(15)를 answer에 입력
        break
print(answer)          # 생성자 answer출력
