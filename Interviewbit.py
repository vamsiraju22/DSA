#Interviewbit

#C++
#1. https://www.interviewbit.com/problems/number-of-1-bits/

int Solution::numSetBits(unsigned int A) {
    int c=0;
    while(A>0){
        if (A&1==1){
            c++;
        }
        A=A>>1;
    }
    return(c);
}
