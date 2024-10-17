/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i;

void func_count (int n);
void func_Merge (int a[], int n, int first, int last, int *quant_of_compare_MergeSort, int *quant_of_change_MergeSort);
void func_MergeSort(int a[], int n, int first, int last, int *quant_of_compare_QuickSort, int *quant_of_change_QuickSort);
void func_swap (int *a, int *b);

void func_compare_upgraged (int a[], int n, int k, int *quant_of_compare_upgraded, int *quant_of_change_upgraded);
void func_compare (int a[], int n,  int first, int last, int k, int *quant_of_compare, int *quant_of_change);
void func_change(int a[], int n_1, int n_2, int *quant_of_change);

void func_random (int a[], int k);
void func_print (int a[], int k);
void func_scan (int a[], int k);

int main()
{
    int n, k=1, quant_of_compare=0, quant_of_change=0,
        quant_of_compare_upgraded=0, quant_of_change_upgraded=0,
        quant_of_change_MergeSort=0, quant_of_compare_MergeSort=0;
    
    printf ("Введите количество элементов: ");
    scanf ("%d", &n);
    printf ("Исходный массив:\n");
    func_print(m_11, n);
    /*
    func_count (n);
    int m_11[n], m_12[n], m_13[n];
    func_random(m_11, n);
    //func_scan(m, n);
    for (i=0; i<n; i++){
        m_12[i]=m_11[i];
        m_13[i]=m_11[i];
    }
    
    while (k!=n){
        func_compare (m_11, n, 0, k, k, &quant_of_compare, &quant_of_change);
        k+=1;
    }
    
    k=1;
    while (k!=n){
        func_compare_upgraged (m_12, n, k, &quant_of_compare_upgraded, &quant_of_change_upgraded);
        k+=1;
    }
    
    func_MergeSort(m_13, n, 0, n-1, &quant_of_compare_MergeSort, &quant_of_change_MergeSort);
    
    printf ("Количество сравнений и присваиваний при использовании\n\n");
    printf ("Обычного метода сортировки:\nКоличество сравнений --- %d\nКоличество присваиваний --- %d\n\n", quant_of_compare, quant_of_change);
    printf ("Усовершенствованного метода сортировки:\nКоличество сравнений --- %d\nКоличество присваиваний --- %d\n\n", quant_of_compare_upgraded, quant_of_change_upgraded);
    printf ("Метода слияния:\nКоличество сравнений --- %d\nКоличество присваиваний --- %d\n\n", quant_of_compare_MergeSort, quant_of_change_MergeSort);
    */
    printf ("Количество сравнений и присваиваний при различных количествах элементов\n");
    printf ("при использовании различных методов\n\n");
    printf ("Кол-во эл-ов   Кол-во ср-ий    Кол-во присв-ий\n");
    
    
    func_count (n);
    func_count (20);
    func_count (50);
    func_count (100);
    func_count (500);

    return 0;
}

void func_count(int n){
    int m_11[n], m_12[n], m_13[n];
    func_random (m_11, n);
    for (i=0; i<n; i++){
        m_12[i]=m_11[i];
        m_13[i]=m_11[i];
    }
    int k=1, quant_of_compare=0, quant_of_change=0,
        quant_of_compare_upgraded=0, quant_of_change_upgraded=0,
        quant_of_change_MergeSort=0, quant_of_compare_MergeSort=0;
    while (k!=n){
        func_compare (m_11, n, 0, k, k, &quant_of_compare, &quant_of_change);
        k+=1;
    }
    k=1;
    while (k!=n){
        func_compare_upgraged (m_12, n, k, &quant_of_compare_upgraded, &quant_of_change_upgraded);
        k+=1;
    }
    func_MergeSort(m_13, n, 0, n-1, &quant_of_compare_MergeSort, &quant_of_change_MergeSort);
    
    printf ("        %4d   %12d    %14d --- Обычный метод сортировки\n", n, quant_of_compare, quant_of_change);
    printf ("               %12d    %14d --- Усовершенствованный метод сортировки\n", quant_of_compare_upgraded, quant_of_change_upgraded);
    printf ("               %12d    %14d --- Метод слияния\n\n", quant_of_compare_MergeSort, quant_of_change_MergeSort);
}

void func_compare_upgraged (int a[], int n, int k, int *quant_of_compare_upgraded, int *quant_of_change_upgraded){
    if (a[k]==a[k/2]){
        *quant_of_compare_upgraded+=1;
        func_change (a, k/2, k, quant_of_change_upgraded);
    }
    else if (a[k]>a[k/2]){
        *quant_of_compare_upgraded+=1;
        func_compare (a, n, 0, k/2, k, quant_of_compare_upgraded, quant_of_change_upgraded);
    }
    else if (a[k]<a[k/2]){
        *quant_of_compare_upgraded+=1;
        func_compare (a, n, k/2, k, k, quant_of_compare_upgraded, quant_of_change_upgraded);
        
    }
}

void func_compare (int a[], int n, int first, int last, int k, int *quant_of_compare, int *quant_of_change){
    for (i=0; i<last-first; i++){
        *quant_of_compare+=1;
        if (a[k]>=a[first+i]){
            func_change (a, first+i, k, quant_of_change);
            //func_print(a, n);
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
            //printf ("\n");
            //func_print (a, n);
        }
    }
    else {
        *quant_of_compare_MergeSort+=1;
        m=(first+last)/2;
        func_MergeSort(a, n, first, m, quant_of_compare_MergeSort, quant_of_change_MergeSort);
        func_MergeSort(a, n, m+1, last, quant_of_compare_MergeSort, quant_of_change_MergeSort);
        func_Merge(a, n, first, last, quant_of_compare_MergeSort, quant_of_change_MergeSort);
        //func_print (a, n);
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
        }
        else {
            b[k]=a[r]; r++; 
        }
        k++; 
    } /*Один из фрагментов закончился.*/
    /*Переносим остаток другого фрагмента во вспомогательный
    массив.*/
    while (l<=m) {
        b[k]=a[l]; l++; k++; 
    }
    while (r<=last) {
        b[k]=a[r]; r++; k++; 
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
