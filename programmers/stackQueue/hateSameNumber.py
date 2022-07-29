def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])
    return answer

'''
arr에서 값을 지워 가는 방식은 안됨 answer에 새로 넣어주는 방식

빈 answer을 만들고 첫번째 값은 넣어 주고
두 수를 비교 하는 것이기 때문에 전체 길이 보다 하나 작은 for문을 돌린다
두 수가 다르면 뒤에 수를 답에 저장
'''