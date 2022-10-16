from collections import deque
global dx, dy, visited
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    global visited
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    return bfs(maps)


def bfs(maps):
    global dx, dy
    queue = deque()
    queue.append([0, 0])

    while queue:
        p = queue.popleft()
        row = p[0]
        col = p[1]

        if row == len(maps) - 1 and col == len(maps[0]) - 1:
            return maps[row][col]

        for i in range(4):
            nr = row + dy[i]
            nc = col + dx[i]

            if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and maps[nr][nc] == 1:
                queue.append([nr, nc])
                maps[nr][nc] = maps[row][col] + 1
    return -1

s=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
x=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(x))
'''
알고리즘 자체를 정확히 이해 하지 못했고, 푸는 방법도 어려워서 많이 검색 해서 답을 구하였다.

collections 패키지에서 deque를 사용 한다.
글로벌 변수로 dx, dy, visited를 선언 한다.
좌우 배열 dx와 상하 배열 dy를 선언
글로벌 visited를 받아서 maps의 가로 세로 길이만큼 초기 값을 세팅 한다.

bfs 함수
글로벌 dx, dy를 가져 오고
queue에 deque()함수를 선언
초기 값으로 [0, 0]을 넣고
(bfs가 solution 안일 경우 (x, y) 로 받고 x, y=popleft()해도 된다)
queue가 빌 때까지 반복을 한다

p = queue.popleft(), row = p[0], col = p[1]
if row == len(maps)-1 and col == len(maps[0])-1:
return maps[row][col]

새 변수 nx와 ny에 row+dx[i], col+dy[i]로 상하 좌우 칸을 확인 한다.
nx의 범위가 0부터 가로 길이 사이 이고, ny의 길이가 0부터 세로 길이 사이 이고, 위치 값이 1일때
queue에 nx, ny를 넣고 maps[nx][ny]에 maps[row][col] + 1 값을 넣는다.(거리 계산)
(다른 방법인데 조금 비효율)
if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue
맵을 벗어 나는 경우 무시
if maps[nx][ny] == 0:  continue 벽이면 무시
if maps[nx][ny] == 1:  처음 지나는 길 일경우
maps[nx][ny] = maps[x][y] + 1 거리 계산
queue.append((nx, ny)) 상하 좌우 확인

-1로 리턴 하는 경우는 목표 지점에 도달 하지 못할 경우
'''