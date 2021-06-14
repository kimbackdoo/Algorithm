# def sort(arr): # 정렬 구현
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
    
#     return arr

# def solution(arr, divisor):
#     answer = [num for num in arr if num % divisor == 0] # divisor로 나눠지는 숫자만 answer 리스트 생성
#     return [-1] if len(answer) == 0 else sort(answer) # 나눠지는 숫자가 없다면 -1 아니면 answer 정렬

def solution(arr, divisor):
    return sorted([a for a in arr if a % divisor == 0]) or [-1] # or을 사용해 나눠지는 숫자 리스트 또는 [-1]을 
