#bits
#funcion to count total no of bits
def totalbits(num):
        count=0
        n=num
        setbits=0
        unsetbits=0
        while n>0:
            if n&1 == 1:
                setbits+= n&1
            else:
                unsetbits+=1
            n=n>>1
        return(setbits+unsetbits)

#Binary to Decimal Conversion
def binary1(num):
    l=[]
    rem=0
    if num==0:
        return(0)
    if num==1:
        return(1)
    while num>1:
        rem=num%2
        l.append(rem)
        num=num//2
        if num==1:
            l.append(1)
    return(''.join(map(str,l[::-1])))

def binary2(num):
    return(bin(num).replace('0b',''))


# Count set bits 
def count_setbits(num):
        count=0
        while n>0:
            count+= n&1
            n=n>>1
        #print(count)
        return(count)

#check if a bit at ith position is set or not (checkbit)
def checkbit(n, i): 
    if n & (1 << (i - 1)): 
        return(True) 
    else: 
        return(False)
  
# to convert decimal to binary in python
int('10101',2)

