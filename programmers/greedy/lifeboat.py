def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1
    while i <= j:
        answer += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1
    return answer

'''
i는 0부터 올라 가고
j는 마지막 인덱스에서 내려 와서
j와 i가 같거나 i가 더 커질 때 까지 while문을 돈다.
먼저 구명 보트 수를 올리고
people[i]+people[j]가 limit보다 작거나 같으면
i를 올린다.(크다면 i가 올라 가지 않는다)
j를 하나 내리고 반복(반복할 때마다 answer은 계속 올라 간다.)
'''