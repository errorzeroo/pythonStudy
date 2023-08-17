from itertools import combinations
def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    cnt = 0
    for c in combi:
        for p in range(2, sum(c)):
            if sum(c) % p == 0:
                cnt += 1
        if cnt == 0:
            answer += 1
        cnt = 0
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))

'''
소수 구하는 방법을 어떻게 구하지 싶었는데 for문으로 돌리는 방법이 있었다. 검색함(시간 초과 안나서 다행 1단계라 그런 듯)
cnt는 소수인지 판별하는 거 숫자 말고 false/true로 할걸 그랬다 더 깔끔할 듯 그리고 있으면 for문도 멈추고(시간 확보)
nums에서 3가지 숫자 뽑는건 조합 라이브러리 사용 했다.
'''