
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

