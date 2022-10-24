def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report = list(set(report))
    report_dict = {i: [] for i in id_list}
    for r in report:
        r = r.split()
        report_dict[r[1]].append(r[0])

    for ck, val in report_dict.items():
        if len(val) >= k:
            for v in val:
                answer[id_list.index(v)] += 1
    return answer

'''
def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report = list(set(report))
    report_split = []
    check_list = [0 for i in range(len(id_list))]
    for r in report:
        report_split.append(r.split())
    for cnt in report_split:
        for idx, check in enumerate(id_list):
            if cnt[1] == check:
                check_list[idx] += 1
                break

    cnt = []
    for i, j in enumerate(check_list):
        if j >= k:
            cnt.append([id_list[i], j])
    for ck in report_split:
        for c in cnt:
            if ck[1] == c[0]:
                answer[id_list.index(ck[0])] += 1
                break
    return answer
3번만 시간 초과 나는 풀이 리스트로 풀어보려 했음

나랑 로직은 비슷한데 딕셔너리로 푼거 가져 옴
answer에 id_list만큼 0으로 초기화 하고
report의 중복값을 set을 통해 제거 하고
report_dict에 key값에 id_list를 value에는 빈 리스트를 만든다.
report를 돌면서 split으로 쪼갠 값을
신고 당한 사람[1]을 key에 신고 한 사람[0]을 value에 리스트로 넣는다.
items()를 이용해 key, value를 가져 와서
val이 k보다 클때만
for문을 val로 돌고,
index()를 이용해 id_list의 인덱스에 1을 더한다.

시간 완전 단축됨 일단 전체에서 k이상인 값만 for문을 따로 도는건 생각 못함
그리고 나는 숫자로 가져 와서 반복문을 많이 돌아야 했는데(3중을 2중으로 줄인것) 또 모든 값을 봐서 시간이 오래 걸렸는데
이름으로 가져오니까 반복문 돌기에도 편했다.
'''