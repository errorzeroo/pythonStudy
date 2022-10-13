# 수 찾기
from sys import stdin
num = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
find_num = int(stdin.readline())
find_nums = list(map(int, stdin.readline().split()))
nums.sort()
for i in find_nums:
    start = 0
    end = num
    is_num = 0
    if i > nums[-1]:
        print(is_num)
    else:
        while start <= end:
            mid = (start + end) // 2
            if i > nums[mid]:
                start = mid + 1
            elif i < nums[mid]:
                end = mid - 1
            elif i == nums[mid]:
                is_num = 1
                break
        print(is_num)

'''
input()보다 빠른 sys를 불러오고
입력 받을 숫자 num
num의 수만큼 받은 숫자 리스트로 저장
찾을 숫자 find_num
find_num의 수만큼 받은 숫자 리스트로 저장
nums에 있는지 볼 거니까 sort시키고
find_nums를 돌면서 있는지 확인하는데
start와 end, 출력할 is_num 선언
비교할 수 i가 nums의 마지막 수보다 크면 없는 거니가 0 출력
start가 end보다 커지기 전까지 while문 돌건데
mid는 start+end를 2로 나눈 것의 몫이고
i가 nums[mid]보다 크면 start를 mid+1로 변경(이분탐색 중간 값보다 크면 중간 위를 봄)
i가 nums[mid]보다 작으면 end를 mid-1로 변경(중간 값보다 작으면 중간 아래를 봄)
i가 nums[mid]이면 있는 거니까 is_num을 1로 바꾸고 반복문 나가고 is_num 출력

nums 안에 있는지 보는 거기 때문에 nums[mid]로 했어야 했는데 계속 mid로 해서 여러번 틀림
'''