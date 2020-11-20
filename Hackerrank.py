
#1. https://www.hackerrank.com/challenges/grading/problem

grades=[13,45,67,43]
new_grade=[]
for ind,grade in enumerate(grades):    
    if grade >= 38:
        if (5-(grade%5))<3:
            #new_grade[ind]=grade+(5-grade%5)
            #print(new_grade)
            new_grade.append(grade+(5-grade%5))
        else:
            new_grade.append(grade)
    else:
        new_grade.append(grade)
return(new_grade)
#Hackerrank

#2. https://www.hackerrank.com/challenges/diagonal-difference/problem

arr= [[11,2,4],[4,5,6],[10,8,-12]]
sum1=0
sum2=0
for ind,i in enumerate(arr):
    for j_ind,j in enumerate(i):
        if j_ind==ind:
            sum1+=j
    for j_ind,j in enumerate(i[::-1]):
        if j_ind==ind:
            sum2+=j   
if sum1>sum2:
    return(sum1-sum2)
else:
    return(sum2-sum1)

#3. https://www.hackerrank.com/contests/smart-interviews/challenges/si-print-right-angled-triangle-pattern/problem

t=int(input())
for p in range(1,t+1):
    n=int(input())
    print("Case #",end='')
    print(p,end='')
    print(":")
    
    for i in range(1,n+1):
        for j in range(n,0,-1):
            if j>i:
                print(" ",end='')
            else:
                print('*',end='')
        print()

#4. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-sum-of-two-matrices/submissions/code/1328018402

n,m=input().split()
n=int(n)
m=int(m)
arr1=[input().split() for i in range(n)]
arr2=[input().split() for i in range(n)]
sum_arr=[]
for i in range(n):
    chota_sum=[]
    for j in range(m):
        chota_sum.append(0)
    sum_arr.append(chota_sum)
    del (chota_sum)

for ind,i in enumerate(arr1):
    for j_ind,j in enumerate(arr2):
        if ind==j_ind:
            for element_ind,element in enumerate(i):
                sum_arr[ind][element_ind]=int(element)+int(j[element_ind])

for i in sum_arr:
    for j in i:
        print(j,end=' ')
    print()

#5. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-matrix-row-sum

n,m=input().split()
n=int(n)
m=int(m)
arr1=[input().split() for i in range(n)]
sum_arr=[0]*n
num_rows=len(arr1)
num_cols=len(arr1[0])


for i in range(0,num_rows):
    for j in range(0,num_cols):
        sum_arr[i]+=int(arr1[i][j])
for i in sum_arr:
    print(i)

#6. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-transpose-matrix

n,m=input().split()
n=int(n)
m=int(m)
arr1=[input().split() for i in range(n)]
new_arr=[]

num_rows=len(arr1)
num_cols=len(arr1[0])
for i in range(0,num_cols):
    new_small_arr=[]
    for j in range(0,num_rows):
        new_small_arr.append(arr1[j][i])
    new_arr.append(new_small_arr)
    del new_small_arr

for  i in new_arr:
    for j in i:
        print(j,end=' ')
    print()



#7. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-matrix-column-sum

n,m=input().split()
n=int(n)
m=int(m)
arr1=[input().split() for i in range(n)]
sum_arr=[0]*m
num_rows=len(arr1)
num_cols=len(arr1[0])
for i in range(0,num_cols):
    for j in range(0,num_rows):
        
        sum_arr[i]+=int(arr1[j][i])
for i in sum_arr:
    print(i)
    
#8. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-a-sparse-matrix

n,m=input().split()
n=int(n)
m=int(m)
arr1=[input().split() for i in range(n)]
num_rows=len(arr1)
num_cols=len(arr1[0])
count=0
for i in range(0,num_rows):
    for j in range(0,num_cols):
        if int(arr1[i][j])==0:
            count+=1
if count>(n*m)/2:
    print("Yes")
else:
    print("No")

#9. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-digits-sum

a=int(input())
sum=0
while a>0:
    r=a%10
    sum=sum+r
    a=a//10
print(sum)

#10. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-number-of-multiples/submissions/code/1328044850

