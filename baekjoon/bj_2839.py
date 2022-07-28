# 설탕 배달
sugar = int(input())                       # 설탕의 무게 인풋
delivery = -1                              # 최종 정답 -1 초기화
for i in range(sugar//5, -1, -1):          # 설탕에서 5를 나눈 몫에서 -1씩 0까지 for문
    if (sugar - i*5) % 3 == 0:             # 설탕에서 5를 나눈 값을 빼고 3으로 나눠지는지 확인
        delivery = i + (sugar - i*5)//3    # 나눠지면 3의 몫까지 합한 값이 정답
        break
print(delivery)

'''
포인트 : 5를 먼저 쓰는게 적게 사용 하니까 5로 나누어 줌
포인트 : i가 5의 몫이니까 i*5는 처음 값에서 설탕을 사용한 양
포인트 : sugar- i*5에서 나머지 3을 사용할 양을 구함
'''