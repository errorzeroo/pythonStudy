from heapq import heappop, heappush
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            s1 = heappop(scoville)
            s2 = heappop(scoville)
            heappush(scoville, s1 + s2*2)
            answer += 1
    return answer

s=[1,2,3,9,10,12]
print(solution(s, 7))
'''
heapq의 heappop, heappush를 사용 했다.
처음 scoville를 sort하고
while문 scoville[0]이 K보다 작은 경우 돈다.
scville의 길이가 1보다 작거나 같을 때
-1를 리턴 하고 (K 이상으로 만들 수 없는 경우)
최소 값을 pop하는 heappop을 사용해서 없애면서 s1에 최소 값을 저장 하고
최소 값이 없어졌으니 그 다음 최소 값을 heappop으로 없애면서 s2에 저장 한다.
heappush로 s1 + s2*2를 scoville에 넣는다.

heappush는 최소값을 맨 앞으로 가져오기 때문에 while문을 계속 돌릴 수 있고,
s1, s2로 최소값, 두번째 최소값을 넣어둬서 sort할 필요도 없다.

풀었는데 틀려서 어디가 틀린지 모르겠어서 검색하다 답을 봤다.
내가 푼건 for문으로 enumerate 써서 값이랑 인덱스를 가져 왔고
두번째 값에 섞은 것을 덮어 씌웠다. answer 올라갈 때마다 sort를 했는데
sort가 시간이 오래 걸려서 효율성에서 계속 시간 초과가 났다.
K 이상으로 만들 수 없는 경우 설정을 잘못 해줘서 런타임 에러(인덱스 에러)가 난게 몇 개 있었다.
코드를 덮어 써서 썼던 코드는 없고 기억 나는 대로 적는다.
'''