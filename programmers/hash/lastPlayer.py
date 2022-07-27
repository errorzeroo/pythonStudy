def solution(participant, completion):
    participant.sort()
    completion.sort()
    for last in range(len(completion)):
        if participant[last] != completion[last]:
            return participant[last]
    return participant[-1]

'''
participant는 참여한 사람
completion은 완주한 사람
한명씩 차이난다.
둘을 sort해서 순서를 같이 맞춘다
for문을 작은 completion수로 돌려서 다른 값이 나오면 그 다른 값 리턴
만약 다 돌았는데 다른 값이 없으면 맨 마지막에 정렬된거니까 맨 마지막 값 리턴
'''