def solution(priorities, location):
    cnt = 0
    while priorities:
        if location == 0:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                location = len(priorities) - 1
            else:
                return cnt + 1
        else:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
            else:
                priorities.pop(0)
                cnt += 1
            location -= 1
    return cnt

'''
max_idx = priorities.index(max(priorities))
idx = max_idx - 1
cnt = 0
if location > max_idx:
    return location - idx
elif location < max_idx:
    for c in range(max_idx):
        if priorities[location] < priorities[c] and location < c:
            cnt += 1
    return location + (len(priorities) - idx) + cnt
else:
    return 1
---풀던 건데 elif를 건드리면 풀 수 있을거 같긴 한데 찾아도 안 나와서 포기---

<검색한 풀이>근데 잘 모르겠다.
cnt를 0으로 선언 하고 priorities를 돌면서
요청 문서 인덱스가 첫번째 이고
priorities[0]이 max(priorities)보다 작을 때(더 높은 숫자가 있을 경우)
pop(0)로 빼내고 append로 맨 뒤로 보낸다.
맨 뒤로 보내서 요청 문서 인덱스를 맨 뒤에 숫자로 변경 한다.
더이상 우선 순위 없을 때(location이 제일 처음 우선 순위일 때) cnt + 1로 리턴
요청 문서 인덱스가 첫 번째가 아닐 때
priorities[0]이 max(priorities)보다 작을 때(더 높은 숫자가 있을 경우)
pop(0)로 빼내고 append로 맨 뒤로 보낸다.
우선 순위 값이 0번째 있을 때 pop(0)로 빼내고 cnt를 하나 올린다.
pop으로 인덱스가 밀려서 location -= 1을 한다.
cnt로 리턴
'''