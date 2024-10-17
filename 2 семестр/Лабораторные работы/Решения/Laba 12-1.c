/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i;

void func_compare (int a[], int n, int k, int *quant_of_compare, int *quant_of_change);
void func_change(int a[], int n_1, int n_2, int *quant_of_change);
void func_random (int a[], int k);
void func_print (int a[], int k);
void func_scan (int a[], int k);

int main()
{
    int n, f, k, quant_of_compare=0, quant_of_change=0;
    scanf ("%d", &n);
    int m[n];
    //func_random(m, n);
    func_scan(m, n);
    func_print(m, n);
    while (k!=n){
        func_compare (m, n, k, &quant_of_compare, &quant_of_change);
        k+=1;
    }
    printf ("%d %d\n", quant_of_change, quant_of_compare);
    return 0;
}

void func_compare (int a[], int n, int k, int *quant_of_compare, int *quant_of_change){
    for (i=0; i<k; i++){
        *quant_of_compare+=1;
        if (a[k]>=a[i]){
            func_change (a, i, k, quant_of_change);
            func_print(a, n);
        }
    }
}

void func_change(int a[], int n_1, int n_2, int *quant_of_change){
    *quant_of_change+=2;
    int j;    
    j=a[n_2];
    for (i=0; i<n_2-n_1; i++){
        a[n_2-i]=a[n_2-1-i];
        *quant_of_change+=1;
    }
    a[n_1]=j;
}

void func_random (int a[], int k){
    for (i=0; i<k; i++)
        a[i]=rand()%20+1;
}

void func_print (int a[], int k){
    for (i=0; i<k; i++)
        printf ("%3d", i+1);
    printf ("\n");
    for (i=0; i<k; i++)
        printf ("%3d", a[i]);
    printf ("\n\n");
}

void func_scan (int a[], int k){
    for (i=0; i<k; i++)
        scanf("%d", &a[i]);
}
