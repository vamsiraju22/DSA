# https://www.spoj.com/problems/INVCNT/

t=int(input())
for tc in range(t):
    l=[]
    n=int(input())
    for i in range(n+1):
        a=input()
        if a!=' ':
            l.append(int(a))
    count=0
    for ind,i in enumerate(l):
        for j_ind,j in enumerate(l):
            #print(i,j)
            if ind<j_ind and l[ind]>l[j_ind]:
                #print(ind,i," - ",j_ind,j)
                count+=1
    print(count)