# 상근이가 구할 수 있는 두 수의 가능합 중, 최소값과 최대값을 구하면됨
# 최소값을 구하기 위해서는 a, b 모두 6을 5로 변환 후 더하면 됨
# 최대값을 구하기 위해서는 a, b 모두 5를 6으로 변환 후 더하면 됨

a, b = input().split()

min = int(a.replace("6", "5")) + int(b.replace("6", "5")) # 최소값
max = int(a.replace("5", "6")) + int(b.replace("5", "6")) # 최대값

print(min, max)
