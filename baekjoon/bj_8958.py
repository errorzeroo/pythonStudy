# 나머지
num = int(input())
for quiz in range(num):              # 받은 숫자 만큼 반복
    quiz = list(map(str, input()))   # OX 받기
    sum_q = 0
    add_q = 0
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            add_q += 1               # 'O' 일때 1 더하기
            sum_q += add_q           # 더한 값을 누적 해서 더하기
        else:
            add_q = 0                # 'X' 일때 리셋
    print(sum_q)