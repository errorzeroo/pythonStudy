x, y, w, h = map(int, input().split())
print(min(w-x, h-y, x-0, y-0))
# (x, y)에서 직사각 형 (0, 0) (w, h)의 경계선 까지 최소 거리 구하기
