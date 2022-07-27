def solution(array, commands):
    kTH = []
    for idx in range(len(commands)):
        cmd_a = sorted(array[commands[idx][0]-1:commands[idx][1]])
        kTH.append(cmd_a[commands[idx][2]-1])
    return kTH


'''
array는 주어진 배열
commands는 끊어낼 i j 정렬 후 구할 k가 담긴 리스트
kTH는 최종 k번째수 리스트
cmd_a는 정렬된 리스트

코드 해석:
idx가 commands의 길이만큼 돌건데
array에서 commands의 idx번째의 0번째 값에서 하나 작은 값에서
commands의 idx번째의 1번째 값을 슬라이싱한 것을 정렬하여 cmd_a에 저장한다
cmd_a에서 commands의 idx번째의 2번째 값에서 하나 작은 값을 kTH리스트에 저장

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])

처음 idx가 돌 때 idx는 0이어서 [2, 5, 3]을 가리키고 거기에 0번째는 2, 1번째는 5,
2번째는 3이다.

리스트는 0번째부터 세기 때문에 2에서 5까지를 슬라이싱 하려면 2-1번째로 해줘야함
슬라이싱 할 때 마지막 전까지 슬라이싱하기 때문에 뒤에값은 -1 할 필요 없음 
'''