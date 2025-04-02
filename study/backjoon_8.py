#이상한 기호
a, b = map(int, input().split())

print((a+b) * (a-b))
#검증수
num = map(int, input().split())

result = 0

for i in num:
   result += i ** 2

print(result%10)
