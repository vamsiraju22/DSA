# https://www.spoj.com/problems/FCTRL/
"""
t=int(input())
for tc in range(t):
    n=int(input())
    a=[1]
    for i in range(1,n+1):
        a.append(a[i-1]*i)
    #print(a[-1])
    arr=a[-1]
    count=0
    if arr%10==0:
        rem=0
        while(rem==0):
            count+=1
            arr=arr//10
            rem=arr%10
    print(count)"""
    
t=int(input())
for tc in range(t):
    count=0
    n=int(input())
    i=5
    rem=n//i
    while(rem!=0):
        rem=n//i
        count+=rem
        i=i*5
    print(count)