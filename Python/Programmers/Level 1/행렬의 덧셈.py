# def solution(arr1, arr2):
#     answer = []
#     for i in range(len(arr1)):
#         tmp = []
#         for a, b in zip(arr1[i], arr2[i]): # zip을 이용하여 묶고 합을 계산
#             tmp.append(a+b)
        
#         answer.append(tmp)
    
#     return answer

# def solution(arr1, arr2):
#     answer = []
#     for i in range(len(arr1)):
#         temp = []
#         for j in range(len(arr1[i])):
#             temp.append(arr1[i][j] + arr2[i][j]) # 하니씩 더함
#         answer.append(temp)
    
#     return answer

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j] # arr1이나 arr2에 행렬 덧셈 값을 바로 저장
            
    return arr1
