def solution(absolutes, signs):
    answer = 0
    for idx, i in enumerate(signs):
        if i:
            answer += absolutes[idx]
        else:
            answer -= absolutes[idx]
    return answer