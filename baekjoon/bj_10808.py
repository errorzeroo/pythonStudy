# 알파벳 개수
words = input()                 # 문자열 인풋 받는다
cnt = [0 for i in range(26)]    # 알파벳 숫자만큼 초기값 0으로 리스트 만든다
for w in words:                 # word를 돌면서
    cnt[ord(w)-97] += 1         # 해당 알파벳 인덱스에 1을 더한다
for c in cnt:                   # cnt를 돌며
    print(c, end=' ')           # 알파벳 개수 출력
