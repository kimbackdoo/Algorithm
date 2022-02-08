# def solution(arr):
#     answer = []
#     for i in range(len(arr)-1):
#         if arr[i] != arr[i+1]: # arr[i]가 다음 요소랑 다를 경우에만 이유는 다른 경우가 아니라면 모두 같다는 뜻이므로
#             answer.append(arr[i])
    
#     # 위 for문에서 len(arr)-1까지만 반복하므로 arr 마지막 요소는 확인을 안함
#     answer.append(arr[-1])  # 따라서 arr 마지막 요소 answer에 추가
    
#     return answer

# def solution(arr):
#     answer = []
#     for a in arr:
#         if answer[-1:] == [a]: continue # answer 마지막 요소랑 a랑 비교해서 같으면 continue,
#         answer.append(a) # 다르면 answer에 append

#     return answer

def solution(arr):
    answer = [arr[0]] # arr의 첫번째 요소 answer에 저장
    for a in arr:
        if answer[-1] != a: # answer[-1]과 a가 같지 않으면 append
            answer.append(a)
    
    return answer
