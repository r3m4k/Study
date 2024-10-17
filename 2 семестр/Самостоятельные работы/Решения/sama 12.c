/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i;

void func_random (int a[], int k);
void func_print (int a[], int k);
void func_compare_upgraded (int a[], int k);
void func_compare(int a[], int k, int first, int last);
void func_change(int a[], int n_1, int n_2);


int main()
{
    int n;
    scanf ("%d", &n);
    int m[n], k=1;    //к-количество элементов порядка
    func_random (m, n);
    //func_print (m, n);
    printf ("Flag");
    while(k!=n){
        printf ("Flag");
        func_compare_upgraded (m, k);
        k+=1;
    }
    func_print (m, n);
    return 0;
}

void func_compare_upgraded (int a[], int k){
        printf ("Flag");
        if (a[k]==a[k/2])
            func_change (a, k/2, k);
         
        else if (a[k]>a[k/2])
            func_compare (a, k, k/2, k);
            
        else if (a[k]<a[k/2])
            func_compare (a, k, 1, k/2);
}

void func_compare(int a[], int k, int first, int last){
    for (i=first; i<last; i++){
        //*quant_of_compare+=1;
        if (a[k]>=a[i-1]){
            func_change (a, k, i-1);
        }
    }
}

void func_change(int a[], int n_1, int n_2){
    int j;    
    j=a[n_1];
    for (i=0; i<n_2-n_1; i++){
        a[n_1+i]=a[n_1+1+i];
        //*quant_of_change+=1;
    }
    a[n_2]=j;
    //*quant_of_change+=1;
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
    printf ("\n");
}