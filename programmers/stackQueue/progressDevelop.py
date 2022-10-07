def solution(progresses, speeds):
    import math
    answer = [1]
    percent = []
    days = []
    for i in range(len(progresses)):
        percent.append(100 - progresses[i])
    for j in range(len(speeds)):
        days.append(math.ceil(percent[j] / speeds[j]))
    biggest = days[0]
    for k in range(1, len(days)):
        if days[k] <= biggest:
            answer[-1] += 1
        else:
            answer.append(1)
            biggest = days[k]
    return answer

'''
answer의 1은 처음은 무조건 1이 들어가고, 첫번째 값 계산은 안 하려고.
percent는 for 문 돌면서 100에서 얼마나 남았는지
days는 각 기능 마다 100까지 걸리는 기간
-> for문 돌면서 percent에서 speeds를 나눈 값 올림
days[0] 값을 biggest로 만들고
for문 돌면서 작거나 같으면 마지막 값에 +1
biggest보다 크면 answer에 1 추가
'''