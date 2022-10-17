from itertools import permutations
def solution(numbers):
    answer = []
    num_list = [n for n in numbers]
    per = []
    for i in range(1, len(numbers)+1):
        per += list((permutations(num_list, i)))
    nums = set([int(("").join(p)) for p in per])
    for num in nums:
        check = True
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    check = False
                    break
            if check:
                answer.append(num)
    return len(answer)

'''
경우의 수 구하기가 어려워서 검색 해서 순열 사용 하는 답을 찾아서 보면서 했다. 

itertools의 permutations(순열)을 사용 했다.
answer를 리스트로 선언 하고
numbers에서 문자열 하나씩 가져와 num_list에 넣고
per 빈 리스트를 만들어 permutations로 하나씩 추가 한다.
(append로 넣어 봤는데 순열이 제대로 들어 가지 않았다.)
새로운 리스트에 순열로 들어간 애들을 ""문자 기준으로 join 해서 정수로 만들고 중복을 없애려고 set을 했다.

nums를 돌면서 소수를 체크 하려고 True 초기 값을 설정 하고
num이 1보다 클 때 2부터 num의 루트까지 돌면서
num으로 나눈 i가 나누어 떨어질 때 check를 False로 바꾸고 소수가 아니니까 for문 break 한다.
그리고 check가 True일 때 answer에 append 한다.
answer의 길이로 리턴 
'''