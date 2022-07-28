def solution(n, lost, reserve):
    lost.sort()
    for i in lost.copy():
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    ex_class = n - len(lost)
    for i in lost:
        if i - 1 in reserve:
            ex_class += 1
            reserve.remove(i-1)
        elif i + 1 in reserve:
            ex_class += 1
            reserve.remove(i+1)
    return ex_class

# def solution(n, lost, reserve):
#     answer = 0
#     reserve.sort()
#     lost.sort()
#     for i in lost.copy():
#         if i in reserve:
#             reserve.remove(i)
#             lost.remove(i)
#
#     for i in range(n):
#         if i+1 not in lost:
#             answer += 1
#         elif i in reserve:
#             answer += 1
#             reserve.remove(i)
#         elif i+2 in reserve:
#             answer +=1
#             reserve.remove(i+2)
#         else:
#             pass
#
#     return answer

'''
n은 학생수, lost는 체육복을 읽어버린 학생, reserve는 여분 옷을 가져온 학생
여분 옷을 가져온 학생이 잃어버렸으면 잃어버린 곳과 여분에서 빼기(pop은 안됨)
뺄 때 for문 도는 개수가 달라져서 copy를 사용
최종 답이 ex_class, ex_class에서 lost의 길이를 뺀 값
lost를 돌면서 여분 옷을 줄 수 있는 학생을 뺀다(pop은 인덱스를 봐야 해서 안됨)

잃어버린 학생이 sort가 안 된 경우에 테스트를 통과하지 못함

문제 조건이 여분 옷을 줄 수 있는 사람이 +1이거나 -1 이거나였음

주석 처리된 것은 lost를 보지 않고 학생 수를 돌면서 i는 0부터 시작하니까
i+1이 현재 학생이고 그게 lost에 없으면 최종 답에 추가
i가 현재 학생보다 -1이고 i+2가 현재 학생보다 +2이다

학생 수를 돌면서 lost를 봐서 이미 sort된 상태라 따로 해줄 필요가 없음
'''