# 정렬 후 k번째 수 출력

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

print(sorted(numbers)[k-1])
