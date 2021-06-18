# 유클리드 호제법을 이용하여 최대공약수 계산
# pop 연산을 통해 N개의 최소공배수 계산
# 예를 들어, [2, 6, 8, 14]의 최소공배수는 두개씩 최소공배수를 구하면 됨
# 2, 6의 최소공배수: 6 => [8, 14, 6]
# 8, 14의 최소공배수: 56 => [6, 56]
# 6, 56의 최소공배수: 168 => [168] 따라서 168이 [2, 6, 8, 14]의 최소공배수가 됨

# def gcd(a, b):
#     if a < b: # 유클리드 호제법에서 a가 더 커야하므로 b가 더 클 경우 a, b 스와프
#         a, b = b, a
    
#     while b:
#         a, b = b, a%b # 유클리드 호제법
    
#     return a

# def solution(arr):
#     while len(arr) != 1:
#         # 리스트에서 처음 2개의 값 pop 후 최소 공배수 구한 후 다시 append 반복
#         a = arr.pop()
#         b = arr.pop()
#         arr.append(a * b // gcd(a, b))
        
#     return arr[0]

# 정렬이 되어 있을 경우만
def gcd(a, b): # 유클리드 호제법
    while b: # b가 0이상일 경우만
        a, b = b, a % b # a에 b를 넣고, b에 a%b 값을 넣어 반복

    return a

def solution(arr):
    for i in range(len(arr) - 1):
        arr[i+1] = (arr[i] * arr[i+1]) // gcd(arr[i], arr[i+1]) # 리스트에서 i+1에 최소공배수를 계속해서 구해나감

    return arr[-1] # 리스트의 마지막 요소가 N개의 최소공배수가 됨
