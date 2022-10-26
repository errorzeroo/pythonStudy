def solution(survey, choices):
    answer = ''
    types = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    score = [[0]*2 for i in range(4)]
    for l in range(len(choices)):
        if choices[l] <= 3:
            for t in range(4):
                if types[t][0] == survey[l][0]:
                    score[t][0] += 4 - choices[l]
                elif types[t][1] == survey[l][0]:
                    score[t][1] += 4 - choices[l]
        elif choices[l] > 4:
            for t in range(4):
                if types[t][0] == survey[l][1]:
                    score[t][0] += choices[l] - 4
                elif types[t][1] == survey[l][1]:
                    score[t][1] += choices[l] - 4
    for a in range(4):
        if score[a][0] > score[a][1]:
            answer += types[a][0]
        elif score[a][0] < score[a][1]:
            answer += types[a][1]
        else:
            answer += types[a][0]

    return answer


'''
처음엔 삼중 배열로 [[['R', 0], ['T', 0]], ...]이렇게 만들었다가 보기가 힘들어서
검색 하니 이중 배열에 점수를 따로 하길래 그렇게 해서 풀었다.(내 코드로 푼거)
성격 유형 별 배열을 2중으로 초기화 하고
점수도 2중으로 초기화 하고
choices의 길이를 돌면서
점수가 3 이하면(1, 2, 3 이면)
다시 4번 for문 돌면서(types와 score의 길이가 4여서)
types의 t번째 첫번째 값과 같은지 본다 같으면 score에 t번째 첫번째 값에 4-점수를 저장(하고 break를 넣으면 빨라질 듯)
아니면 types의 t번째 두번째 값과 같은지 본다 같으면 score에 t번째 두번째 값에 4-점수를 저장(하고 break를 넣으면 빨라질 듯)
점수가 4를 초과 하면(5, 6, 7 이면)
다시 4번 for문 돌면서(types와 score의 길이가 4여서)
types의 t번째 첫번째 값과 같은지 본다 같으면 score에 t번째 첫번째 값에 점수-4를 저장(하고 break를 넣으면 빨라질 듯)
아니면 types의 t번째 두번째 값과 같은지 본다 같으면 score에 t번째 두번째 값에 점수-4를 저장(하고 break를 넣으면 빨라질 듯)
answer에 넣어줄 for문 4번 돌면서(types와 score의 길이가 4여서)
score에 a번째 첫수가 두번째 수보다 크면
type의 a번째 첫수를 answer에 추가 하고
score에 a번째 두번째 수가 첫 수보다 크면
type의 a번째 두번째 수를 answer에 추가 하고
같으면 type의 a번째 첫수를 answer에 추가 한다.(type을 알파벳 빠른 순으로 맞췄기 떄문에)
'''