/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int func_create (int n, int m, int i, int a[]);
int func_change (int k, int num, int a[]);
void func_print (int i);

int main()
{
    int a1, b1, a2, b2, i, k,
        m1[8], m2[12];
    scanf ("%d %d", &a1, &b1);
    scanf ("%d %d", &a2, &b2);
    scanf ("%d", &k);
    
    func_print (8);
    for(i=0; i<8; i++){
        m1[i]=func_create(a1, b1, i, m1);
        printf ("%5d",m1[i]);
    }
    func_print (12);
    for(i=0; i<12; i++){
        m2[i]=func_create(a2, b2, i, m2);
        printf ("%5d", m2[i]);
    }
    
    func_print (8);
    func_change(k, 8, m1);
    for (i=0; i<8; i++){
        
        printf ("%5d", m1[i]);
    }
    func_print (12);
    func_change(k, 12, m2);
    for (i=0; i<12; i++){
        
        printf ("%5d", m2[i]);
    }
    return 0;
}

int func_create (int n, int m, int i, int a[]){
    a[i+1]=n*(i+m);
}

int func_change (int k, int num, int a[]){
    int i, m[2*k];
    for (i=0; i<k; i++)
        m[i]=a[i];
    for (i=0; i<k; i++)
        m[k+i]=a[num-1-i];
    for (i=0; i<k; i++){
        a[i]=m[k+i];
        a[num-1-i]=m[i];
    }
}

void func_print (int i){
    int j;
    printf ("\n");
    printf ("\n");
    for (j=1; j<=i; j++)
        printf ("%5d", j);
    printf ("\n");
}


