/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <limits.h>

unsigned long int f=0, *p_f=&f;
unsigned long int func (unsigned long int n, unsigned long int m);

int main()
{
    unsigned long int res, a, b;
    scanf ("%ld %ld", &a, &b);
    res = func (a, b);
    if (f==0)
        printf ("%ld\n", res);
    else if (f==1)
        printf ("endless");
    else if (f==2)
        printf ("overflow");
    return 0;
}

unsigned long int func (unsigned long int n, unsigned long int m){
    unsigned long int p, q, i=0, j=0;
    if (n<=ULONG_MAX-m){
        if ((i!=ULONG_MAX)&&(j!=ULONG_MAX)){
            if ((n+m)%2==1){
                if (n>=m)
                    return n;
                else 
                    return m;
            }
            else {
		    i+=1;
                p=func((n+m)/2, m);
		    j+=1;
                q=func(n, (n+m)/2);
                return p+q;
            }
        }
        else 
            *p_f=1;
    }
    else 
        *p_f=2;
}

