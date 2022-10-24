import sys
input = sys.stdin.readline
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, k = map(int, input().split())
mat = [[0 for _ in range(n)] for _ in range(n)]
q = deque()
for _ in range(k):
    s, e = map(int, input().split())
    q.append([s-1, e-1])

while q:
    x, y = q.popleft()
    mat[x][y] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:  # 해당 과정 대신에, 조건이 성립 하면 1을 더해도 된다.
            mat[nx][ny] += 1
ans = 0
for i in mat:
    ans += sum(i)
print(ans)

'''
length, num = map(int, input().split())
cnt = 0
for i in range(num):
    garo, sero = map(int, input().split())
    if garo == 1:
        if sero == 1 or sero == length:
            cnt += 3
        elif sero != 1 and sero != length:
            cnt += 4
    elif garo == length:
        if sero == 1 or sero == length:
            cnt += 3
        elif sero != 1 and sero != length:
            cnt += 4
    elif garo != 1 and garo != length:
        if sero == 1 or sero == length:
            cnt += 4
        elif sero != 1 and sero != length:
            cnt += 5
print(cnt)
내가 풀다 테스트 케이스 몇개 통과 못한거
위에 코드를 보니 deque를 사용 했다
'''