def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    set(report)
    duplicate = [0 for i in range(len(id_list))]
    for i in report:
        temp = i[i.find(' ')+1:]
        for j, idx in enumerate(id_list):
            if j == temp:
                duplicate[idx] = +1
                break
    for cnt in len(duplicate):
        if cnt >= k:
            id_list[cnt]
    return answer