# n이 1일 때 CY, n이 2일 때 SK, n이 3일 때 CY, n이 4일 때 SK, ...
# 즉, n이 짝수일 때 SK, 홀수일 때 CY 

n = int(input())
print("SK" if n % 2 == 0 else "CY")
