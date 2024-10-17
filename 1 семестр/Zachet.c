/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int i;

void func_one (int k, int a[]);

int main()
{
    int a[20], p[20], j, k;
    for (i=0; i<20; i++){
        scanf ("%d", &a[i]);
    }
    func_one(20, p);
    
    for (i=0; i<20; i++){
        k=20-i;
        for (j=1; j<k; j++){
            if (a[i]==a[i+j])
                p[i]+=1;
        }
        k=0;
    }

    for (i=19; i>-1; i--){
        for (j=i-1; j>-1; j--)
            if (a[i]==a[j])
                p[i]=0;
    }
    
    for (i=0; i<20; i++){
        if (p[i]>1)
            printf ("%4d", a[i]);
    }
    printf ("\n");
    return 0;
}

void func_one (int k, int a[]){
    for (i=0; i<k; i++)
        a[i]=1;
}