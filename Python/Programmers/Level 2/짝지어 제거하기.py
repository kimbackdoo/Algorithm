# def solution(s):
#     answer = []
#     for word in s:
#         if answer and answer[-1] == word: # answer가 비어있지 않거나 answer[-1]이 word와 같다면
#             answer.pop() # answer에서 마지막 값 pop
#             continue
            
#         answer.append(word) # 그렇지 않으면 word append
    
#     return 1 if len(answer) == 0 else 0

def solution(s):
    answer = []
    for alpha in s:
        if answer and answer[-1] == alpha:
            answer.pop()
            continue
        
        answer.append(alpha)
    
    return 0 if answer else 1 # answer가 비어 있지 않으면 0, 비어 있으면 1 return
