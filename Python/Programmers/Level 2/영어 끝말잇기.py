# 끝말잇기 규칙 그대로 적용
# 그 전 사람의 마지막 단어가 다음 사람의 첫 단어랑 일치해야하고, 이전에 말한 단어를 또 말하면 안된다

# def solution(n, words):
#     tmp = [words[0]] # 비교할 리스트인 tmp를 선언하고 words의 첫번째 요소를 저장
#     for i in range(1, len(words)):
#         if tmp[-1][-1] == words[i][0]: # tmp의 마지막 단어와 현재 첫 단어가 일치하면
#             if words[i] not in tmp: # 이전에 말한 단어를 또 말하지 않았으면 append
#                 tmp.append(words[i])
#             else: # 이전에 말한 단어를 또 말했으면 [번호, 차례] 반환
#                 return [i % n + 1, i // n + 1]
#         else: # tmp의 마지막 단어와 현재 첫 단어가 일치하지 않으면 [번호, 차례] 반환
#             return [i % n + 1, i // n + 1]
    
#     return [0, 0] # 중간에 반환되지 않으면 탈락하는 사람이 없다는 뜻이므로 [0, 0] 반환

def solution(n, words):
    check = [words[0]] # 첫 번째 단어 저장
    for i in range(1, len(words)): # words 크기만큼 반복
        # 전 단어의 마지막 글자가 현재 첫 번째 글자와 다르거나 이미 말한 것을 또 말한 경우
        if words[i-1][len(words[i-1])-1] != words[i][0] or words[i] in check:
            return [(i%n) + 1, (i//n) + 1]
        
        check.append(words[i])
        
    return [0, 0]
