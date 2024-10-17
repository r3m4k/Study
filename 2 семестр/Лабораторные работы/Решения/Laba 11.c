/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i;

void func_add (int **a, int n, int element, int num);
void func_swap (int **a, int n, int k);
void func_print (int k, int a[]);

int main()
{
    int n;
    scanf("%d", &n);
    int *p, num_add, element_add, num_swap;
    p=(int*)calloc (n, sizeof(int));
    if (p == NULL) 
        exit(EXIT_FAILURE);
    for (i=0; i<n; i++)
        scanf ("%d", &p[i]);
    scanf ("%d %d %d", &element_add, &num_add, &num_swap);
    func_print (n, p);
    printf("\n");
    n+=1;
    func_add (&p, n, element_add, num_add);
    func_swap (&p, num_swap, n);
    free (p);
    return 0;
}

void func_add (int **a, int n, int element, int num){
    int *q; 
    q=(int*)realloc(*a, n*sizeof(int));
    if (q == NULL) 
        exit(EXIT_FAILURE);
    else {
        for (i=n-1; i>num-1; i--)
            q[i]=q[i-1];
        q[num-1]=element;
    }
}


void func_swap (int **a, int n, int k){
    int element=(*a)[0];
    (*a)[0]=(*a)[n-1];
    (*a)[n-1]=element;
    func_print (k, *a);
}


void func_print (int k, int a[]){
    for (i=0; i<k; i++)
        printf ("%3d", i+1);
    printf ("\n");
    for (i=0; i<k; i++)
        printf ("%3d", a[i]);
    printf ("\n");
}