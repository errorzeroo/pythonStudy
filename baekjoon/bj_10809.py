# alpha = input()
# word = []
# for i in range(alpha):
#     if alpha in word:
#         print(alpha[i])
#     else:
#         print(-1)
# 알파벳 찾기
from string import ascii_lowercase  # 아스키코드 임포트
S = list(input().lower())           # 단어 인풋
for i in ascii_lowercase:           # 아스키 코드 만큼 돈다
    if i in S:
        print(S.index(i), end=' ')  # 아스키 코드 안에 있으면 인덱스 번호 출력
    else:
        print(-1, end=' ')          # 아니면 -1 출력