#두수비교하기기
a,b=map(int,input().split())

if(a>b):
    print(">")
elif(a==b):
    print("==")
else:
    print("<")
#시험 성적적
a=int(input())
if(90<=a<=100):
    print("A")
elif(80<=a<90):
    print("B")
elif(70<=a<80):
    print("C")
elif(60<=a<70):
    print("D")
else:
    print("F")
#사분면 고르기
x=int(input())
y=int(input())
if(1000>=x>0 and 1000>=y>0):
    print("1")
elif(-1000<=x<0 and 1000>=y>0):
    print("2")
elif(-1000<=x<0 and -1000<=y<0):
    print("3")
elif(1000>=x>0 and -1000<=y<0):
    print("4")  
#윤년
a=int(input())

if(1<=a<4000):
    if(a%4==0 and a%100!=0 or a%400==0):
        print("1")
    else:
        print("0")
#사파리 월드
N, M = map(int, input().split())
print(abs(N-M))