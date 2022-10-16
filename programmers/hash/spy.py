def solution(clothes):
    answer = 1
    types = [y for x, y in clothes]
    types = [types.count(type) for type in set(types)]
    for clo in types:
        answer *= clo + 1

    answer -= 1
    return answer

'''
해시 문제인데 수학이 들어 갔다. 풀이 방법을 좀 참고 해서 풀었다.
types에 옷의 종류만 담아 주려고 했는데 제일 깔끔한 방법이라고 생각 한다.
그리고 for문에서 2중 리스트 안에 2개 값을 둘 다 가져올 수 있는 것도 이번에 처음 알았다.

옷 종류의 개수를 옷 종류 별로 넣어 두고
for 문 돌면서 answer에 선택 하는 경우의 수(cnt) 선택 하지 않는 수(+1)를 곱한다
하나도 고르지 않은 것 을 제외 한다(-1)
'''