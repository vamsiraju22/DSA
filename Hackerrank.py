#https://www.hackerrank.com/challenges/grading/problem

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

#https://www.hackerrank.com/challenges/diagonal-difference/problem

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

#https://www.hackerrank.com/contests/smart-interviews/challenges/si-print-right-angled-triangle-pattern/problem

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


