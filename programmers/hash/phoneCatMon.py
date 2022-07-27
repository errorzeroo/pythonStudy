def solution(nums):
    sel_nums = len(nums)//2
    set_nums = set(nums)
    if sel_nums <= len(set_nums):
        return sel_nums
    else:
        return len(set_nums)

'''
set을 써서 nums안의 값의 종류를 계산
그 값이 뽑아야하는 개수랑 비교를 하여 더 작은 값을 리턴
'''