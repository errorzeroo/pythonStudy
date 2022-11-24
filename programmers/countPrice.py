def solution(price, money, count):
    cnt = 0
    for c in range(1, count+1):
        cnt += price * c
    if cnt - money > 0:
        return cnt - money
    else:
        return 0

print(solution(3, 20, 4))