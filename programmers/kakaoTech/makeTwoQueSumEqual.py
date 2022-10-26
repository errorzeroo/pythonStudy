def solution(queue1, queue2):
    answer = -1
    sumq1 = sum(queue1)
    sumq2 = sum(queue2)
    sumq = (sumq1+sumq2)//2
    idx1, idx2, length = 0, 0, len(queue1)
    while idx1 < 2*length and idx2 < 2*length and sumq1 != sumq2:
        if sumq1 < sumq:
            sumq1 += queue2[idx2]
            sumq2 -= queue2[idx2]
            queue1.append(queue2[idx2])
            idx2 += 1
        else:
            sumq1 -= queue1[idx1]
            sumq2 += queue1[idx1]
            queue2.append(queue1[idx1])
            idx1 += 1
    if sumq1 == sumq:
        answer = idx1 + idx2
    return answer

'''
방법이 하나도 생각이 안 나서 검색 해서 풀었다.(sum을 해야 하나 싶었는데 맞았다, pop순서를 생각 하느라 복잡 했는데 순서는 상관 없이 합만 비교 하는 거 같다)
초기 answer를 -1로 선언(합이 안될 때 즉 while을 안 돌 때 -1로 리턴 하려고)
queue1을 sum한 것, queue2를 sum한 것, 두개를 더하고 2로 나눈 것, queue1의 인덱스(0으로 시작), queue2의 인덱스(0으로 시작), 길이(두 큐의 길이는 같다.)
큐1의 인덱스가 길이*2보다 작고, 큐2의 인덱스가 길이*2보다 작고, 두 개를 sum이 같지 않을 때(같게 만들 거라서)
sumq가 sumq1보다 클 때
queue2의 idx2인덱스 값을 sumq1에 추가 하고(insert)
queue2의 idx2인덱스 값을 sumq2에서 빼준다(pop)
queue1에는 queue2의 idx2인덱스 값을 넣는다(insert)
idx2(queue2의 인덱스)를 1 높인다.
sumq가 sumq1보다 같거나 작을 때
queue1의 idx1인덱스 값을 sumq1에서 빼준다(pop)
queue1의 idx1인덱스 값을 sumq2에 추가 하고(insert)
queue2에는 queue1의 idx1인덱스 값을 넣는다(insert)
idx1(queue1의 인덱스)를 1 높인다.
sumq1와 sumq가 같을 때(원하는 sumq1 = sumq2가 됐을 때)
answer에 인덱스들의 합을 넣는다.(큐를 움직인 횟수들)
'''