/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i;

void func_QuickSort (int a[], int n, int first, int last);
void func_swap (int *a, int *b);
void func_random (int a[], int k);
void func_print (int a[], int k);
void func_scan (int a[], int k);

int main()
{
    int n_1, n_2, j=0, k=1;
    scanf ("%d", &n_1);
    int m_1[n_1];
    func_scan (m_1, n_1);
    //func_random (m_1, n_1);
    //func_print (m_1, n_1);
    //func_QuickSort (m_1, n_1, 0, n_1-1);
    //func_print (m_1, n_1);
    
    scanf ("%d", &n_2);
    int m_2[n_2];
    func_scan (m_2, n_2);
    //func_random (m_2, n_2);
    
    func_print (m_1, n_1);
    func_print (m_2, n_2);
    
    int arp[n_1+n_2];
    
    for (i=0; i<n_1; i++)
        arp[i]=m_1[i];
    for (i=0; i<n_2; i++)
        arp[n_1+i]=m_2[i];
    
    //func_print (arp, n_1+n_2);
    func_QuickSort(arp, n_1+n_2, 0, (n_1+n_2)-1);
    
    func_print (arp, n_1+n_2);
}


void func_QuickSort (int a[], int n, int first, int last)
{
    int pivot; 
    int l,r; 
    l=first; r=last;
    pivot=a[(l+r)/2]; 
    while (l<=r) {
        while (a[l]>pivot) l++;
        while (a[r]<pivot) r--;
        if (l<=r) {
            func_swap(&a[r],&a[l]); 
            l++;
            r--;
        }
    } 
    if (first<r) func_QuickSort(a, n, first, r);
    if (l<last) func_QuickSort(a, n, l, last); 
}

void func_QuickSort_pointers (int **a, int n, int first, int last)
{
    int pivot; 
    int l,r; 
    l=first; r=last;
    pivot=(*a)[(l+r)/2]; 
    while (l<=r) {
        while ((*a)[l]>pivot) l++;
        while ((*a)[r]<pivot) r--;
        if (l<=r) {
            func_swap(a[r],a[l]);
            l++;
            r--;
        }
    } 
    if (first<r) func_QuickSort_pointers (a, n, first, r); 
    if (l<last) func_QuickSort_pointers (a, n, l, last);
}

void func_swap (int *a, int *b){
    int c;
    c=*a;
    *a=*b;
    *b=c;
}

void func_random (int a[], int k){
    for (i=0; i<k; i++)
        a[i]=rand()%98+1;
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