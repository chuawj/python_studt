#아스키코드
a=input()
print(ord(a))
#단어 길이 재기
print(len(input()))
#대소문자 바꾸기
print(input().swapcase())
#학점계산
dic = {'A+':'4.3', 'A0':'4.0', 'A-':'3.7',
       'B+':'3.3', 'B0':'3.0', 'B-':'2.7',
       'C+':'2.3', 'C0':'2.0', 'C-':'1.7',
       'D+':'1.3', 'D0':'1.0', 'D-':'0.7',
       'F':'0.0'}
grade = input()
print(dic[grade])
#문자와 문자열
s = input()
i = int(input())
print(s[i-1])
#그대로 출력하기
while True :
    try :
        print(input())
    except EOFError:
        break
#문자열
T = int(input())
 
for i in range(T):
    test = input()
    print(test[0] + test[-1])