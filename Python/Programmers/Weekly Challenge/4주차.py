# languages와 preference을 이용하여 table 안에 각 직군 별로 languages에 해당하는 점수를 더하면 됨

# def solution(table, languages, preference):
#     answer = {} # 결과를 저장할 dict
#     for t in table:
#         tmp = t.split(" ") # 직군과 언어를 분리
#         answer[tmp[0]] = 0 # answer에 직군을 key로 설정하고 초기값 0으로 설정
#         for i in range(len(languages)):
#             try:
#                 # 해당 직군의 값에서 (언어 점수 * 선호도)을 더함, 결국 해당 직군에서 모든 languages의 점수의 합을 구함
#                 # 언어에서 index 메소드를 이용하여 languages[i]의 값의 인덱스를 찾음, 이때 언어에 languages[i]가 없으면 오류 발생하므로 try, except 구문 이용
#                 answer[tmp[0]] += ((5 - tmp[1:].index(languages[i])) * preference[i])
#             except:
#                 continue
        
#     return sorted(answer.items(), key=lambda x : (-x[1], x[0]))[0][0] # 점수를 기준으로 내림차순, 점수가 같을 경우 직군을 기준으로 오름차순한 리스트의 직군을 return

def solution(table, languages, preference):
    score = dict(zip(languages, preference)) # 미리 언어에 해당하는 선호도 dict을 구함, languages의 요소가 key, preference의 요소가 value가 됨
    answer = {}
    for t in table:
        tmp = t.split(" ")
        answer[tmp[0]] = 0 # answer에 직군을 key로 설정하고 초기값 0으로 설정
        for idx, language in enumerate(tmp[1:]): # enumerate을 이용하여 언어와 인덱스를 구함
            if language in score: # 언어가 score에 있으면
                answer[tmp[0]] += (5 - idx) * score[language] # 언어의 점수를 구하고 해당 직군의 값을 더해나감, 이렇게 하여 해당 직군의 총 점수를 구함
                
    return sorted(answer.items(), key=lambda x : (-x[1], x[0]))[0][0]
