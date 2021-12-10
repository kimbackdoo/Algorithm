# a, b 리스트의 곱의 합이 최소가 되려면 a를 오름차순 정렬, b를 내림차순 정렬하여 곱의 합을 구하면 됨
# 문제에서 b 리스트를 바꾸면 안된다고 했지만 b의 큰 수부터 차례대로 a의 작은 수를 곱해나가면 되므로 정렬해서 답을 구하면됨, 그리디 알고리즘 적용

# import sys
# input = sys.stdin.readline

# n = int(input())
# a = sorted(map(int, input().split())) # a 오름차순 정렬
# b = sorted(map(int, input().split()), reverse=True) # b 내림차순 정렬

# print(sum([x * y for x, y in zip(a, b)])) # zip 함수를 이용하여 a, b 리스트를 묶고 곱을 구한 후 sum 함수를 이용하여 전체 합을 구함

import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)

print(sum(map(lambda x, y: x * y, a, b))) # map 함수와 lambda식을 이용하여 a, b 모든 요소의 곱을 구하고 sum 함수를 이용하여 전체 합을 구함
