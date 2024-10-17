/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i, j;

void func_filling (int *arr, int n, int m);
void func_print (int *arr, int n, int m);
void func_transposition (int *arr, int *arr_tr, int n, int m);
int func_sum (int *arr1, int *arr2, int *arr_sum, int n1, int m1, int n2, int m2);
int func_mult (int *arr1, int *arr2, int *arr_mult, int n1, int m1, int n2, int m2, int flag);

int main()
{
    int flag=0;
    int n1, m1,
        n2, m2;
    printf ("Введите размерность первой матрицы: ");
    scanf ("%d %d", &n1, &m1);
    int arr1[n1][m1];    
    func_filling (*arr1, n1, m1);
    
    printf ("Введите размерность второй матрицы: ");
    scanf ("%d %d", &n2, &m2);
    int arr2[n2][m2];    
    func_filling (*arr2, n2, m2);
    
    int arr1_tr[m1][n1];
    func_transposition(*arr1, *arr1_tr, n1, m1);
    int arr1_1tr[n1][m1];
    flag=func_mult (*arr1, *arr1_tr, *arr1_1tr, n1, m1, m1, n1, 2);
    if (flag==0){
        int arr1_1tr_sq[n1][m1];
        flag=func_mult(*arr1_1tr, *arr1_1tr, *arr1_1tr_sq, n1, m1, n1, m1, 3);
        if (flag==0){
            int arr_mult[n1][m2];
            flag=func_mult(*arr1, *arr2, *arr_mult, n1, m1, n2, m2, 2);
            if (flag==0){
                int arr[n1][m1];
                flag=func_sum(*arr_mult, *arr1_1tr_sq, *arr, n1, m2, n1, m1);
                if (flag==0)
                    func_print (*arr, n1, m1);
                else printf("!%d\n", flag);    
            }
            else 
                printf ("!%d\n", flag);
        }
        else
            printf ("!%d\n", flag);
    }
    else
        printf ("!%d\n", flag);

    return 0;
}

void func_filling (int *arr, int n, int m){
    int max, min;
    printf ("Введите диапозон заполнения: ");
    scanf ("%d %d", &min, &max); 
    //min=1; max=20;
    for (i=0; i<n; i++){
        for (j=0; j<m; j++){
            *(arr+i*m + j)=rand()%(max-min+1)+min;
        }
    }
    func_print (arr, n, m);
}

void func_print (int *arr, int n, int m){
    for (i=0; i<n; i++){
        for (j=0; j<m; j++)
            printf ("%7d", *(arr+i*m + j));
        printf ("\n");
    }
    printf ("\n");
}

void func_transposition (int *arr, int *arr_tr, int n, int m){
    for (i=0; i<n; i++){
        for (j=0; j<m; j++)
            *(arr_tr+j*n + i)=*(arr+i*m + j);
    }
    //func_print (arr_tr, m, n);
}

int func_sum (int *arr1, int *arr2, int *arr_sum, int n1, int m1, int n2, int m2){
    if ((n1!=n2)||(m1!=m2))
        return 1;
    else{
        int n=n1, m=m1;
        for (i=0; i<n1; i++){
            for (j=0; j<m1; j++)
                *(arr_sum+i*m + j)=*(arr1+i*m + j)+*(arr2+i*m + j);
        }
        //func_print(arr_sum, n, m);
        return 0;
    }
}

int func_mult (int *arr1, int *arr2, int *arr_mult, int n1, int m1, int n2, int m2, int flag){
    if (m1!=n2){
        if (flag==2)
            return 2;
        else 
            return 3;
    }
    else{
        int k, n=m1;
        for (i=0; i<n1; i++){
            for (j=0; j<m2; j++){
                *(arr_mult+i*m2 + j)=0;
                for (k=0; k<n; k++)
                    *(arr_mult+i*m2+j)+=*(arr1+i*n+k)* *(arr2+k*m2+j);
            }
        }
        //func_print (arr_mult, n1, m2);
        return 0;
    }
}














