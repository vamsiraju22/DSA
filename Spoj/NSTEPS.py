# https://www.spoj.com/problems/NSTEPS/
#Series
t=int(input())
for j in range(t):
    x,y=list(map(int,input().split()))

    if x>=y:
        if x-y==2 or x==y:
            if x%2!=0:
                print(x+y-1)
            if x%2==0:
                print((x+y))
        else:
            print("No Number")
    else:
        print("No Number")