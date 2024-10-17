/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby,
C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int i, j;

void func_random (int a[], int n);
void func_print (int a[], int k);

int main()
{
    int n1;
    scanf ("%d", &n1);
    int m1[n1];
    func_random (m1, n1);
    func_print (m1, n1);
    printf ("\n");
    int n2;
    scanf ("%d", &n2);
    int m2[n2];
    func_random (m2, n2);
    func_print (m2, n2);
    
    int *arp[n1+n2];
    for (i=0; i<n1; i++){
        arp[i]=&m1[i];
    }
    for (i=0; i<n2; i++){
        arp[n1+i]=&m2[i];
    }
    printf ("\n");
    
    int t;
    for (i=0; i<n1+n2; i++){
        for (j=0; j<n1+n2-i-1; j++){
            if (*arp[j]>*arp[j+1]){
                t=*arp[j];
                *arp[j]=*arp[j+1];
                *arp[j+1]=t;
            }
        }
    }
    
    for (i=0; i<n1+n2; i++)
        printf ("%3d", i+1);
    printf ("\n");
    for (i=0; i<n1+n2; i++)
        printf ("%3d", *arp[i]);
    printf ("\n\n");
    
    return 0;
}

void func_random (int a[], int n){
    for (i=0; i<n; i++)
        a[i]=rand()%19+1;
}

void func_print (int a[], int k){
    for (i=0; i<k; i++)
        printf ("%3d", i+1);
    printf ("\n");
    for (i=0; i<k; i++)
        printf ("%3d", a[i]);
    printf ("\n");
}