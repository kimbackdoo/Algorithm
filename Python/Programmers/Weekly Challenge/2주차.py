# 문제에 나온대로 구현
# 평균을 구할 때 행 단위로 평균을 구하는 것이 아니라 열 단위로 평균을 구해야함
# 따라서 행과 열을 바꿔 리스트를 생성하고 본인 점수가 유일한 최고점 또는 최저점이라면 제외하고 평균을 구함

# def grade(score): # 각 점수에 따른 학점 함수
#     if score >= 90: return "A"
#     elif 80 <= score < 90: return "B"
#     elif 70 <= score < 80: return "C"
#     elif 50 <= score < 70: return "D"
#     else: return "F"

# def solution(scores):
#     answer = ""
#     for i in range(len(scores[0])):
#         tmp = [score[i] for score in scores] # 열을 기준으로 리스트 생성
#         if (tmp[i] == max(tmp) or tmp[i] == min(tmp)) and tmp.count(tmp[i]) == 1: # 본인 점수가 최고점 또는 최저점이고, 유일하면
#             avg = (sum(tmp) - tmp[i]) / (len(tmp) - 1) # 본인 점수를 제외하고 평균을 구함
#             answer += grade(avg) # 평균에 따른 학점을 answer에 더함
#             continue
            
#         avg = sum(tmp) / len(tmp) # 아니라면 전체 평균을 구함
#         answer += grade(avg) # 평균에 따른 학점을 answer에 더함
        
#     return answer

# 학점을 계산할 때 if문 대신 dict으로 순회를 돌면서 계산하는 걸로 수정

# def grade(score): # 학점 계산 함수
#     rank = {90: "A", 80: "B", 70: "C", 50: "D"} # 점수에 따른 학점 dict
#     for key, value in rank.items(): # rank를 순회하면서 score가 key보다 크거나 같으면 key에 해당하는 value 반환
#         if score >= key:
#             return value
        
#     return "F" # rank에 점수가 없으면 F 반환

# def solution(scores):
#     answer = ""
#     for i in range(len(scores[0])):
#         tmp = [score[i] for score in scores]
#         if (tmp[i] == max(tmp) or tmp[i] == min(tmp)) and tmp.count(tmp[i]) == 1:
#             avg = (sum(tmp) - tmp[i]) / (len(tmp) - 1)
#             answer += grade(avg)
#             continue
            
#         avg = sum(tmp) / len(tmp)
#         answer += grade(avg)

#     return answer

# 학점을 계산할 때 함수를 따로 선언하지 않고, "FFFFFDDCBAA" 문자열을 이용하여 계산

def solution(scores):
    answer = ""
    for i in range(len(scores[0])):
        tmp = [score[i] for score in scores]
        if (tmp[i] == max(tmp) or tmp[i] == min(tmp)) and tmp.count(tmp[i]) == 1: # 본인의 점수가 유일한 최고점 또는 최저점이라면
            avg = (sum(tmp) - tmp[i]) / (len(tmp) - 1) # 본인 점수를 제외하고 평균 계산
        else: # 아니라면
            avg = sum(tmp) / len(tmp) # 전체 평균 계산
            
        answer += "FFFFFDDCBAA"[int(avg) // 10] # 학점 계산, 문자열이 길이가 10이므로 평균의 소수 부분을 자르고 10으로 나눈 몫으로 학점을 찾음
        
    return answer
