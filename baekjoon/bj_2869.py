from sys import stdin
from math import ceil
up, down, meter = map(int, stdin.readline().split())
day = (meter - down) / (up - down)
print(ceil(day))

'''
마지막으로 내려갔다가 올라오는 걸 방지하기 위해 미리 내려갈 수를 빼고(meter - down),
미끄러진 것 까지 계산 하여(up - down) 나눈다.
나머지를 올려서 계산 해야 미끄러짐 없이 올라간 것
'''