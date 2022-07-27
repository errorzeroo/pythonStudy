test_case = int(input())
for i in range(test_case):
    rule = input()
    for idx, j in enumerate(rule[1:]):
        if rule[0] == rule[idx]:
            pattern = rule[:idx]
            if pattern == rule[idx:idx+len(pattern)] and len(pattern) != 0:
                print('#', i+1, ' ', len(pattern), sep='')
                break

'''
문장을 수행할 테스트케이스를 받는다
테스트 케이스만큼 반복문 돈다
문자열을 받는다
문자열의 인덱스, 값을 두번째 값부터 받는다
첫번째 문자열과 같은 값이 나왔을 때,
첫번째 문자열부터 같은 값의 전까지를 패턴에 저장한다
패턴과 패턴의 길이만큼의 값(idx+len(pattern))이 같을 때, 패턴이 0일때는 고려하지 않는다.
패턴의 길이를 출력
반복문 멈춤
'''