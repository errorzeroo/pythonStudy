# 동전 0
import sys
coins, price = map(int, sys.stdin.readline().split())
coin_list = []
for i in range(coins):
    coin = int(sys.stdin.readline())
    if coin <= price:
        coin_list.append(coin)
coin_list.sort(reverse=True)
cnt = 0
for j in coin_list:
    if price >= j:
        num = price//j
        price -= j*num
        cnt += num

print(cnt)

'''
시스템에서 인풋 받으려고 선언
코인 개수와 코인으로 만들 가격을 입력 받음
코인 비교할 리스트 생성
for문으로 코인 개수만큼 돌려서 코인을 입력 받음
코인이 가격보다 작거나 같으면 리스트에 넣어줌
리스트를 내림차순으로 정렬해주고
코인 개수를 셀 cnt 변수를 0으로 세팅

(이렇게 하면 시간 초과 남-이중 반복문
for c in coin_list:           리스트를 for문으로 돌건데
    while 1:                  무한 루프 while 문에서
        if price - c >= 0:    가격에서 현재 리스트의 값을 뺀게 0보다 같거나 크면
            cnt += 1          cnt를 1 올리고
            price = price-c   가격을 뺀 값으로 변경 한다.
        else:                 뺀 가격이 음수면
            break             와일문을 빠져나옴
    if price == 0:            가격이 0이되면
        break                 for문도 빠져 나온다.
pypy3에서는 성공)

(이렇게 해도 시간 초과 남-무한 루프 반복문
idx = 0                              coin_list 의 인덱스를 셀 변수 idx 선언
while 1:
    if price - coin_list[idx] >= 0:  price-coin_list의 idx값이 0이거나 크면
        cnt += 1                     cnt를 1 올리고
        price = price-coin_list[idx] price를 price-coin_list[idx]로 변경
    elif price == 0:                 price가 0이 될 때까지
        break
    else:                            price-coin_list[idx]가 음수이면
        idx += 1                     idx를 1 올림
pypy3에서는 성공)
for j in coin_list:     for문을 coin_list로 돌건데
    if price >= j:      price가 j보다 클 때
        num = price//j  num을 price에서 j로 나눈 몫으로 선언
        price -= j*num  price를 price에서 j*num을 뺀 가격으로 변경
        cnt += num      cnt에 num을 더함
    elif price == 0:    price가 0일 때
        break           for문 빠져나감
coin을 센 cnt출력

구글링 해서 얻은 답
몫을 새 변수에 넣어서(num = price//j)
그만큼 곱한 값을 뺀다는 건 생각도 못함(price -= j*num)
'''