from itertools import combinations_with_replacement as cwr
def solution(n, info):
    answer = [-1]
    score_diff = -1
    for c in cwr(range(11), n):
        lion_info = [0]*11

        for i in c:
            lion_info[10-i] += 1

        apeach, lion = 0, 0
        for idx in range(11):
            if info[idx] == lion_info[idx] == 0:
                continue
            elif info[idx] >= lion_info[idx]:
                apeach += 10 - idx
            else:
                lion += 10 - idx

        if lion > apeach:
            gap = lion - apeach
            if gap > score_diff:
                score_diff = gap
                answer = lion_info
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))

'''
솔직히 감도 안 오고 내가 풀 수 있는 문제가 아닌데 풀고 있는 느낌이 들어서 검색 했다. 어려운 말들만 줄줄.. 금방 끝내려 했는데 오래 걸렸다.
max_a = 0
    for i in range(len(info)-1, -1, -1):
        apeach[10-i] = info[i]
apeach에 점수랑 info 같이 넣어서 차이 나는 어쩌구 해보려고 했는데 잘 안됐고.. 그나마 주석 되어 있는 풀이를 가져 왔다.(이것도 어려워서 하기 싫어함)
from itertools import combinations_with_replacement 이거 처음 알았는데 중복 조합 라이브러리. 중복 조합 해서 쉽게 풀린 듯
점수 차-score_diff를 -1로 선언(라이언이 이길 수 없을 경우를 초기화)
중복 조합으로 11개를 n만큼 뽑아서 for문 돈다.
lion_info에 0을 11개 초기값 선언(중복 조합으로 화살 수가 바뀔 수 있어서 for문 안에 선언)
중복 조합을 for문 돌면서
lion_info에 화살 개수 넣는다
어피치와 라이언 점수를 0으로 선언
점수인 11만큼 돌면서
어피치 인덱스와 라이언 인덱스가 같고 그 값이 0이면
넘어 간다(이거 중요함, 안 써줘서 답이 달라짐)
어피치 인덱스가 라이언 인덱스가 같거나 크면
어피치에 점수를 넣고
라이언이 어피치보다 크면
라이언에 점수를 넣는다
라이언이 점수가 놓으면
라이언에서 어피치를 뺀 값이 점수 차가 되고
기존 정수 차보다 크면 기존 점수 차가 점수차이고 라이언 과녁은 answer 
'''