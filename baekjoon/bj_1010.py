# 다리 놓기
import sys
num = int(sys.stdin.readline())
def combination(west, east):
    parent = 1
    child = 1
    factorial = 1
    for iii in range(1, east+1):
        parent *= iii
    for j in range(1, east-west+1):
        child *= j
    for k in range(1, west+1):
        factorial *= k
    bridge = parent//(child*factorial)
    return bridge
for i in range(num):
    west, east = map(int, sys.stdin.readline().split())
    print(combination(west, east))

'''
인풋 말고 시스템에서 불러오려고 sys 임포트
조합 함수를 만든다
분모, 분자, 팩토리얼을 1로 리셋 시키고
각각 팩토리얼을 for문을 돌린다.
bridge 변수에 조합을 위한 변수들을 넣고
리턴을 bridge로 한다.
입력 받은 테스트 케이스(num)별로 for문을 도는데
강 서쪽과 강 동쪽을 입력 받아서
조합 함수로 출력 한다.
'''