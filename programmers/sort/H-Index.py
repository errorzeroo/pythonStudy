def solution(citations):
    for i in range(len(citations), -1, -1):
        cnt = 0
        for j in citations:
            if j >= i:
               cnt += 1
        if i <= cnt:
            return i

'''
s = [3, 0, 6, 1, 5]
s = [2, 2, 2, 2]
print(solution(s))
h는 인용된 회수 이기 떄문에 논문의 수를 넘지 않는다. 그래서 시작을 논문 수로 하였다.
회수를 저장할 cnt를 for문 안에서 초기화 해준다.
첫번째 i일 때 논문을 보면서 논문 수가 크거나 같은지 비교,
크다면 cnt를 1 올린다.
cnt가 인용 횟수 i보다 같거나 클 때
i로 리턴하고 종료

----정렬해서 하는 방법
def solution(citations):
    citations.sort(reverse=True)
    answer = [i+1 for i in range(len(citations)) if i+1 <= citations[i]]
    return len(answer)
citations를 내림차순 정렬하여 첫 수부터 인덱스를 비교한다.
'''