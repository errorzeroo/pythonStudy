# 나무 자르기
num, namu = map(int, input().split())
nums = list(map(int, input().split()))
srt = 0
end = max(nums)
get_namu = 0
while srt <= end:
    mid = (srt + end) // 2
    namu_plus = 0
    for i in range(len(nums)):
        if nums[i] > mid:
            namu_plus += nums[i] - mid
            if namu_plus >= namu:
                break
    if namu_plus >= namu:
        srt = mid + 1
        get_namu = mid
    elif namu_plus < namu:
        end = mid - 1
    else:
        break
print(get_namu)

'''
나무의 숫자와 가져갈 나무의 길이를 인풋 받는다
나무 길이를 인풋 받아 리스트에 저장 한다.
srt 시작 값을 0으로, 끝값을 가장 큰 나무 길이로 초기화
최종 자를 나무의 길이(get_namu) 초기화
시작 값이 끝값과 같거나 작을 때 까지 반복문을 돌건데
중간값(자를값)의 처음은 시작 값과 끝값을 더한 것의 반이다.
비교할 나무의 길이(namu_plus)를 0으로 초기화

나무의 숫자만큼 for반복문을 돌건데 나무 길이의 리스트의 뭔소가 중간 값보다 크면
그 원소에서 중간 값을 뺀 값을 나무의 길이에 저장
최종 저장된 수가 나무 보다 클 때 for반복문 정지

저장된 나무 길이가 가저갈 나무 길이보다 크면
시작 값을 중간값 +1 한 숫자로 바꾸고 최종 가져갈 값에 중간값 저장

저장된 나무 길이가 가저갈 나무 길이보다 작으면
끝값을 중간 값보다 1 작은수로 저장

while문을 돌며 반복 하다가 저장된 나무 길이가 가져갈 나무 길이와 같으면
와일문 종료

저장된 나무의 길이 출력
'''