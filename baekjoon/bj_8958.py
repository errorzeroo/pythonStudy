num = int(input())
for quiz in range(num):
    quiz = list(map(str, input()))
    sum_q = 0
    add_q = 0
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            add_q += 1
            sum_q += add_q
        else:
            add_q = 0
    print(sum_q)