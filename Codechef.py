#CODECHEF

#1. https://www.codechef.com/problems/FLOW006

t=int(input())
for p in range(1,t+1):
    n=int(input())
    
    l=(".".join(str(n))).split('.')
    sum=0
    for i in l:
        sum+=int(i)
    print(sum)
    
#2. https://www.codechef.com/submit/HS08TEST

withdrawal_amount, balance_amount = input().split()              
withdrawal_amount = int(withdrawal_amount)                        
balance_amount = float(balance_amount)                            
if (withdrawal_amount % 5 == 0 and balance_amount>(withdrawal_amount+.5)):
    balance_amount = balance_amount - withdrawal_amount - 0.5     
    print('%.2f' % balance_amount)
else:
    print('%.2f' % balance_amount)


#3. https://www.codechef.com/problems/FLOW004
t=int(input())
for i in range(t):
    n=input()
    l=len(n)
    sum1=int(n[0])+int(n[l-1])
    print(sum1)
    
#4. https://www.codechef.com/submit/START01

n=input()
print(n)

#5. https://www.codechef.com/problems/INTEST
count=0
n, k = list(map(int,input().split()))
for i in range(n):
    val=int(input())
    if val%k==0:
        count+=1
    del val
print(count)

#6. https://www.codechef.com/problems/FLOW002

t=int(input())

for i in range(t):
    n, k = list(map(int,input().split()))
    print(n%k)a
    
#7. https://www.codechef.com/problems/FLOW007

def reverseArray(a):
    res=[]
    for i in range(len(a),0,-1):
        #print(a[i-1])
        res.append(a[i-1])
    return(res)

t = int(input())
for i in range(t):
    arr = int(input())
    if arr%10==0:
        rem=0
        while(rem==0):
            arr=arr//10
            rem=arr%10
    #print(arr)
    res = reverseArray(str(arr))
    print(''.join(map(str, res)))
    
#Doubt
# 8. https://www.codechef.com/problems/FLOW013
t=int(input())
for i in range(t):
    a,b,c=list(map(int,input().split()))
    if a==0 or b==0 or c==0:
        print("No")
        break
    elif a+b+c ==180:
        print("Yes")
    else:
        print("No")
    
#9. https://www.codechef.com/submit/FLOW017
#second largest
t = int(input())
for i in range(t):
    l = list(map(int,input().split()))
    
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    print(l[1])
    
#10. https://www.codechef.com/problems/FLOW018
t=int(input())
for i in range(t):
    n=int(input())
    a=[1]
    for i in range(1,n+1):
        a.append(a[i-1]*i)
    print(a[-1])   

#11 https://www.codechef.com/problems/FSQRT
#square root

import math
t=int(input())

for i in range(t):
    n=int(input())
    print(round(math.sqrt(n)))

#12 https://www.codechef.com/problems/FLOW001
t = int(input())
for i in range(t):
    # Read integers a and b.
    (a, b) = map(int, input().split(' '))
    
    ans = a + b
    print(ans)
    
#13. https://www.codechef.com/problems/LUCKFOUR
t=int(input())
for i in range(t):
    n=input()
    t=(" ".join(n)).split()
    print(t.count('4'))