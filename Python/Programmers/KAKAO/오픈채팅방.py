# 최종적으로 방을 개설한 사람이 보게 되는 메시지를 출력하는 것이므로 key가 유저아이디, value가 닉네임으로 이루어진 dict 생성
# 이후 최종 변환된 닉네임을 저장

def solution(record):
    answer = []
    user = {} # 유저아이디와 닉네임이 저장될 dict
    for r in record:
        r = r.split(" ") # 공백을 기준으로 split
        if r[0] in ["Enter", "Change"]: # r[0]가 Enter, Change 중 하나라면
            user[r[1]] = r[2] # user에 저장 즉, 제일 마지막에 변하는 닉네임이 최종 닉네임
    
    for r in record:
        r = r.split(" ")
        # 문제 조건에 맞게 출력
        tmp = "{}님이 ".format(user[r[1]])
        if r[0] == "Enter":
            answer.append(tmp + "들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(tmp + "나갔습니다.")

    return answer
