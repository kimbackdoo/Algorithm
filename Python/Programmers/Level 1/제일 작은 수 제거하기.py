# def find_min(arr): # min 함수 구현
#     result = 99999
#     for a in arr:
#         if result > a:
#             result = a
    
#     return result

# def remove(arr): # remove 함수 구현
#     mn = find_min(arr)
#     result = []
#     for a in arr:
#         if a != mn: # 제일 작은 수를 빼고 리스트에 저장
#             result.append(a)
            
#     return result
    
# def solution(arr):
#     return [-1] if remove(arr) == [] else remove(arr)

# def solution(arr):
#     arr.remove(min(arr))
#     return [-1] if len(arr) == 0 else arr

def solution(arr):
    arr.remove(min(arr)) # remove 메소드 이용하여 제일 작은수 
    return arr if arr else [-1]
