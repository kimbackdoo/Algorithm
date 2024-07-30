def gradingStudents(grades):
    tmp = []
    
    for i in range(len(grades)):
        tmp.append(grades[i])

        if grades[i] < 38: continue
        for _ in range(1, 5):
            if tmp[i]%5 != 0: tmp[i] += 1
            else: break

        if tmp[i]-grades[i] < 3: grades[i] = tmp[i]

    return grades

# 코드의 시간 복잡도가 높아 수정
# 5로 나누었을 때 나머지가 3이상이면 조건 만족
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38: continue
        elif grades[i]%5 >= 3:
            grades[i] = grades[i] + (5-grades[i]%5)

    return grades