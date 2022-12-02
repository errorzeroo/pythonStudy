def solution(left, right):
    answer = 0
    cnt = 0
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
            cnt = 0
        else:
            answer -= i
            cnt = 0
    return answer

print(solution(13, 17))
print(solution(24, 27))

'''
이렇게 이중 포문으로 하는 것 보다 던 쉬운 방법이 있었다.
어떤 수의 제곱인 수는 약수의 개수가 홀수이고(4, 9, 16, 25등)
나머지 수는 약수의 개수가 짝수이다.

다른 사람 풀이 보고 처음 안 사실.
제곱근을 표현 하는 방법은 **0.5가 있고, math 라이브러리에 sqrt가 있다.
'''