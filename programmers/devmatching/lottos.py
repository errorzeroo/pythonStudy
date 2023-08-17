def solution(lottos, win_nums):
    answer = []
    cnt_zero = 0
    cnt_win = 0
    for i in range(6):
        if lottos[i] == 0:
            cnt_zero += 1
        elif lottos[i] in win_nums:
            cnt_win += 1
    if cnt_win + cnt_zero == 6:
        answer.append(1)
    elif cnt_win + cnt_zero == 5:
        answer.append(2)
    elif cnt_win + cnt_zero == 4:
        answer.append(3)
    elif cnt_win + cnt_zero == 3:
        answer.append(4)
    elif cnt_win + cnt_zero == 2:
        answer.append(5)
    else:
        answer.append(6)
    if cnt_win == 6:
        answer.append(1)
    elif cnt_win == 5:
        answer.append(2)
    elif cnt_win == 4:
        answer.append(3)
    elif cnt_win == 3:
        answer.append(4)
    elif cnt_win == 2:
        answer.append(5)
    else:
        answer.append(6)
    return answer