# numbers = [4, 1, 2, 1]
# target = 4
count = 0
def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return count


def dfs(idx, current, numbers, target):
    global count
    if idx == len(numbers):
        if current == target:
            count += 1
    else:
        dfs(idx+1, current + numbers[idx], numbers, target)
        dfs(idx+1, current - numbers[idx], numbers, target)

'''
count는 최종 값
current는 최종 값을 구하기 위한 변수
numbers는 주어진 리스트(배열)
target은 주어진 목표 값
idx는 numbers의 인덱스

dfs 깊이 우선 탐색 알고리즘

if 코트 해석: idx가 numbers 길이와 같아질 때 인덱스 번호가 초과될 때,
current와 target이 같으면 최종 count 값을 올린다
인덱스 번호(idx)가 number 길이와 같지 않으면,
인텍스 번호를 하나 올리고 current에 numbers의 인덱스 번호 값을 더하거나 빼준다
'''