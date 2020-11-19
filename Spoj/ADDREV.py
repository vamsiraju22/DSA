#SPOJ

#https://www.spoj.com/problems/ADDREV/

def rev(n1):
    l=(".".join(str(n1))).split('.')
    l=l[::-1]
    rev_n=""
    for i in l:
        rev_n+=(i)
    return(int(rev_n))
t=int(input())
for p in range(1,t+1):
    n=input()
    n1,n2=n.split()

    sum=rev(n1)+rev(n2)
    print(rev(sum))
    