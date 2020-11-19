#Doubt
#  https://www.spoj.com/problems/LASTDIG/

t=int(input())
for tc in range(t):
    (num, d) = map(int, input().split(' '))
    dic ={1:1,2:4,3:4,4:2,5:1,6:1,7:4,8:4,9:2}
    last_digit = num%10
    if d>num:
        power=d%dic[last_digit]
        if power==0:
            power=1
    else:
        power=dic[last_digit]
    #print(power)
    val=(last_digit**power)%10
    print(val)