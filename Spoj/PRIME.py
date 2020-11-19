# https://www.spoj.com/problems/PRIME1/

t=int(input())
for i in range(t):
    m,n=list(map(int,input().split()))
    for j in range(m-1,n+1):
        i=2
        count=0
        while(i**2<=j):
            if j<2:
                break
            if j==2:
                print(j)
                break
            else:
                if j%i==0:
                    if i!=j:
                        count+=1
            i+=1
        if count==0:
            if j!=1:
                #print('Yes')
                print(j)
