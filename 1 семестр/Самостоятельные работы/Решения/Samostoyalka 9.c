/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i;

void func_random (int k, int a[]);
void func_scan (int k, int a[]); 
void func_print (int k, int a[]);
int func_sum (int k, int a[]);
float func_average (int p, int q, int a[]);
void func_chisla (int a1[], int a2[], int a3[]);
void func_zero (int k, int a[]);
void underfunction_chisla (int p[], int k[], int a[], int x);

int main()
{
    int m1[5], m2[6], m3[8], a, b;
    
    func_scan (5, m1);
    func_scan (6, m2);
    func_scan (8, m3);
    scanf ("%d %d", &a, &b);
    printf ("%d %d %d\n", func_sum (5, m1), func_sum (6, m2), func_sum (8, m3));
    printf ("%.1f\n", func_average (a, b, m3));
    func_chisla (m1, m2, m3);
    printf ("\n");
    return 0;
}

void func_random (int k, int a[]){
    for (i=0; i<k; i++)
        a[i]=rand()%6+10; 
}

void func_scan (int k, int a[]){
    for (i=0; i<k;i++)
        scanf ("%d", &a[i]);
}

void func_print (int k, int a[]){
    for (i=0; i<k; i++)
        printf ("%2d ", a[i]);
    printf ("\n");
}

int func_sum (int k, int a[]){
    int res=0;
    for (i=0; i<k;i++)
        res+=a[i];
    return res;
}

float func_average (int p, int q, int a[]){
    int sum=0;
    float res;
    for (i=0; i<(q-p+1); i++)
        sum+=a[p-1+i];
    return (float) sum/(q-p+1);
}

void func_zero (int k, int a[]){
    for (i=0; i<k; i++)
        a[i]=0;
}

void func_chisla (int a1[], int a2[], int a3[]){
    int p[6], k1[6], k2[6], k3[6];
    for (i=0; i<6; i++)
        p[i]=10+i;
    func_zero (6, k1);
    func_zero (6, k2);
    func_zero (6, k3);
    underfunction_chisla (p, k1, a1, 5);
    underfunction_chisla (p, k2, a2, 6);
    underfunction_chisla (p, k3, a3, 8);
    for (i=0; i<6; i++){
        if ((k1[i]!=0)&&(k2[i]!=0)&&(k3[i]!=0))
            printf ("%d ", p[i]);
    }
    printf ("\n");
}

void underfunction_chisla (int p[], int k[], int a[], int x){
    int j;
    for (i=0; i<x; i++){
        for (j=0; j<6; j++){
            if (a[i]==p[j])
                k[j]+=1;
        }    
    } 
}