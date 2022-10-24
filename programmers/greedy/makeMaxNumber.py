def solution(number, k):
    answer = []
    for i in number:
        if not answer:
            answer.append(i)
            continue
        while answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        answer.append(i)
        if len(answer) == len(number) - k:
            break
    return ''.join(answer)

'''
방법도 생각 안 나고 집중도 안 되서 푸는 것에 의의를 뒀다.(그래서 리뷰도 나중에함)

빈배열 받는다.
number를 돌면서 answer가 아니면 answer에 i를 추가 한다.
for문 안에서 while문이 도는데 answer에 마지막 숫자가 i보다 크고, k가 0보다 클 때
answer의 마지막을 삭제 한다.
k를 줄이고
answer가 아니거나 k가 0이거나 음수일 때
while을 멈춘다.
answer에 i를 넣고 answer의 길이와 number에서 k를 뺀 길이가 같을 때
for문을 멈춘다.
answer을 join으로 묶은 값을 리턴
'''