def solution(sizes):
    answer = [sizes[0][0], sizes[0][1]]
    answer.sort(reverse=True)
    for i in range(1, len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            if answer[0] < sizes[i][0]:
                answer[0] = sizes[i][0]
            if answer[1] < sizes[i][1]:
                answer[1] = sizes[i][1]
        else:
            if answer[0] < sizes[i][1]:
                answer[0] = sizes[i][1]
            if answer[1] < sizes[i][0]:
                answer[1] = sizes[i][0]
    return answer[0] * answer[1]

'''
답에 sizes 첫 값의 가로 세로를 넣고
내림차순으로 정렬 한다
for문을 sizes의 길이 보다 하나 적게 돌고
i의 0번이 크면 size의 0번과 비교해서 클경우 값을 바꾼다
i의 1번과 size의 1번도 비교하여 클경우 값을 바꾼다
i의 1번이 큰 경우도 똑같이 비교해서 클경우 값을 바꾼다.
'''