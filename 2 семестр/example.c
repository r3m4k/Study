/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int i, j, m, n;

void SearchMax(int a[][m],
    int *amax, /* значение искомого элемента */
    int *imax, int *jmax) { /* его координаты */
    *amax=a[0][0];
    *imax=0; *jmax=0;
    for (i=0; i<n; i++)
        for (j=0; j<m; j++){
            if (a[i][j] > *amax) {
                *amax=a[i][j];
                *imax=i; *jmax=j;
            }
        }
}

int main()
{
    int matrix[3][3]={1, 2, 3, 4, 5, 6 , 7, 8, 9};
    int am,im,jm;
    SearchMax(matrix,&am,&im,&jm);
    printf("MAX: matrix[%d][%d]=%d\n",im,jm,am);
    return 0;
}
