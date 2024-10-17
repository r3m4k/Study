/******************************************************************************

Welcome to GDb Online.
  GDb online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, Vb, Perl, Swift, Prolog, Javascript, Pascal, CObOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i;

void func_QuickSort (int a[], int n, int first, int last, int *quant_of_compare_QuickSort, int  *quant_of_change_QuickSort);
void func_Merge (int a[], int n, int first, int last, int *quant_of_compare_MergeSort, int *quant_of_change_MergeSort);
void func_MergeSort(int a[], int n, int first, int last, int *quant_of_compare_QuickSort, int *quant_of_change_QuickSort);
void func_swap (int *a, int *b);
void func_random (int a[], int k);
void func_print (int a[], int k);
void func_scan (int a[], int k);

int main()
{
    int n;
    scanf ("%d", &n);
    int m[n], m_q[n], m_m[n], quant_of_change_QuickSort=0, quant_of_compare_QuickSort=0,
        quant_of_change_MergeSort=0, quant_of_compare_MergeSort=0;
    func_random (m, n);
    //func_scan(m, n);
    for (i=0; i<n; i++){
        m_q[i]=m[i];
        m_m[i]=m[i];
    }
    func_print (m_q, n);
    func_QuickSort (m_q, n, 0, n-1, &quant_of_compare_QuickSort, &quant_of_change_QuickSort);
    printf ("%3d %3d\n\n", quant_of_change_QuickSort, quant_of_compare_QuickSort);
    func_MergeSort(m_m, n, 0, n-1, &quant_of_compare_MergeSort, &quant_of_change_MergeSort);
    printf ("%3d %3d\n", quant_of_change_MergeSort, quant_of_compare_MergeSort);
    return 0;
}

void func_QuickSort (int a[], int n, int first, int last, int *quant_of_compare_QuickSort, int *quant_of_change_QuickSort)
{
    int pivot; /*опорное значение*/
    int l,r; /*левый и правый счетчики*/
    l=first; r=last;
    pivot=a[(l+r)/2]; /*определение опорного значения*/
    while (l<=r) {
        while (a[l]>pivot) l++;
        *quant_of_compare_QuickSort+=1;
        while (a[r]<pivot) r--;
        *quant_of_compare_QuickSort+=1;
        if (l<=r) {
            func_swap(&a[r],&a[l]); /*перестановка двух элементов*/
            *quant_of_change_QuickSort+=3;
            printf ("\n");
            func_print (a, n);
            l++;
            r--;
        }
    } /*Рекурсивная сортировка:*/
    if (first<r) func_QuickSort(a, n, first, r, quant_of_compare_QuickSort, quant_of_change_QuickSort); /*- левого участка, */
    if (l<last) func_QuickSort(a, n, l, last, quant_of_compare_QuickSort, quant_of_compare_QuickSort); /*- правого участка.*/
}

void func_MergeSort(int a[], int n, int first, int last, int *quant_of_compare_MergeSort, int *quant_of_change_MergeSort)
{
    int m; /*индекс среднего элемента*/
    if (first<last)
    if (last-first==1) {
        *quant_of_compare_MergeSort+=1;
        if (a[last]>a[first]){
            func_swap(&a[first],&a[last]);
            *quant_of_compare_MergeSort+=1;
            *quant_of_change_MergeSort+=3;
            printf ("\n");
            func_print (a, n);
        }
    }
    else {
        *quant_of_compare_MergeSort+=1;
        m=(first+last)/2;
        func_MergeSort(a, n, first, m, quant_of_compare_MergeSort, quant_of_change_MergeSort);
        func_MergeSort(a, n, m+1, last, quant_of_compare_MergeSort, quant_of_change_MergeSort);
        func_Merge(a, n, first, last, quant_of_compare_MergeSort, quant_of_change_MergeSort);
        printf ("\n");
        func_print (a, n);
    }
}

void func_Merge(int a[], int n, int first, int last, int *quant_of_compare_MergeSort, int *quant_of_change_MergeSort)
{
    int b[n]; /*вспомогательный массив*/
    int k; /*индекс во вспомогательном массиве*/
    int l,r; /*левый и правый счетчики*/
    int m; /*индекс среднего элемента*/
    m=(first+last)/2;
    l=first; r=m+1;
    k=0;
    while (l<=m && r<=last) { /* Пока не закончился */
        if (a[l]>=a[r]) { /*хотя бы один фрагмент.*/
            b[k]=a[l]; l++; 
            *quant_of_compare_MergeSort+=1;
            *quant_of_change_MergeSort+=1;
        }
        else {
            b[k]=a[r]; r++; 
            *quant_of_change_MergeSort+=1;
        }
        k++; 
    } /*Один из фрагментов закончился.*/
    /*Переносим остаток другого фрагмента во вспомогательный
    массив.*/
    while (l<=m) {
        b[k]=a[l]; l++; k++; 
        *quant_of_change_MergeSort+=1;
    }
    while (r<=last) {
        b[k]=a[r]; r++; k++; 
        *quant_of_change_MergeSort+=1;
    }
    for (l=0; l<k; l++){
        a[first+l]=b[l];
        *quant_of_change_MergeSort+=1;
    }
}

void func_swap (int *a, int *b){
    int c;
    c=*a;
    *a=*b;
    *b=c;
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

void func_scan (int a[], int k){
    for (i=0; i<k; i++)
        scanf("%d", &a[i]);
}
