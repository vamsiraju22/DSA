#CODEFORCES

#1.http://codeforces.com/problemset/problem/71/A

t=int(input())
for p in range(1,t+1):
    s=str(input())
    
    if len(s)>10:
        new_s=""
        new_s+=str(s[0])
        new_s+=str(len(s)-2)
        new_s+=str(s[len(s)-1])
        print(new_s)
    else:
        print(s)
        
#2.  https://codeforces.com/problemset/problem/4/A

a=int(input())
if a%2==0:
    if a==2:
        print("No")
    else:
        print("Yes")
else:
    print("No")

#3. https://codeforces.com/problemset/problem/231/A

n=int(input())
a=[]
a_yes=0
c_yes=0
c_no=0
for i in range(n):
    a.append(list(map(int,input().split(' '))))
for i in a:
    for j in i:
        if j==1:
            c_yes+=1
        else:
            c_no+=1
    
    if c_yes>=2:
        a_yes+=1
    c_yes=0
    c_no=0
print(a_yes)

#4. https://codeforces.com/problemset/problem/158/A 

n,val=list(map(int,input().split(' ')))
c=0
a=list(map(int,input().split(' ')))
if sum(a)>0:
    for i in a:
        if i>=a[val-1] and i!=0:
            c+=1
    print(c)
else:
    print(0)

#5. https://codeforces.com/problemset/problem/50/A

m,n=list(map(int,input().split(' ')))

print(m*n//2)

#6. https://codeforces.com/problemset/problem/282/A

n=int(input())
x=0
for i in range(n):
    a= input()
    if a in ['X++','++X']:
        x+=1
    if a in ['--X','X--']:
        x-=1
print(x)

#7. https://codeforces.com/problemset/problem/112/A

a=input().lower()
b=input().lower()
if a>b:
    print(1)
elif a<b:
    print(-1)
else:
    print(0)
    
#8. https://codeforces.com/problemset/problem/281/A
a=input()
if a[0].islower():
    print(a[0].upper()+a[1:])
else:
    print(a)

#9. https://codeforces.com/problemset/problem/263/A
a=[]
for i in range(5):
    a.append(list(map(int,input().split(' '))))
r=0
c=0
rs=0
cs=0
for i in range(len(a)):
    for j in range(5):
        if a[i][j]==1:
            r,c=i,j
            break
r=r+1
c=c+1

if r>=3:
    rs=r-3
else:
    rs=3-r
if c>=3:
    cs=c-3
else:
    cs=3-c
print(rs+cs)

#10. https://codeforces.com/problemset/problem/339/A

a= list(map(int,input().split('+')))
a.sort()
res=""
for i in a:
    res+=str(i)+"+"
print(res[:-1])