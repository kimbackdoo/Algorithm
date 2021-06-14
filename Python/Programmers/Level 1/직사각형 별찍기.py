n, m = map(int, input().split())

# print("\n".join(["*" * n for _ in range(m)]))

print(("*" * n + "\n") * m) # "*"을 n번 곱하고 마지막에 줄바꿈 문자 삽입 후 m번 반복
