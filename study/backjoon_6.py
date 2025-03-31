
#x보다 작은수수
n,x=map(int,input().split())
num= list(map(int,input().split()))
for i in range(n):
    if(num[i]<x):
        print(num[i],end=" ")
#개수 세기기
n=int(input())
n_list=list(map(int,input().split()))
v=int(input())
print(n_list.count(v))

#과제 안내신분..?
student=[i for i in range(1,31)]
for i in range(28):
    data=int(input())
    student.remove(data)
print(min(student))
print(max(student))

#행렬 덧셈

A, B = [], []

N, M = map(int, input().split())

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()
