from math import gcd
def solution(w,h):
    return (w*h)-(w+h-gcd(w,h))

print(solution(8, 12))

'''
솔직히 생각 못 했는데
최대공약수 구하는 수학문제 였다...
gcd는 최대 공약수 구하는 math 라이브러리고
전체 정사각형 수에서 가로 새로 더한 값에서 최대공약수 빼면 멀쩡한 사각형 개수가 나옴
'''