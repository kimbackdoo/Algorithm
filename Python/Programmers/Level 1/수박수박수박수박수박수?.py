# def solution(n):
#     answer = "수박"
#     if n % 2 == 0: # n이 짝수이면 n//2만큼을 곱합
#         answer *= n//2
#     else: # 홀수면 (n-1)//2만큼을 곱하고 answer의 첫번째 요소를 더함
#         answer = answer * ((n-1)//2) + answer[0]
        
#     return answer
  
# def solution(n):
#     pattern = ["수", "박"]
#     answer = ''
#     for i in range(n):
#         answer += pattern[i % 2]

#     return answer

def solution(n):
    return ("수박"*n)[:n] # 수박 문자열에 n을 곱하고 n만큼 split
