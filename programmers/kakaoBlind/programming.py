def solution(today, terms, privacies):
    answer = []
    date = [0 for i in range(len(privacies))]
    period = [0 for i in range(len(privacies))]
    for idx, i in enumerate(privacies):
        date[idx] = i[:10].split('.')
        for j in terms:
            if j[0] == i[-1]:
                period[idx] = int(j[-1])
                break

    for i in range(len(date)):
        month = period[i] + int(date[i][1])
        if month > 12:
            date[i][0] = str(int(date[i][0]) + month // 12)
            hap = int(date[i][1]) + month % 12
            if hap > 12:
                temp = hap - 12
                if temp < 10:
                    date[i][1] = '0' + str(temp)
                else:
                    date[i][1] = str(temp)
                date[i][0] = str(int(date[i][0]) + 1)
            elif hap < 10:
                date[i][1] = '0' + str(hap)
            else:
                date[i][1] = str(hap)
        elif month < 10:
            date[i][1] = '0' + str(month)
        else:
            date[i][1] = str(month)

    for idx, i in enumerate(date):
        if today[0:4] > i[0]:
            answer.append(idx+1)
        elif today[0:4] == i[0]:
            if today[5:7] > i[1]:
                answer.append(idx+1)
            elif today[5:7] == i[1]:
                if today[8:] >= i[2]:
                    answer.append(idx+1)
    return answer

today = '2022.05.19'
terms = ['A 6', 'B 12', 'C 3']
privacies = ['2021.05.02 A', '2021.07.01 B', '2022.02.19 C', '2022.02.20 C']

print(solution(today, terms, privacies))

# month가 12일경우, hap이 12일경우, temp가 12일경우