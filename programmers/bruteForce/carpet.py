def solution(brown, yellow):
    answer = []
    divisor = []
    if yellow == 1:
        return [3, 3]
    for div in range(1, yellow//2+1):
        if yellow % div == 0:
            divisor.append([div, yellow//div])
    for i in divisor:
        if i[0]*2 + i[1]*2 +4 == brown:
            answer.append(i[1]+2)
            answer.append(i[0]+2)
            break
    return answer

'''
약수를 구해줄 divisor 선언
yellow가 1일 때는 답이 3, 3일 수 밖에 없어서 [3, 3]로 리턴
yellow의 반까지 1부터 돌면서
yellow로 나누어 떨어지면 그 수와 몫을 리스트 형태로 divisor에 저장 한다.
divisor를 돌면서 테두리(brown)와 같을 때 answer에 넣고 멈춘다.
'''