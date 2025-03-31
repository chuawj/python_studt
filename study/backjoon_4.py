
#N 찍기기
n=int(input(" "))

for i in range(n):
    print(i+1)
#펙토리얼
n = int(input())
result = 1

for i in range(1, n+1):
    result *= i
    
print(result)

#A+B-3
T=int(input(""))

for i in range(T):
    a,b=map(int,input("").split( ))

    print(a+b)
#A+B-5
while True:
    a,b=map(int,input().split())
    if(a==0 and b==0):
        break
    else:
        print(a+b)
#99단
n=int(input(""))
if(1<=n<=9):
    for i in range(1,10):
        print(n,"*",i,"=",n*i)
#별찍기-1      
n=int(input())
for i in range(1,n+1):
    print("*"*i)
#a+b-4
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break