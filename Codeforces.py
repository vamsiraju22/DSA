#CODEFORCES

#http://codeforces.com/problemset/problem/71/A

t=int(input())
for p in range(1,t+1):
    s=str(input())
    
    if len(s)>10:
        new_s=""
        new_s+=str(s[0])
        new_s+=str(len(s)-2)
        new_s+=str(s[len(s)-1])
        print(new_s)
    else:
        print(s)