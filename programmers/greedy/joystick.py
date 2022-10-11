def solution(name):
    answer = 0
    alpha = "ABCDEFGHIJKLM"
    ahpla = "ZYXWVUTSRQPON"
    curser = len(name)-1

    for i, j in enumerate(name):
        if j in alpha:
            answer += alpha.index(j)
        elif j in ahpla:
            answer += ahpla.index(j)+1

        idx = i + 1
        while idx < len(name) and name[idx] == "A":
            idx += 1
        curser = min(curser, i*2+len(name)-idx, (len(name)-idx)*2+i)

    answer += curser
    return answer

'''
alpha에 알파벳 앞부분, ahpla에 알파벳 Z에서 N까지 정의하고,
for문 돌면서 alpha나 ahpla에 인덱스를 answer에 추가
(A는 0이 맞는데 Z는 1이어야 해서 +1 해줌)

커서는 어려워서 조언을 받았다

cuser는 name길이 보다 작은 값을 초기 값으로 놓고
idx를 1부터 세려고 i+1을 해준 뒤
idx가 name 길이 보다 작을 때와 A를 만나기 전까지 while문 돌며 idx를 1씩 누적 한다
원래 cuser값과, A전에 커서가 있을 때
앞을 왕복(*2)하고 뒤를 더한 값과,
뒤를 왕복(*2)하고 앞을 더한 값의 최소 값을 cuser에 리셋
answer에 cuser를 더해 준다.
'''