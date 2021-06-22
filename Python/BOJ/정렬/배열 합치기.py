# 입력 받은 2개의 배열을 합쳐 오름차순 정렬

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# numbers = []
# for num in a:
#   numbers.append(num)

# for num in b:
#   numbers.append(num)

# for num in sorted(numbers):
#   print(num, end=" ")

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

numbers = a + b # + 연산으로 배열을 합칠 수 있음
numbers = " ".join(map(str, sorted(numbers))) # join을 사용하여 공백으로 배열을 str로 변환
print(numbers)
