/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <math.h> 

long int func (long int k){
    long int res = 0;
    int i=0, j=0;
    if(k==1)
        //j=1;
        return 1;
    else if (k==2)
        //j=1;
        return 2;
    else{ 
        /*
        {
            
            if (j==0){
                i+=1;
                printf ("%d-й уровень рекурсии при спуске", i);
            }
            else{
                j-=1;
                printf ("%d-й уровень рекурсии при подъёме", i-j);
            }
        }
    */
        res = 2*func(k-1)+func(k-2);
        return res;
    
    }
}
int main()
{
    long int k, r;
    scanf("%ld", &k);
    r = func(k);
    printf("%ld\n", r);
        return 0;
}
