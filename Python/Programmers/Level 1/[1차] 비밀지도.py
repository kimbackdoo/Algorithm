# def binary(num, n): # 이진수 변환
#     result = []
#     while num > 0:
#         result.append(num % 2)
#         num //= 2
    
#     result.extend([0] * (n-len(result))) # extend를 이용하여 리스트 마지막에 n의 개수만큼 0 추가
#     result.reverse()
#     return result

# def solution(n, arr1, arr2):
#     maps = []
#     for a, b in zip(arr1, arr2): # zip을 이용하여 묶음
#         maps.append(a|b) # or 비트연산으로 최종 지도를 구함
    
#     answer = []
#     for num in maps:
#         bina = binary(num, n) # 2진수 변환
#         tmp = ""
#         for b in bina:
#             if b == 1: tmp += "#" # 1이면 #, 0이면 공백
#             else: tmp += " "
        
#         answer.append(tmp)
#     return answer

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        map = str(bin(i|j)[2:]) # bin을 이용하여 2진수 변환 후 str을 통해 문자열로 변환
        map = map.rjust(n, "0") # 전체 자리 n을 확보한 후 map을 오른쪽 정렬 후 공백을 0으로 채움
        map = map.replace("1", "#") # 1을 #으로 교체
        map = map.replace("0", " ") # 0을 공백으로 교체
        answer.append(map)

    return answer
