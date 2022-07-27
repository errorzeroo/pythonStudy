# 제로
test_num = int(input())        # 숫자 개수 인풋
num_list = []
for i in range(test_num):
    num = int(input())         # 숫자를 인풋 받음
    if num != 0:               # 인풋 받은 숫자가 0이 아니면
        num_list.append(num)   # 리스트에 저장
    else:
        num_list.pop()         # 0이면 저장된 리스트의 맨 마지막 수 지움
print(sum(num_list))