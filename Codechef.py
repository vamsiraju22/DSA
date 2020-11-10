#CODECHEF

#https://www.codechef.com/problems/FLOW006

t=int(input())
for p in range(1,t+1):
    n=int(input())
    
    l=(".".join(str(n))).split('.')
    sum=0
    for i in l:
        sum+=int(i)
    print(sum)
    
# https://www.codechef.com/submit/HS08TEST

w=int(input())
a=int(input())

if (w%5)!=0:
    print(a)
else:
    if a-w>0:
        print(a-w-0.5)
    else:
        print(a)