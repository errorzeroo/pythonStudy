def solution(d, budget):
    answer = len(d)
    hap = sum(d)
    idx = 0
    d.sort(reverse=True)
    while answer > 0:
        if hap > budget:
            answer -= 1
            hap -= d[idx]
            idx += 1
        else:
            break
    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))

'''
pop 해서 숏 코드로 해결한 걸 봤는데 신셰계였음
hap에서 idx를 빼는 방법으로 해결
hap이 budget보다 작거나 같으면 while문 나감
'''