n=int(input())
print(n//3+n//5-n//15)

#11. https://www.hackerrank.com/challenges/arrays-ds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    res=[]
    for i in range(len(a),0,-1):
        #print(a[i-1])
        res.append(a[i-1])
    return(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

#12. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-triangle-validator/problem

n=list(map(int,input().split(' ')))
case_results=[]
master=[]
count=0
new=[]
for i in range(len(n)):
    
    a=n.copy()
    first=a.pop(i)
    second,third=a
    new= [j for j in [first,second,third]]
    master.append(new)
    a.reverse()
    second,third=a
    new= [j for j in [first,second,third]]
    master.append(new)
    del new
for i in master:
    a,b,c=i
    if a+b>c:
        count+=1
    else:
        print("No")
        break
if count==6:
    print("Yes")

#13. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-long-factorial

n=int(input())
a=[1]
for i in range(1,n+1):
    a.append(a[i-1]*i)
print(a[-1])

#14. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-natural-numbers-sum/problem

n=int(input())
print(round(n*(n+1)/2))

#15. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-cubes-sum/problem

n=int(input())
print(int((n*(n+1))*(n*(n+1))/4))

#16. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-squares-sum/problem

n=int(input())
print(int(n*(n+1)*((2*n)+1)/6))

#17. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-prime-or-not/problem

n=int(input())
i=2
count=0
while(i**2<=n):
    if n<2:
        break
    if n==2:
        break
    else:
        if n%i==0:
            if i!=n:
                count+=1
    i+=1
if count==0:
    if n!=1:
        print('Yes')
    else:
        print("No")
else:
    print("No")
#18. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-narcissistic-numbers/problem

n=input()
sum1=0
dig=len(".".join(n).split('.'))
a=int(n)
while n!=0:
    #print(n%10)
    rem=int(n)%10
    sum1+=rem**dig
    n=int(n)//10
if sum1==a:
    print("Yes")
else:
    print("No")
    
#19. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-harshad-number

n=input()
sum1=0
new=list(map(int,list(".".join(n).split('.'))))
for i in new:
    sum1+=i
if int(n)%sum1==0:
    print("Yes")
else:
    print("No")

#20. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-number-reverse

def rev(num):
    n=num
    while n!=0:
        rem=n%10
        l.append(rem)
        n=n//10
    return(list(map(int,l)))

num=int(input())
l=[]
sum1=0

if num<0:
    new=rev(num*-1)
    for ind,i in enumerate(new):
        dig=10**(len(new)-1-ind)
        sum1=sum1+dig*i
    print(sum1*-1)
if num>=0:
    new=rev(num)
    for ind,i in enumerate(new):
        dig=10**(len(new)-1-ind)
        sum1=sum1+dig*i
    print(sum1)

#21. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-right-angled-triangle-pattern-1

n=int(input())
count=1
for i in range(1,n+1):
    for j in range(i):
        print(count,end=' ')
        count+=1
    print()

#22. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-letters-of-the-alphabet

s=input()
if len(set(s.lower()))==26:
    print("Yes")
else:
    print("No")

#23. # https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-right-angled-triangle-pattern-2

n=int(input())

for i in range(1,n+1):
    value=i
    for j in range(1,i+1):
        print(value,end=' ')
        value+=n-j
    print()

#24. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-digits-in-a-string

s=input()
count=0
for i in s:
    if 47<ord(str(i))<58:
        count+=1
if count==len(s):
    print("Yes")
else:
    print("No")
    
#25. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-vowels-in-a-string

s=input()
s=s.lower()
vow=['a','e','i','o','u']
count=0
for i in s:
    if i in vow:
        count+=1
if count==len(s):
    print("Yes")
else:
    print("No")

#26. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-print-pyramid-pattern

n=int(input())
l=[]
for i in range(1,n+1):
    l.append("*"*(i*2-1))
l=l[::-1]
p1=((2*n)+1)//2
for i in range(1,n+1):
    for j in range(1,n+1):
            if j==p1:
                print(l[p1-1],end='')
                p1-=1
            else:
                print(' ',end='')
    print()
          
#27. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-print-multiplication-table

n=int(input())

for i in range(1,11):
    print("{} * {} = {}".format(n,i,n*i))            

#28. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-print-half-diamond-pattern

maximum=int(input()) #n=int(input())
n=(2*maximum)-1 #maximum=int((n+1)/2)
l=[]
p1=maximum-1
for i in range(1,n+1):
    if i<=maximum:
        l.append("*"*i)
    else:
        l.append("*"*p1)
        p1-=1
for i in range(0,n):
    print(l[i])
   
#29. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-reverse-string/problem

s=input()
print(s[::-1])

#30. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-occurrence-of-a-character-1

s=input()
count=0
c=input()
for i in s:
    if i==c:
        count+=1
print(count)

#31. https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-count-vowels-and-consonants

s=input().lower()
count_v=0
count_c=0
vowels=['a','e','i','o','u']
total=[]
for i in range(97,123):
    total.append(chr(i))
consonants=set(total)-set(vowels)
s.lower()
for i in s:
    if i in vowels:
        count_v+=1
    if i in consonants:
        count_c+=1
print(count_v,end=' ')
print(count_c)