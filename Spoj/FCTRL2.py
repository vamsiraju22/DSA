# https://www.spoj.com/problems/FCTRL2/

t=int(input())
for i in range(t):
    n=int(input())
    #a=[1]
    var=1
    for i in range(1,n+1):
        #a.append(a[i-1]*i)
        var=var*i
    print(var)  